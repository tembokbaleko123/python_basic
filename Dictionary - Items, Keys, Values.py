#menampilkan seluruh key yang ada di dalam sebuah dictionary dengan fungsi keys()
dic = {'a': 10,'b': 20,'c': 30, 'd': 40}
print(dic.keys()) # mengakses seluruh key yang ada dalam dictionary

#menampilkan seluruh value yang ada di dalam sebuah dictionary dengan fungsi values()
dic = {'a': 10,'b': 20,'c': 30, 'd': 40}
print(dic.values()) # mengakses seluruh values yang ada dalam dictionary

#Kita juga dapat mengakses seluruh item dalam sebuah dictionary dengan fungsi items(). Jika fungsi items() digunakan menggunakan for loop maka akan mengembalikan sebuah tipe data tuple yang berisi (key,value)
dic = {'a': 10,'b': 20,'c': 30, 'd': 40}
print(dic.items()) # mengakses seluruh items yang ada dalam dictionary

# kita juga bisa menggunakan *for loop* untuk mengakses seluruh *item* satu per satu

for str1,num, in dic.items():
    print(str1,':',num)