#copy() Dalam sebuah dictionary kita bisa menggunakan fungsi copy() untuk membuat replika dari dictionary tersebut.
x = {'a': 0, 'b': 0 , 'c': 0, 'd': 0}
y = x.copy()

#deepcopy() Apabila kita ingin membuat replika dari sebuah double dictionary, kita tidak bisa menggunakan metode copy(). Berikut contoh jika kita melakukan replika menggunakan metode copy() pada tipe data double dictionary


b = {'a': {'python':'2.7'},'b':{'python':'3.6'}}
o = b.copy()

o['a']['python'] = '2.7.15' # merubah value dari key a - python
print(x)
print(y)


#double dictionary kita bisa menggunakan fungsi deepcopy(). Namun perbedaannya jika kita ingin memanggil deepcopy(), kita harus melakukan import terlebih dahulu dari copy module.
import copy

y = copy.deepcopy(dictionary_yang_ingin_dicopy)
x = {'a': {'python':'2.7'},'b':{'python':'3.6'}}
import copy # memanggil copy module
y = copy.deepcopy(x) # deep copy menggunakan deepcopy function dari copy module

y['a']['python'] = '2.7.15' # merubah value dari key a - python
print(x)
print(y)
