#Exercise!
#Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

for image in picture: # Dia akan mengambil row (baris) dulu
    for pixel in image: 
        if pixel == 0:
            print(' ', end='')
        elif pixel == 1:
            print('*', end='')
    print(' ')

# Lebih mudah menggunakan for lalu for (contoh diatas)
# for image in picture:
#     while image == 0:
#         print(' ', end = '')
#     else:
#         print('*', end = '')
#     print(' ')