import os
import time
import random

FILE_SIZE_MB = 10
CHUNK_SIZE = 1024 # 1KB records
NUM_WRITES = 5000

redo_file = "redo_log.log"
data_file = "datafile.dbf"

# Pre-allocate the data file (Simulating a real DB file)
with open(data_file, "wb") as f:
    f.write(b'\0' * (FILE_SIZE_MB * 1024 * 1024))

print(f"--- Racing {NUM_WRITES} writes ---")

# 1. Sequential Write (LGWR simulation)
start = time.time()
with open(redo_file, "wb") as f:
    for i in range(NUM_WRITES):
        f.write(os.urandom(CHUNK_SIZE)) # Always appending at the end
print(f"Sequential (Redo Log): {time.time() - start:.4f} seconds")

# 2. Random Write (DBWn simulation)
start = time.time()
with open(data_file, "r+b") as f:
    for i in range(NUM_WRITES):
        # Seek to a random location in the file
        random_pos = random.randint(0, FILE_SIZE_MB * 1024 * 1024 - CHUNK_SIZE)
        f.seek(random_pos)
        f.write(os.urandom(CHUNK_SIZE))
print(f"Random (Datafile):     {time.time() - start:.4f} seconds")

# Result: Sequential is usually 10x-50x faster!
if os.path.exists(redo_file): os.remove(redo_file)
if os.path.exists(data_file): os.remove(data_file)