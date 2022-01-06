# Importing Library yang Digunakan
import math
import numpy as np
from PIL import Image

# Mengakses data gambar dan mengubah gambar tersebut dalam bentuk array
load_image = Image.open('input.jpg')
image_array = np.array(load_image)
img_width = len(image_array[0])
img_height = len(image_array)

print("Gambar memiliki ukuran : %s x %s pixel" %(img_height, img_width))

# Fungsi untuk memilih metode blurring yang diinginkan
def menuSelection():
    global selection
    print("Pilih Metode Blur yang Diinginkan : ")
    print("1. Average Blur")
    print("2. Gaussian Blur")
    selection = int(input("Pilihan : "))

# Fungsi untuk men-generate kernel gaussian dengan menggunakan distribusi normal dengan variable radius sebagai ukuran matriks dan sigma sebagai standar deviasi
def generateGaussianKernel(radius, sigma):
    global sum
    gaussian_kernel = [[0 for i in range(2*radius + 1)] for i in range(2*radius + 1)] # Membuat matriks berukuran 2*radius + 1 x 2*radius + 1
    sum = 0 
    # Looping sepanjang matriks 
    for i in range(2*radius + 1): 
        for j in range(2*radius + 1):
            gaussian_kernel[i][j] = (1/(2*math.pi*sigma**2))*(math.exp(-0.5*(((i - radius)**2 + (j - radius)**2)/(2*sigma**2)))) # Mengubah nilai matriks dengan hasil distribusi normal
            sum += gaussian_kernel[i][j] # Menghitung total dari nilai matriks yang akan digunakan untuk mencari nilai rasio
    print("Gaussian Kernel : ")
    # Mengubah nilai matriks dengan nilai rasio
    for i in range(2*radius + 1):
        for j in range(2*radius + 1):
            gaussian_kernel[i][j] /= sum
            print("%.10f" %(gaussian_kernel[i][j]), end=" ")
        print()
    return gaussian_kernel

# Fungsi Average Blur
def average_blur():
    # Input
    blur_factor = int(input("Masukkan Blur Faktor (semakin besar semakin lama prosesnya dan semakin blur, rekomendasi : 3) : ")) # Blur Factor = ukuran kernel gaussian blur
    blurred = image_array # Menyimpan array gambar pada array baru bernama blurred
    print("Proses Blurring Image sedang berlangsung, silahkan tunggu beberapa saat...")
    # Looping sepanjang matriks image_array
    for i in range(img_height):
        for j in range(img_width):
            r, g, b = 0, 0, 0 # Dummy variable berupa r,g, dan b
            # Looping sebesar ukuran matriks average sesuai dengan ukuran blur yang kita inginkan 
            for k in range(-blur_factor,blur_factor+1):
                for l in range(-blur_factor,blur_factor+1):
                    if (i+k >= 0 and i+k <= img_height-1) and (j+l >= 0 and j+l <= img_width-1): # Fungsi untuk mengecek apakah pixel yang diperhatikan berada diluar ukuran matriks gambar
                        r += image_array[i+k][j+l][0] / (2*blur_factor+1)**2 # Menambahkan nilai r dengan perkalian antara rata-rata dari elemen matriks average dengan data r pada pixel
                        g += image_array[i+k][j+l][1] / (2*blur_factor+1)**2 # Menambahkan nilai g dengan perkalian antara rata-rata dari elemen matriks average dengan data g pada pixel
                        b += image_array[i+k][j+l][2] / (2*blur_factor+1)**2 # Menambahkan nilai b dengan perkalian antara rata-rata dari elemen matriks average dengan data b pada pixel
            blurred[i][j] = [r, g, b] # Menggubah nilai pada matriks gambar blurred dengan hasil r, g, b yang telah didapat dengan gaussian kernel
    # Menyimpan gambar hasil blurring dan menampilkan gambar tersebut
    output = Image.fromarray(blurred)
    output.save("output (average blur).jpg")
    output.show()
    print("Proses Selesai")

# Fungsi Gaussian Blur
def gaussian_blur():
    # Input
    blur_factor = int(input("Masukkan Blur Faktor (semakin besar semakin lama prosesnya dan semakin blur, rekomendasi : 3) : ")) # Blur Factor = ukuran kernel gaussian blur
    sigma = float(input("Masukkan Besar Standar Deviasi (semakin besar, gambar semakin blur) : ")) # Masukkan Standar Deviasi
    gaussian_kernel = generateGaussianKernel(blur_factor, sigma) # Memanggil fungsi untuk men-generate gaussian kernel
    blurred = image_array # Menyimpan array gambar pada array baru bernama blurred
    print("Proses Blurring Image sedang berlangsung, silahkan tunggu beberapa saat...")
    # Looping sepanjang matriks image_array
    for i in range(img_height):
        for j in range(img_width):
            r, g, b = 0, 0, 0 # Dummy variable berupa r,g, dan b
            # Looping sebesar ukuran matriks gaussian kernel 
            for k in range(-blur_factor,blur_factor+1):
                for l in range(-blur_factor,blur_factor+1):
                    if (i+k >= 0 and i+k <= img_height-1) and (j+l >= 0 and j+l <= img_width-1): # Fungsi untuk mengecek apakah pixel yang diperhatikan berada diluar ukuran matriks gambar
                        r += image_array[i+k][j+l][0] * gaussian_kernel[k][l] # Menambahkan nilai r dengan perkalian antara gaussian kernel dengan data r pada pixel
                        g += image_array[i+k][j+l][1] * gaussian_kernel[k][l] # Menambahkan nilai g dengan perkalian antara gaussian kernel dengan data g pada pixel
                        b += image_array[i+k][j+l][2] * gaussian_kernel[k][l] # Menambahkan nilai b dengan perkalian antara gaussian kernel dengan data b pada pixel
            blurred[i][j] = [r, g, b] # Menggubah nilai pada matriks gambar blurred dengan hasil r, g, b yang telah didapat dengan gaussian kernel
    # Menyimpan gambar hasil blurring dan menampilkan gambar tersebut
    output = Image.fromarray(blurred)
    output.save("output (gaussian blur).jpg")
    output.show()
    print("Proses Selesai")

# Menampilkan pilihan metode
menuSelection()
if selection == 1:
    average_blur()
elif selection == 2:
    gaussian_blur()
else: 
    menuSelection()