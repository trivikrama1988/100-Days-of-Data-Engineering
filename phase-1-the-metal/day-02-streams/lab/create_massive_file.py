import os
path_file = os.path.join(os.getcwd(),"massive_file2.txt")
with open(path_file, "w") as f:
    for i in range(10**8):
        f.write(f"This is line {i}\n")
