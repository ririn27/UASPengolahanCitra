# UASPengolahanCitra

# Digital Image Segmentation Using KNN Algorithm

This project demonstrates digital image segmentation using the K-Nearest Neighbors (KNN) algorithm. The segmentation process divides an image into different regions based on color similarities, enabling the identification of distinct objects or areas within the image.

## Project Overview

The segmentation process involves the following steps:
1. Selecting the number of clusters (k).
2. Assigning data points randomly to one of the k clusters.
3. Calculating the cluster centers.
4. Calculating the distance of each data point from the cluster centers.
5. Reassigning data points to the nearest cluster based on distance.
6. Recalculating the cluster centers.
7. Repeating steps 4, 5, and 6 until data points no longer change clusters or a set number of iterations is reached.

## Requirements

Ensure you have the following libraries installed:

- numpy
- matplotlib
- scikit-learn
- opencv-python

You can install these libraries using the following command:

```bash
pip install numpy matplotlib scikit-learn opencv-python


## Requirements

1. Kloning repositori atau unduh file kode.
2. Tempatkan gambar yang ingin Anda segmenkan di direktori proyek.
3. Perbarui jalur gambar dalam kode.
4. Jalankan skrip untuk melakukan segmentasi gambar.

## Kode


import numpy as np
import matplotlib.pyplot as plt
import cv2
from sklearn.neighbors import KNeighborsClassifier

# Membaca gambar
image = cv2.imread('image.jpg')  # Ganti 'image.jpg dengan path gambar Anda
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Mengubah warna gambar dari BGR ke RGB

# Mengubah gambar menjadi array 2D
pixels = image.reshape(-1, 3)  # Mengubah gambar menjadi bentuk (jumlah piksel, 3) untuk RGB

# Menentukan jumlah cluster
k = 3  # Jumlah cluster yang ingin dicari

# Membuat model KNN
knn = KNeighborsClassifier(n_neighbors=1)

# Menetapkan titik data secara acak ke salah satu dari k cluster
np.random.seed(0)
random_indices = np.random.choice(len(pixels), size=k, replace=False)
centers = pixels[random_indices]

# Menginisialisasi variabel
prev_centers = np.zeros(centers.shape)
max_iterations = 10  # Jumlah iterasi maksimum
iteration = 0
converged = False

while not converged and iteration < max_iterations:
    # Menghitung jarak titik data dari pusat cluster
    distances = np.linalg.norm(pixels[:, np.newaxis] - centers, axis=2)
    
    # Menetapkan titik data ke cluster terdekat
    labels = np.argmin(distances, axis=1)
    
    # Menghitung pusat cluster baru
    new_centers = np.array([pixels[labels == i].mean(axis=0) for i in range(k)])
    
    # Memeriksa konvergensi
    if np.all(centers == new_centers):
        converged = True
    
    centers = new_centers
    iteration += 1

# Mengubah label menjadi gambar segmentasi
segmentation_image = np.reshape(labels, image.shape[:2])

# Menampilkan gambar segmentasi
plt.imshow(segmentation_image, cmap='viridis')
plt.title('Segmentasi Gambar')
plt.show()



## Penjelasan

1. Membaca dan Mempersiapkan Gambar: Gambar dibaca menggunakan OpenCV dan dikonversi ke format RGB. Gambar tersebut kemudian dibentuk kembali menjadi array 2D di mana setiap piksel adalah titik data.
2. Inisialisasi Cluster: Model KNN dibuat dengan jumlah cluster yang diatur ke k. Pusat cluster awal dipilih secara acak.
3. Pengelompokan Iteratif: Algoritme secara berulang menghitung jarak setiap titik data ke pusat cluster, menetapkan kembali titik data ke cluster terdekat, dan menghitung ulang pusat cluster hingga konvergensi atau jumlah iterasi maksimum tercapai.
4. Menampilkan Gambar Tersegmentasi: Gambar tersegmentasi yang dihasilkan ditampilkan menggunakan Matplotlib.

## Kustomisasi

1. Jumlah Cluster: Ubah nilai k untuk mengatur jumlah cluster.
2. Iterasi Maks: Sesuaikan variabel max_iterations untuk mengubah jumlah iterasi maksimum untuk konvergensi.
3. Jalur Gambar: Ganti 'image_path.jpg' dengan jalur ke file gambar Anda.


## Kesimpulan

Proyek ini mendemonstrasikan metode sederhana namun efektif untuk segmentasi gambar menggunakan algoritma KNN. Proses segmentasi dapat disesuaikan dengan menyesuaikan jumlah cluster dan parameter lainnya. Untuk teknik segmentasi gambar tingkat lanjut, pertimbangkan untuk menjelajahi algoritme seperti K-Means atau metode pengelompokan lainnya.


Lisensi
Proyek ini dilisensikan di bawah Lisensi MIT. Lihat file LISENSI untuk detailnya.

a. OpenCV
b. scikit-learn
c. NumPy
d. Matplotlib


Ucapan Terima Kasih
