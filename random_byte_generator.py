import os

def generate_random_file(file_name, size_in_bytes):
    with open(file_name, 'wb') as f:
        f.write(os.urandom(size_in_bytes))

# Example usage
file_name = 'random_file1.bin'
size_in_bytes = 1024 * 1024 * 1024   # 1 MB
generate_random_file(file_name, size_in_bytes)
print(f"Random file '{file_name}' of size {size_in_bytes} bytes created.")