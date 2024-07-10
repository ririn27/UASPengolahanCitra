# Digital Image Segmentation Using KNN Algorithm dan KMeans Algorithm 

Proyek ini mendemonstrasikan segmentasi citra digital menggunakan algoritma K-Nearest Neighbors (KNN) Dan K- means . Proses segmentasi membagi gambar menjadi wilayah berbeda berdasarkan kesamaan warna, sehingga memungkinkan identifikasi objek atau area berbeda di dalam gambar.

## Ulasan Proyek

Proses segmentasi melibatkan langkah-langkah berikut:
1. Memilih jumlah cluster (k).
2. Menetapkan titik data secara acak ke salah satu k cluster.
3. Menghitung pusat cluster.
4. Menghitung jarak setiap titik data dari pusat cluster.
5. Menugaskan kembali titik data ke cluster terdekat berdasarkan jarak.
6. Menghitung ulang pusat cluster.
7. Mengulangi langkah 4, 5, dan 6 hingga titik data tidak lagi mengubah cluster atau mencapai jumlah iterasi yang ditetapkan.

   ## Persyaratan 

Pastikan Anda telah menginstal perpustakaan berikut:

- numpy
- matplotlib
- scikit-belajar
- opencv-python

Anda dapat menginstal perpustakaan ini menggunakan perintah berikut:

{``` pesta
pip instal numpy matplotlib scikit-belajar opencv-python }

## pengunaan

1. Kloning repositori atau unduh file kode.
2. Tempatkan gambar yang ingin Anda segmenkan di direktori proyek.
3. Perbarui jalur gambar dalam kode.
4. Jalankan skrip untuk melakukan segmentasi gambar.


Penjelasan
- Membaca dan Mempersiapkan Gambar: Gambar dibaca menggunakan OpenCV dan diubah ke format RGB. Gambar tersebut kemudian dibentuk kembali menjadi array 2D di mana setiap piksel merupakan titik data.
  
- Inisialisasi Cluster: Model KNN dibuat dengan jumlah cluster yang diatur ke k. Pusat cluster awal dipilih secara acak.
  
- Pengelompokan Iteratif: Algoritme secara berulang menghitung jarak setiap titik data ke pusat cluster, menetapkan kembali titik data ke cluster terdekat, dan menghitung ulang pusat cluster hingga konvergensi atau jumlah iterasi maksimum tercapai.

- Menampilkan Gambar Tersegmentasi: Gambar tersegmentasi yang dihasilkan ditampilkan menggunakan Matplotlib.

# Kustomisasi

- Jumlah Cluster: Ubah nilai k untuk mengatur jumlah cluster.

- Iterasi Maks: Sesuaikan variabel max_iterations untuk mengubah jumlah iterasi maksimum untuk konvergensi.

- Jalur Gambar: Ganti 'image_path.jpg' dengan jalur ke file gambar Anda.
  
# Kesimpulan

Proyek ini mendemonstrasikan metode segmentasi gambar yang sederhana namun efektif menggunakan algoritma KNN. Proses segmentasi dapat disesuaikan dengan menyesuaikan jumlah cluster dan parameter lainnya. Untuk teknik segmentasi gambar tingkat lanjut, pertimbangkan untuk menjelajahi algoritme seperti K-Means atau metode pengelompokan lainnya.

# Lisensi

Proyek ini dilisensikan di bawah Lisensi MIT. Lihat file LISENSI untuk detailnya.
## Gambar Asli

![image](https://github.com/ririn27/UASPengolahanCitra/assets/115934294/7fca5e6e-2a7f-4ea9-bda5-e658cfd82d1e)


![OriginalImage](https://github.com/ririn27/UASPengolahanCitra/assets/115934294/7f8b92fa-a04a-47fa-af6b-ec4a8d5c4243)


# Hasil 

## Segmented Image

![Figure_1](https://github.com/ririn27/UASPengolahanCitra/assets/115934294/c6c51146-9c94-4cbf-b03d-ee721e128f99)


![Segmented Image](https://github.com/ririn27/UASPengolahanCitra/assets/115934294/75f7ac2a-5fab-4b5b-96c5-e3a2f35dd695)

## Cluster Image

![Cluster Image_1](https://github.com/ririn27/UASPengolahanCitra/assets/115934294/9a8a2197-b2d3-4dc6-9439-e4c49613a399)


![Cluster Image_2](https://github.com/ririn27/UASPengolahanCitra/assets/115934294/39950f9c-2666-4651-830e-7649c572f70e)


![Cluster Image_3](https://github.com/ririn27/UASPengolahanCitra/assets/115934294/fad753fe-feb8-4310-b35b-3a57d7e7a4d0)


![Cluster Image_4](https://github.com/ririn27/UASPengolahanCitra/assets/115934294/694ade21-d51b-4d81-b1f9-3d3e16767c16)


![Cluster Image_5](https://github.com/ririn27/UASPengolahanCitra/assets/115934294/06e204b0-8ef2-4a16-9c3e-284450626830)


![Cluster Image_6](https://github.com/ririn27/UASPengolahanCitra/assets/115934294/78084448-2eee-43fa-9e02-aba76f651a15)


![Cluster Image_7](https://github.com/ririn27/UASPengolahanCitra/assets/115934294/6f6170ba-02e6-40a3-82a6-cb5ec468c6b2)



Ucapan Terima Kasih

- OpenCV
  
- scikit-learn
  
- NumPy
  
- Matplotlib

by : ririn nofrima
