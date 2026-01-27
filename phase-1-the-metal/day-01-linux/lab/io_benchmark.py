import mmap
import os
import time
import random

FILE_SIZE_MB = 500  # 500MB test file
FILENAME = "/tmp/io_benchmark.dat"


def generate_file():
    if os.path.exists(FILENAME):
        print(f"Using existing file: {FILENAME}")
        return

    print(f"Generating {FILE_SIZE_MB}MB test file... (this may take a moment)")
    with open(FILENAME, "wb") as f:
        # Write 1MB chunks
        chunk = os.urandom(1024 * 1024)
        for _ in range(FILE_SIZE_MB):
            f.write(chunk)
    print("✅ File generated.")


def benchmark_syscall_read():
    print(f"\n[1] Testing Traditional read() Syscalls...")
    start_time = time.time()

    bytes_read = 0
    with open(FILENAME, "rb") as f:
        # Simulate random access (seeking) which hurts HDD/SSD
        # We do 5,000 random reads of 4KB
        for _ in range(5000):
            f.seek(random.randint(0, (FILE_SIZE_MB * 1024 * 1024) - 4096))
            data = f.read(4096)
            bytes_read += len(data)

    duration = time.time() - start_time
    print(f"    Time: {duration:.4f} seconds")
    return duration


def benchmark_mmap_read():
    print(f"\n[2] Testing Memory Mapped (mmap) Access...")
    start_time = time.time()

    bytes_read = 0
    with open(FILENAME, "r+b") as f:
        # Map the file into memory
        mm = mmap.mmap(f.fileno(), 0)

        # Exact same workload: 5,000 random reads
        for _ in range(5000):
            pos = random.randint(0, (FILE_SIZE_MB * 1024 * 1024) - 4096)
            # Slice memory instead of calling read()
            data = mm[pos:pos + 4096]
            bytes_read += len(data)

        mm.close()

    duration = time.time() - start_time
    print(f"    Time: {duration:.4f} seconds")
    return duration


if __name__ == "__main__":
    try:
        generate_file()

        t_sys = benchmark_syscall_read()
        t_mmap = benchmark_mmap_read()

        print("\n" + "=" * 40)
        print("🏆 RESULTS")
        print("=" * 40)
        print(f"Traditional I/O: {t_sys:.4f}s")
        print(f"Memory Mapped:   {t_mmap:.4f}s")
        print("-" * 40)
        print(f"Speedup: {t_sys / t_mmap:.1f}x FASTER")

        # Cleanup
        os.remove(FILENAME)

    except KeyboardInterrupt:
        print("\nCancelled.")
        