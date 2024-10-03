# Tentukan rentang nilai
nilai_terendah = 0
nilai_tertinggi = 100 

# Buat list untuk menyimpan nilai-nilai mahasiswa
nilai_mahasiswa = []

# Pelemparan dart sebanyak 70 kali
for _ in range(70):
    # Simulasikan pelemparan dart
    nilai = int(input("Masukkan nilai mahasiswa: "))
    # Simpan nilai
    nilai_mahasiswa.append(nilai)

# Cari nilai tertinggi dan terendah
nilai_tertinggi = max(nilai_mahasiswa)
nilai_terendah = min(nilai_mahasiswa)

# Print nilai tertinggi dan terendah
print("Nilai tertinggi:", nilai_tertinggi)
print("Nilai terendah:", nilai_terendah)