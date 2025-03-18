log_file_path = input(f'pleae pase the file path ')

error_count = 0

with open (log_file_path, 'r') as file:
    for line in file:
        if "404" in line:
            error_count += 1
            

print (f'the number of 404 errors : {error_count}')