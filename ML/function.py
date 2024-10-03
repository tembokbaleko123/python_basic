def say_hello():
    print("Hello!")

say_hello()

print(say_hello) # Outputnya berupa dimana tempat memory-nya disimpan

# Parameter
# def hi(name, emoji):
#     print(f'Halo {name} {emoji}')

# Default parameter yaitu inputan yang sudah ada isinya
def hi(name='Farid', emoji='👲'):
    print(f'Halo {name} {emoji}')

# Arguments dan positional default arguments
hi(input('Namamu: '), '🕵️‍♀️') # Orang-orang sering memanggilnya sebagai call, invoke

# keyword arguments
hi(emoji= '👮‍♂️', name = 'Farid')

def sum(sum1, sum2):
    tes = sum1 + sum2
    # print(tes) # kalau ada print maka tidak perlu return
    return tes 

print(sum(1, 2))