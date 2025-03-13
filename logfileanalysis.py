log_file = "access.log"

error_count = 0

with open (log_file , 'r') as file:
    for line in file:
        if "404" in line:
            error_count += 1
            


print (f'the number of 404 errors : {error_count}')