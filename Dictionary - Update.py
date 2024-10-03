#update(). Fungsi update(key=value) memodifikasi nilai key dalam sebuah dictionary
dic = {'a': 10,'b': 20,'c': 30, 'd': 40}
print(dic)
dic.update(a=90) # mengupdate value dari key a
print(dic)

#Namun jika kita menggunakan fungsi update() untuk sebuah key yang belum tersedia, maka fungsi update() akan berfungsi untuk menambahkan key-value pair tersebut ke dalam dictionary


#dapat mengupdate beberapa key-value pair secara bersamaan dalam fungsi update()
dic.update(a=900,f=60) # mengupdate value a dan menambahkan key dan value f
print(dic)