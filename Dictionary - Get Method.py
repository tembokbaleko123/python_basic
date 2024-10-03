#Fungsi get() dapat kita gunakan untuk mendapatkan value dari key yang spesifik.
dic = {'a':10,'b':20,'c':30,'d':40}
a = dic.get('a') # fungsi get untuk mendapatkan value dari key a
print(a)

#Kita juga dapat memberikan default value dalam sebuah fungsi get().
dic.get(key,default_value)