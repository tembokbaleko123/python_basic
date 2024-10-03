kendaraan = ['motor', 'mobil', 'helikopter', 'pesawat'] #Pengurutan sesuai abjad yang mulai dari a, b, c, d, ...... (default)
kendaraan.sort()

print(kendaraan)


#Mengurutkan secara menurun
kendaraan = ['motor', 'mobil', 'helikopter', 'pesawat']
kendaraan.sort(reverse=True)

print(kendaraan)

#Metode sort tidak dapat mengurutkan list yang memiliki angka dan string sekaligus di dalamnya.

urutan = ['Dicoding', 1, 2, 'Indonesia', 3]
urutan.sort()

print(urutan)


#Metode sort menggunakan urutan ASCII sehingga nilai huruf kapital (uppercase) akan lebih dahulu dibandingkan huruf kecil (lowercase).
kendaraan = ['motor', 'mobil', 'helikopter', 'Pesawat']
kendaraan.sort()

print(kendaraan)