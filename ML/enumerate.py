for i, char in enumerate('Hellooooo', 1):
    print(i, char)

for index, char in enumerate(list(range(100))):
    if char == 50:
        print(f'index of 50 is: {index}')