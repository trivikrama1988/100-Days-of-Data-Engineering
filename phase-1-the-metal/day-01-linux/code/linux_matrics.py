"""
[Day 1 Code] Linux Kernel Metrics Inspector
Author: Senior Data Engineer
Description:
    Reads kernel statistics directly from the /proc virtual filesystem.
    This demonstrates the "Everything is a File" philosophy.
    No external libraries (like psutil) are used, just standard I/O.
"""

import os
import time


def read_proc_file(filepath):
    """Helper to read raw content from /proc files"""
    try:
        with open(filepath, 'r') as f:
            return f.read().strip()
    except FileNotFoundError:
        return None


def get_load_average():
    """Reads /proc/loadavg to see system pressure"""
    # Content format: 0.00 0.01 0.05 1/456 12345
    data = read_proc_file('/proc/loadavg')
    if data:
        parts = data.split()
        return {
            '1_min': float(parts[0]),
            '5_min': float(parts[1]),
            '15_min': float(parts[2]),
            'sched_entities': parts[3]
        }
    return {}


def get_memory_info():
    """Reads /proc/meminfo to see Page Cache usage"""
    # The kernel exposes RAM usage here. Critical for understanding caching.
    data = read_proc_file('/proc/meminfo')
    mem_stats = {}
    if data:
        for line in data.split('\n'):
            parts = line.split(':')
            if len(parts) == 2:
                key = parts[0].strip()
                # value is usually like "16384 kB"
                value = parts[1].strip().split()[0]
                mem_stats[key] = int(value)

    return {
        'Total': mem_stats.get('MemTotal', 0),
        'Free': mem_stats.get('MemFree', 0),
        'Cached': mem_stats.get('Cached', 0),  # This is the Page Cache!
        'Buffers': mem_stats.get('Buffers', 0)
    }


def get_open_fd_count():
    """Counts files in /proc/sys/fs/file-nr"""
    # Content: <allocated> <free> <max>
    data = read_proc_file('/proc/sys/fs/file-nr')
    if data:
        parts = data.split()
        return {
            'allocated': int(parts[0]),
            'unused': int(parts[1]),
            'max_limit': int(parts[2])
        }
    return {}


def main():
    print("=== 🐧 THE METAL INSPECTOR ===")
    print("Reading directly from /proc (Kernel Memory)...\n")

    # 1. Load Average
    load = get_load_average()
    print(f"1. SYSTEM LOAD: {load.get('1_min')} (1 min)")

    # 2. File Descriptors
    fds = get_open_fd_count()
    print(f"2. OPEN FILES:  {fds.get('allocated')} / {fds.get('max_limit')} (System Wide)")

    # 3. Memory & Cache
    mem = get_memory_info()
    total_mb = mem['Total'] // 1024
    cached_mb = mem['Cached'] // 1024
    percent_cached = (cached_mb / total_mb) * 100

    print(f"3. MEMORY:      {total_mb} MB Total")
    print(f"   └─ Page Cache: {cached_mb} MB ({percent_cached:.1f}%)")
    print("      (This is data sitting in RAM to avoid Disk I/O)")


if __name__ == "__main__":
    main()