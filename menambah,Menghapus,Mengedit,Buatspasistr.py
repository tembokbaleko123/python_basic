#rstrip() berfungsi untuk menghapus spasi kososng kanan
print("Dicoding          ".rstrip())

#Kebalikan dari rstrip(), lstrip() bertugas untuk menghapus whitespace pada sebelah kiri atau awal string. 
print("           Dicoding".lstrip())

#Metode ini bertugas untuk menghapus whitespace pada bagian awal dan akhir string.
print("         Dicoding          ".strip())

#Jika ingin menghilangkan karakter selain whitespace .strip()
kata = 'CodeCodeDicodingCodeCode'
print(kata.strip("Code"))

#Metode startswith() bertujuan untuk menemukan suatu kata pada awal string. Metode ini mengembalikan nilai True.
print('Dicoding Indonesia'.startswith('Dicoding'))

#Metode endswith() bertujuan untuk menemukan suatu kata pada akhir string. Metode ini juga mengembalikan nilai True jika menemukannya, sedangkan jika tidak menemukan kata yang diinginkan, nilai False dikembalikan.
print('Dicoding Indonesia'.endswith('Dicoding'))

#.join untuk menambahkan string
print(' '.join(['Dicoding','Indonesia', '!']))

print('123'.join(['Dicoding','Indonesia'])) #bisa juga untuk menngabungkan delimeter lain


#split() untuk memisahkan string berdasarkan demlimeter
print('Dicoding Indonesia !'.split())

print('''Halo,     
aku ikan,
aku suka sekali menyelam
aku tinggal di perairan.
Badanku licin dan renangku cepat.
Senang berkenalan denganmu.'''.split('\n')) #Bisa juga menggunakan delimiter newline (\n) untuk memisahkan setiap baris pada string multiline.

#.replace() berfungsi untuk menggantikan/mengubah string ke string yang lain
string = "Ayo belajar Coding di Dicoding"
print(string.replace("Coding", "Pemrograman"))

#isupper() untuk mengecek apakah semuanya sudah kapital atau tidak. Tipe data boolean
kata = 'DICODING'
print(kata.isupper())

#Kebalikannya, .islower() akan mengembalikan nilai True jika semua huruf dalam string adalah huruf kecil (lowercase). 
kata = 'dicoding'
print(kata.islower())

#.isalpha Nilai True jika semua karakter dalam string adalah huruf alfabet.
kata = 'dicoding'
print(kata.isalpha())

#.isalnum nilai True jika karakter dalam string adalah alfanumerik, yaitu hanya huruf atau hanya angka atau berisi keduanya.
kata = 'dicoding123'
print(kata.isalnum())

#.isdecimal nilai True jika karakter dalam string berisi hanya angka/numerik.
print('123'.isdecimal())

#.isspace() nilai True jika string hanya berisi whitespace, seperti spasi, tab, newline, atau karakter whitespace lainnya.
print('         '.isspace())

#.istittle bernilai jika huruf pertamanya kapital semua
print('Dicoding Indonesia'.istitle())

#.zfill Metode zfill() bertujuan untuk menambahkan nilai nol (0) di depan sebuah string dengan panjang tertentu. 
teks = 'Code'
tambah_number = teks.zfill(7)
print(tambah_number)

#.rjust(jumlahSpasi) untuk membuat teks rata kanan
print('Dicoding'.rjust(20))

print('Dicoding'.rjust(20, '!')) #Bisa menambahkan teks lain, tidak hanya whitespace.

#ljust(jumlahSpasi)
print('Dicoding'.ljust(20))

#.center() Metode center() menjadikan teks rata tengah. Metode ini akan menambahkan whitespace di sebelah kiri dan kanan secara default.
print('Dicoding'.center(10, '-'))

#Escape Character
print("Halo!\nKapan terakhir kali kita bertemu?\nKita bertemu hari Jum\'at yang lalu.")

#Raw String berfungsi umtuk menampilkan syntax apa yang digunakan pada string tsb dengan menambahkan r sebelum pembuka string atau sebelum tanda petik
print(r'Dicoding\tIndonesia')