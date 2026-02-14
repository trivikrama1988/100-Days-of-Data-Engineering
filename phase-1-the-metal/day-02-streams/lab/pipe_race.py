import time
import os
import sys

DATA_SIZE_LINES = 500_000 # 500k lines
INPUT_FILE = "large_input.txt"
TEMP_FILE = "temp_intermediate.txt"

def generate_data():
    if not os.path.exists(INPUT_FILE):
        print(f"Generating {DATA_SIZE_LINES} lines text file...")
        with open(INPUT_FILE, "w","utf-8") as f:
            # Write lines: "Row <ID> <RandomNum>"
            for i in range(DATA_SIZE_LINES):
                f.write(f"Row {i} {i*2} \n")
    print("Input file ready.")

def benchmark_disk_based():
    print("\n[1] Disk-Based (Intermediate File)...")
    start = time.time()
    
    # Step 1: Grep to file (Simulating 'grep > file')
    # We use python list processing to simulate the I/O steps clearly
    # Write to temp file
    with open(INPUT_FILE, 'r') as fin, open(TEMP_FILE, 'w') as fout:
        for line in fin:
            if 'Row' in line:
                fout.write(line)
    
    # Step 2: Read from file and process (Simulating 'awk < file')
    count = 0
    with open(TEMP_FILE, 'r') as fin:
        for line in fin:
            parts = line.split()
            if len(parts) > 2:
                count += 1
    
    duration = time.time() - start
    print(f"    Time: {duration:.4f}s")
    if os.path.exists(TEMP_FILE): os.remove(TEMP_FILE)
    return duration

def benchmark_pipe_based():
    print("\n[2] Stream-Based (Pipe logic)...")
    # Simulating grep | awk behavior in memory (Iterating once)
    start = time.time()
    
    count = 0
    with open(INPUT_FILE, 'r') as fin:
        for line in fin:
            # Pipeline Stage 1: Filter
            if 'Row' in line:
                # Pipeline Stage 2: Process
                parts = line.split()
                if len(parts) > 2:
                    count += 1
    
    duration = time.time() - start
    print(f"    Time: {duration:.4f}s")
    return duration

if __name__ == "__main__":
    generate_data()
    t_disk = benchmark_disk_based()
    t_pipe = benchmark_pipe_based()
    
    print(f"\n Speedup: {t_disk / t_pipe:.2f}x faster using Stream Logic")
    # Cleanup input file to save space
    if os.path.exists(INPUT_FILE): os.remove(INPUT_FILE)
