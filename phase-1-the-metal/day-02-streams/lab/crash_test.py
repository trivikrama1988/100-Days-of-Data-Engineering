# crash_test.py
print("Attempting to load 10GB into RAM...")
with open("massive_file2.txt", "r") as f:
    data = f.readlines() # This tries to store every line as a string object in a list
    print(f"Loaded {len(data)} lines.")