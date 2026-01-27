"""
[Day 1 Code] Smart Buffered Writer
Author: Senior Data Engineer
Description:
    A robust pattern to solve the "Small File Problem".
    Instead of performing a System Call (write) for every record,
    we buffer data in User Space (Ring 3) and flush to Kernel Space (Ring 0)
    only when necessary.
"""

import time
import os


class SmartWriter:
    def __init__(self, filename, buffer_size=4096):
        """
        :param filename: Target file path
        :param buffer_size: Size in bytes before flushing (Default 4KB)
        """
        self.filename = filename
        self.buffer_size = buffer_size
        self._buffer = bytearray()
        self._fd = None
        self._write_count = 0  # Track syscalls

    def __enter__(self):
        # Open file in binary write mode
        self._fd = open(self.filename, 'wb')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.flush()
        if self._fd:
            self._fd.close()
        print(f"\n[Stats] Total System Calls (Writes): {self._write_count}")

    def write(self, data):
        """
        Adds data to internal memory buffer.
        Only triggers OS Write if buffer is full.
        """
        # Convert string to bytes if needed
        if isinstance(data, str):
            data = data.encode('utf-8')

        self._buffer.extend(data)

        # Check if we exceeded buffer size
        if len(self._buffer) >= self.buffer_size:
            self._flush_to_disk()

    def flush(self):
        """Force write remaining data"""
        if self._buffer:
            self._flush_to_disk()

    def _flush_to_disk(self):
        """The expensive operation: Crossing Ring 3 -> Ring 0"""
        if self._fd:
            self._fd.write(self._buffer)
            self._write_count += 1
            # Clear buffer
            self._buffer = bytearray()


# --- Usage Example ---
if __name__ == "__main__":
    OUT_FILE = "/tmp/smart_test.txt"
    RECORDS = 100000

    print(f"Processing {RECORDS} records with Smart Buffering...")
    start = time.time()

    # We create a 8KB buffer (2 memory pages)
    with SmartWriter(OUT_FILE, buffer_size=8192) as writer:
        for i in range(RECORDS):
            # Simulating small log entries
            writer.write(f"Log_Entry_{i}: timestamp={time.time()}\n")

    print(f"Done in {time.time() - start:.4f}s")

    # Verify file exists
    size = os.path.getsize(OUT_FILE)
    print(f"File created: {size / 1024:.2f} KB")

    # Cleanup
    os.remove(OUT_FILE)