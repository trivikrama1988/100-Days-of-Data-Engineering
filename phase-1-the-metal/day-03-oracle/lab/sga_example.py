import multiprocessing
import time
import random


def db_user(user_id, sga_counter, lock):
    """Simulates a User Process connecting to Oracle"""
    # PGA (Private Memory): Only this function sees it
    pga_variable = random.randint(1, 100)

    # SGA (Shared Memory): All processes see/modify this
    with lock:  # Oracle uses 'Latches' (Locks) to protect SGA
        current_val = sga_counter.value
        time.sleep(0.01)  # Simulate CPU work
        sga_counter.value = current_val + 1

    print(f"[User {user_id}] PGA={pga_variable}, SGA_Counter={sga_counter.value}")


if __name__ == "__main__":
    print("--- Starting Instance Simulation ---")

    # 1. Allocate SGA (Shared Value)
    sga_counter = multiprocessing.Value('i', 0)
    sga_lock = multiprocessing.Lock()

    # 2. Spawn 5 User Processes
    processes = []
    for i in range(5):
        p = multiprocessing.Process(target=db_user, args=(i, sga_counter, sga_lock))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print(f"--- Final SGA Value: {sga_counter.value} (Should be 5) ---")