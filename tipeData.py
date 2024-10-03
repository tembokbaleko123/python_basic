#String dengan multi line (lihat aja)
contoh = """Yoo...
Sudah lama yaa, terakhir kita bertemu 1 tahun yang lalu
i see... kamu sudah banyak berubah ternyata"""

print(contoh)

#Metode Formated String umtuk menampilkam variabel dalam print dan syntaxnya f sebelum tanda ini "dan didalam ini ada kurung kurawal {}" 
oke = "Farid Hakim"
print(f"Nama saya {oke}")

#Metode %formatting
nama = 'Farid Hakim'
print("nama saya %s" % (nama))

#List dalam python lain sama list dalam bahasa lain karena String maupun Integer bisa digabung dalam satu list
x = [1, 'Dicoding', True, 1.0]

print(x[3])

#Konsep indexing merujuk kepada pengambilan data dalam Python berdasarkan indeksnya. Beberapa cara untuk melakukan indexing sebagai berikut.
x = ["laptop", "monitor", "mouse", "mousepad", "keyboard", "webcam", "microphone"]

print(x[0])
print(x[2])
print(x[-1])
print(x[-3])

#Penggunaan slicing pada List
x = ["laptop", "monitor", "mouse", "mousepad", "keyboard", "webcam", "microphone"]

print(x[0:5:2])
print(x[1:])
print(x[:3])

#Tupple menggunakan ()
x = (5, 'program', 1+3j)
print(x[1])
print(x[0:3])

#set menggunakan {} dan kita harus print pada nama variabelnya bukan print kaya gini "print(x[0])"
x = {1, 2, 7, 2, 3, 13, 3}
print(x)
print(type(x))

#Dictionary, harus ada kata {kunci : isi, kata kunci : isinya}
x = { 'name': 'Perseus Evans', 'age': 20, 'isMarried': False }

print(x ['name'])

#Menambahkan data pada Dictionary
x ['Job'] = "Web Developer" 
print(x)

#Menghapus data pada Dictionary
del x['isMarried']
print(x)

#Mengubah Data pada Dictionary
x ['name'] = "Dicoding"
print(x)