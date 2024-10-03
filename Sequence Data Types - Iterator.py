#List
list1 = [11,22,33,44] * 2
print(list1)


#Tuples
tup1 = (1,2,3)
print(tup1 * 2)


#String
str2 = 'hello'
print(str2 * 3)

#Range = tidak bisa menggunakan * harus diubah ke list/tuple terlebih dahulu
ran = list(range(5)) * 3
print(ran)


ran = tuple(range(5)) * 3
print(ran)
