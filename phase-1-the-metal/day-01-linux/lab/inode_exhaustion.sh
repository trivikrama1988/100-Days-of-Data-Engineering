#!/bin/bash
# Path: phase-1-the-metal/day-01-linux/lab/inode_exhaustion.sh

FS="/tmp/test_fs"
MOUNT="$FS/mnt"
DATA="$FS/data"

# Safety check: Ensure we are on Linux
if [[ "$OSTYPE" != "linux-gnu"* ]]; then
    echo "❌ Error: This lab requires a Linux Kernel (VM or Native)."
    exit 1
fi

# Create filesystem with limited inodes (requires sudo)
echo "🔒 Creating loopback filesystem..."
mkdir -p $MOUNT $DATA
dd if=/dev/zero of=$FS/disk.img bs=1M count=100 status=none
mkfs.ext4 -N 1000 $FS/disk.img > /dev/null 2>&1
sudo mount -o loop $FS/disk.img $MOUNT

echo "=== 🧪 Starting Inode Exhaustion Test ==="
echo "Disk size: 100MB | Inode count: 1000"

# Fill with empty files
for i in {1..2000}; do
    touch $MOUNT/file_$i 2>/dev/null
    if [ $? -ne 0 ]; then
        echo "✅ Success: Failed at file $i (Inodes exhausted!)"
        break
    fi
done

echo ""
echo "--- Evidence ---"
df -h $MOUNT | grep "/tmp"
df -i $MOUNT | grep "/tmp"

# Cleanup
echo ""
echo "🧹 Cleaning up..."
sudo umount $MOUNT
rm -rf $FS