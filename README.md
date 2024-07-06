# Digital Image Segmentation Using KNN Algorithm

Proyek ini mendemonstrasikan segmentasi citra digital menggunakan algoritma K-Nearest Neighbors (KNN). Proses segmentasi membagi gambar menjadi wilayah berbeda berdasarkan kesamaan warna, sehingga memungkinkan identifikasi objek atau area berbeda di dalam gambar.

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

## Hasil 

![Figure_1](https://github.com/ririn27/UASPengolahanCitra/assets/115934294/c6c51146-9c94-4cbf-b03d-ee721e128f99)


Ucapan Terima Kasih

by : ririn nofrima
