#list
list1 = [11,11,11,22,33,44] 
print(list1.count(11)) # mencari total angka 11 dalam list

#Tupple
tup1 = (11,11,11,22,33,44) 
print(tup1.count(11)) # mencari total angka 11 dalam tuple

#string
str1 = 'hello world'
print(str1.count('l')) # mencari total huruf l dalam string

#Contoh penggunaan dan aplikasi metode count() dalam kode:
ran = range(0,5,1)
print(len(ran))
print(ran.count(2))

#ran memiliki lima elemen 0, 1, 2, 3, 4. Banyaknya elemen yang dicetak dengan menggunakan fungsi len adalah 5.Pada sisi lain, ketika menggunakan metode count() untuk melihat berapa banyak angka 2 dalam variabel yang dijalankan, itu akan mencetak 1 karena hanya ada satu angka 2 dari range 0 hingga 5."""