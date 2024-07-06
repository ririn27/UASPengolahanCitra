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
