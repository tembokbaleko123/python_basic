#pop() dalam dictionary dapat digunakan sebagai salah satu metode untuk menghapus item dari sebuah dictionary
dic = {'a': 10,'b': 20,'c': 30, 'd': 40}
print(dic.pop('a')) # meremove key-value pair dengan key a
print(dic)

#popitem() juga merupakan metode untuk menghapus sebuah elemen dari dictionary, namun fungsi popitem() menghapus key-value pair apa pun dari sebuah dictionary dan mengembalikan key-value pair yang dihapus dalam bentuk tipe data tuple.
print(dic.popitem())

#clear() Untuk menghapus seluruh key-value pair dari sebuah dictionary
dic.clear() # meremove semua value dalam dictionary dic
print(dic) 