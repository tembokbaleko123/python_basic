username = input("Please enter username: ")
password = input("Please enter password: ")

lenght = '*' * len(password)

print(f'{username}, your password {password} is {lenght} letters long')