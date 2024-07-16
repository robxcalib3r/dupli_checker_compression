import os
import hashlib
import mimetypes

def get_file_size(file_path):
    return os.path.getsize(file_path)

# def read_file_bytes(file_path, num_bytes, position='start'):
#     with open(file_path, 'rb') as f:
#         if position == 'start':
#             return f.read(num_bytes)
#         elif position == 'end':
#             f.seek(-num_bytes, os.SEEK_END)
#             return f.read(num_bytes)
#     return None

def get_file_type(file_path):
    return mimetypes.guess_type(file_path)[0]

def get_file_hash(file_path, hash_algo=hashlib.sha256):
    hash_func = hash_algo()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            hash_func.update(chunk)
    return hash_func.hexdigest()

def compare_files(file1, file2, byte_range=100):
    # Step 1: Check if file size is equal
    if get_file_size(file1) != get_file_size(file2):
        return False
    
    # # Step 2: Check if first and last range of bytes are equal
    # if (read_file_bytes(file1, byte_range, 'start') != read_file_bytes(file2, byte_range, 'start') or
    #     read_file_bytes(file1, byte_range, 'end') != read_file_bytes(file2, byte_range, 'end')):
    #     return False

    # Step 3: Check file type
    if get_file_type(file1) != get_file_type(file2):
        return False
    
    # Step 4: Check hash
    if get_file_hash(file1) != get_file_hash(file2):
        return False

    return True

# Example usage
file1 = 'random_file.bin'
file2 = 'random_file1.bin'

if compare_files(file1, file2):
    print("Files are considered equal based on the criteria.")
else:
    print("Files are not equal based on the criteria.")
