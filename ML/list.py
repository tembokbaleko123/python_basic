
amazon_cart = [
    'notebooks',
    'sunglasses',
    'toys',
    'grapes'
]

# List Slicing
# sama seperti str indexes [start:stop:stepover]

amazon_cart[0] = 'laptop' # untuk mengubah
new_cart = amazon_cart[:] # agak tricky disini kalau new_cart = amazon_cart maka itu bukan mengcopy 
# melainkan new_cart dan amazon_cart adalah sama jadinya satu yang dirubah (mau itu new_cart atau amazon_cart) 
# maka itu akan berubah
new_cart[0] = 'gum'

print(new_cart)
print(amazon_cart[0:]) 

# adding
amazon_cart.append('book')
amazon_cart.insert(2, 'game')
print(amazon_cart)

# removing
amazon_cart.pop()
amazon_cart.pop(0)
amazon_cart.remove('game')
print(amazon_cart)
# amazon_cart.clear()
# print(amazon_cart) # ini akan menghapus semua item di list amazon_cart

# sort() = shorting
amazon_cart.sort()
print(amazon_cart)
amazon_cart.reverse()