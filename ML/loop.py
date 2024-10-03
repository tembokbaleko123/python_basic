li1 = [
    'tes',
    'oke',
    'sudah'
]

for item in li1:
    print(item)


for i in (1,2,3,4,5):
    for x in ['a','b','c']:
        print(i, x)

# Dictionary iterable
user = {
    "name": "John",
    "age": 30,
    'can swim' : False
}

for i in user.keys():
    print(i)

for i in user.values():
    print(i) 

for i in user.items():
    print(i)