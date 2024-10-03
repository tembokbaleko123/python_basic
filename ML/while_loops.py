i = 0

while i < 50:
    i += 1
    # Pada python hasil (i+= 1) dan (i = i + 1) itu beda
    print(i)
else:
    # comment: 
    print('done with all work')

while True:
    response = input('say something: ')
    if (response == 'bye'):
        break