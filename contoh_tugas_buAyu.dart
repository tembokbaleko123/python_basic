void main() {
  // Inisialisasi list nilai
  List<int> listIncrement = List<int>.generate(70, (index) => index);

  // Temukan nilai tertinggi dan nilai terendah
  int nilaiTertinggi = listIncrement.reduce((a, b) => a > b ? a : b);
  int nilaiTerendah = listIncrement.reduce((a, b) => a < b ? a : b);

  // Tampilkan hasil
  print("\nNilai tertinggi Mahasiswa: $nilaiTertinggi");
  print("Nilai terendah Mahasiswa: $nilaiTerendah");
}
