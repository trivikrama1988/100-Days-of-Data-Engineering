### **DAY 1: THE PHYSICS OF DATA — LINUX KERNEL & I/O**

```
phase-1-the-metal/
└── day-01-linux/
    ├── README.md               # The Deep Theory (Architecture, Diagrams)
    ├── code/                   # The Builder's Tools
    │   ├── linux_metrics.py    # /proc inspector
    │   └── buffered_writer.py  # Best-practice I/O pattern
    └── lab/                    # The Breaker's Tools
        ├── requirements.txt
        ├── inode_exhaustion.sh # Crash the disk with empty files
        ├── fd_leak_detector.py # Crash the process with open files
        └── io_benchmark.py     # Measure read() vs mmap()
```