# 🌸 Iris Classification Model (Sederhana) 🌸

Selamat datang di proyek **Iris Classification Model Sederhana**!
Proyek ini adalah implementasi dasar dari model _Machine Learning_ untuk melakukan klasifikasi pada **Iris Dataset** yang terkenal. Tujuannya adalah untuk memprediksi spesies bunga Iris (Setosa, Versicolor, atau Virginica) berdasarkan empat fitur utama: panjang sepal, lebar sepal, panjang petal, dan lebar petal.

Sangat cocok untuk pemula yang ingin mempelajari alur dasar _Machine Learning_, mulai dari _preprocessing_ data hingga evaluasi model.

---

## ✨ Fitur Utama Proyek

* **Dataset**: Menggunakan Iris Dataset bawaan dari `sklearn.datasets`.
* **Preprocessing**: Langkah sederhana pembagian data menjadi set pelatihan (_train_) dan pengujian (_test_).
* **Model**: Implementasi menggunakan **[Nama Model Anda, misal: K-Nearest Neighbors (KNN)]**. (Anda bisa mengganti ini dengan model lain seperti Logistic Regression, SVM, Decision Tree, dll.)
* **Evaluasi**: Mengukur performa model menggunakan metrik **Akurasi** dan visualisasi **Confusion Matrix**.
* **Kesederhanaan**: Kode yang mudah dipahami dan diikuti, ideal untuk tujuan pembelajaran.

---

## 📊 Dataset Iris

Dataset Iris terdiri dari 150 sampel data, dengan 50 sampel untuk setiap kelas spesies bunga Iris:
* 🌷 Iris Setosa
* 🌻 Iris Versicolor
* 🌺 Iris Virginica

Setiap sampel memiliki 4 fitur numerik (dalam cm):
1.  Panjang Sepal (_Sepal Length_)
2.  Lebar Sepal (_Sepal Width_)
3.  Panjang Petal (_Petal Length_)
4.  Lebar Petal (_Petal Width_)

---

## 🛠️ Teknologi yang Digunakan

* **Python 3.x**
* **Scikit-learn**: Untuk dataset, model ML, dan metrik evaluasi.
* **NumPy**: Untuk operasi numerik (seringkali sebagai dependensi Scikit-learn).
* **Matplotlib & Seaborn** (Opsional): Untuk visualisasi data atau _confusion matrix_ yang lebih menarik.

---

## 🚀 Langkah-Langkah Implementasi

Alur kerja utama dalam proyek ini adalah sebagai berikut:

1.  **Load Data**:
    * Memuat Iris dataset menggunakan `sklearn.datasets.load_iris()`.
2.  **Pembagian Data**:
    * Membagi dataset menjadi data latih (`X_train`, `y_train`) dan data uji (`X_test`, `y_test`) menggunakan `train_test_split` dari `sklearn.model_selection`.
3.  **Pelatihan Model**:
    * Menginisialisasi model klasifikasi (misalnya, `KNeighborsClassifier`).
    * Melatih model menggunakan data latih (`model.fit(X_train, y_train)`).
    ```python
    # Contoh inisialisasi model KNN
    from sklearn.neighbors import KNeighborsClassifier
    # Ganti n_neighbors sesuai kebutuhan atau hasil tuning
    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(X_train, y_train)
    ```
4.  **Prediksi**:
    * Melakukan prediksi pada data uji (`model.predict(X_test)`).
5.  **Evaluasi Model**:
    * Menghitung **Akurasi** model dengan membandingkan hasil prediksi dan label sebenarnya dari data uji.
    * Membuat dan menampilkan **Confusion Matrix** untuk melihat performa klasifikasi secara detail per kelas.

---

## 📈 Hasil (Contoh)

Setelah menjalankan model, Anda akan mendapatkan hasil performa.

* **Model yang Digunakan**: `[Isi dengan model yang Anda gunakan, misal: K-Nearest Neighbors (KNN) dengan k=3]`
* **Akurasi pada Data Uji**: `[Isi dengan akurasi yang didapatkan, misal: 97% atau 100%]`
* **Confusion Matrix**:
    *(Contoh tampilan confusion matrix sederhana atau deskripsi)*
    ```
    [[10  0  0]  <-- Prediksi Setosa benar
     [ 0  9  1]  <-- 1 Versicolor salah diklasifikasikan sebagai Virginica
     [ 0  0 10]]  <-- Prediksi Virginica benar
    (Gantilah angka ini dengan hasil aktual dari model Anda!)
    ```

> **Catatan**: Hasil dapat bervariasi tergantung pada `random_state` saat pembagian data dan parameter model yang digunakan. Untuk KNN, nilai `k` (jumlah tetangga) dapat memengaruhi hasil.

---

Selamat mencoba dan belajar! Jika ada pertanyaan atau saran, jangan ragu untuk diskusi.
