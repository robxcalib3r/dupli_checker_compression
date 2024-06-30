## Dupli Checker and Compression
This project is intended to check duplicate files in a directory and compress them with reasonable compression ratio

### Probable Algorithm to check duplicates
#### courtesy to https://stackoverflow.com/a/9808270
1. Check if file size is equal
2. if step 1 passes, check if first and last range of bytes (say 100 bytes) are equal
3. if step 2 passes, check file type,
4. if step 3 passes, check the hash