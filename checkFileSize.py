import os

class checkFileSize:
    def convert_bytes(num: int):
        """
        Function to convert bytes to MB, GB etc.
        """
        for size in ['bytes', 'KB', 'MB', 'GB', 'TB']:
            if num < 1024.0:
                return f'{num:.1f} {size}'
            num /= 1024.0


    def file_size(self, file_path, ):
        """
        to return the file size
        """
        if os.path.isfile(file_path):
            file_info = os.stat(file_path)
            file_size = file_info.st_size
            return self.convert_bytes(file_size)
        
    
    