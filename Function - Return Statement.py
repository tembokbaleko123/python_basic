def get_sum(a,b): # fungsi yang akan mengembalikan total dari 2 angka
  result = a + b
  return result # mengembalikan hasil penjumlahan menggunakan return

n1 = get_sum(10,20)
print("hasil penjumlahan dari 10 dan 20 adalah",n1)

#return statement juga bisa mengembalikan multiple result dalam bentuk sebuah tuple seperti contoh sebelumnya.

def get_root(a,b,c):
  r1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
  r2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
  return r1,r2

result1, result2 = get_root(a=1,c=-8,b=2)
print('Hasil akar-akarnya adalah', result1, 'atau', result2)
