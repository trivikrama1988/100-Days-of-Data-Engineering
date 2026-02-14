import time
import multiprocessing

def heavy_task(n):
    # Simulate CPU work: Calculate sum of squares for a large range
    count = 0
    # Reducing range slightly for quick demo, but enough to burn CPU
    for i in range(3_000_000):
        count += i * i
    return count

if __name__ == "__main__":
    # 8 heavy tasks to process
    tasks = list(range(8)) 
    
    print(f"--- Processing {len(tasks)} CPU-heavy tasks ---")
    
    # 1. Sequential Execution (Single Core)
    start = time.time()
    for t in tasks:
        heavy_task(t)
    seq_time = time.time() - start
    print(f"Sequential Time: {seq_time:.4f}s")
    
    # 2. Parallel Execution (Multi-Core)
    # We use 4 workers (simulating 'xargs -P 4')
    start = time.time()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(heavy_task, tasks)
    par_time = time.time() - start
    print(f"Parallel (4 workers) Time: {par_time:.4f}s")
    
    print(f"\n>>> Speedup: {seq_time / par_time:.2f}x")
