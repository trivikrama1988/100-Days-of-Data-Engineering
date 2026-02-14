import time
import os

INPUT_FILE = "tool_race_data.txt"
LINE_COUNT = 1_000_000

def ensure_data():
    if not os.path.exists(INPUT_FILE):
        print("Generating data...")
        with open(INPUT_FILE, "w") as f:
            for i in range(LINE_COUNT):
                # 9999 is rare, most lines just text
                f.write(f"Log Entry {i} [INFO] System status normal with value {i}\n")

def python_grep_simulation():
    # Simulates grep: Just check for substring existence
    print("Running Grep Simulation (Substring Check)...")
    start = time.time()
    count = 0
    with open(INPUT_FILE, 'r') as f:
        for line in f:
            if '9999' in line:
                count += 1
    duration = time.time() - start
    print(f"  Time: {duration:.4f}s")
    return duration

def python_awk_simulation():
    # Simulates awk: Split line into fields first
    print("Running Awk Simulation (Field Parsing)...")
    start = time.time()
    count = 0
    with open(INPUT_FILE, 'r') as f:
        for line in f:
            # The Cost of Structure: Splitting
            fields = line.split()
            # Logic checking a field (awk style)
            if len(fields) > 7 and '9999' in fields[7]: 
                count += 1
    duration = time.time() - start
    print(f"  Time: {duration:.4f}s")
    return duration

if __name__ == "__main__":
    ensure_data()
    
    t_grep = python_grep_simulation()
    t_awk = python_awk_simulation()
    
    print(f"\n>>> Result: Grep-style (Scanning) was {t_awk / t_grep:.1f}x faster than Awk-style (Parsing).")
    if os.path.exists(INPUT_FILE): os.remove(INPUT_FILE)
