import os
import psutil
import time
import sys


def print_status(proc):
    """Query the Kernel for FD usage"""
    try:
        # Get current FD count for this process
        num_fds = proc.num_fds()
        # Get Soft and Hard limits
        soft, hard = proc.rlimit(psutil.RLIMIT_NOFILE)

        # Calculate percentage
        usage = (num_fds / soft) * 100

        bar = "█" * int(usage // 5) + "-" * (20 - int(usage // 5))
        print(f"\rFD Usage: [{bar}] {num_fds}/{soft} ({usage:.1f}%)", end="")
        sys.stdout.flush()

        return num_fds < soft
    except psutil.AccessDenied:
        return False


def run_leak_simulation():
    print("--- 🔥 Starting File Descriptor Leak Simulation ---")
    pid = os.getpid()
    proc = psutil.Process(pid)

    soft, hard = proc.rlimit(psutil.RLIMIT_NOFILE)
    print(f"Process ID: {pid}")
    print(f"System Limits: Soft={soft}, Hard={hard}")
    print("Beginning leak... (Press Ctrl+C to stop early)\n")

    files = []

    try:
        # Loop until we hit the limit
        for i in range(5000):
            # OPEN file but NEVER CLOSE it
            f = open(f"/dev/null", "r")
            files.append(f)

            # Update status every 50 iterations
            if i % 50 == 0:
                if not print_status(proc):
                    print("\n\n❌ CRASH: Hit System Limit!")
                    break

            # Artificial delay to make it visible
            time.sleep(0.002)

    except OSError as e:
        print(f"\n\n💥 OS Error Triggered: {e}")
        print("The Kernel successfully blocked further allocations.")

    finally:
        print("\n\n🧹 Cleaning up (Closing all files)...")
        for f in files:
            f.close()
        print(f"Released {len(files)} file descriptors.")
        print("✅ Done.")


if __name__ == "__main__":
    run_leak_simulation()