from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

"""
Code ini bertujuan untuk melatih pemahaman awal atau bisa disebut "FUNDAMENTAL DASAR" machine learning, menggunakan 
dataset iris yang memiliki 3 target bunga dengan persyaratan tertentu. Dalam dataset terdapat 2 feature yang mudah kita
pisahkan ke dalam 2 variabel yaitu X & y.
"""

# Load dataset iris
df = load_iris()
X = df.data  # Fitur
y = df.target  # Target

# Pisahkan data latih dan data testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Memilih dan menginstall model
model = KNeighborsClassifier(n_neighbors=3)

# Latih model dengan data latih
model.fit(X_train, y_train)

# Membuat prediksi dari data uji
y_pred = model.predict(X_test)

# Evaluasi model
accuracy = accuracy_score(y_test, y_pred)
print(f"Akurasi model KNN pada data uji: {accuracy:.4f}")

# Mnecoba dengan data baru
bunga_baru = [[5.0, 10.0, 11.0, 12.0]]
predic_spesies_index = model.predict(bunga_baru)
predic_spesies_nama = df.target_names[predic_spesies_index]
print(f"Prediksi spesies untuk bunga baru dengan fitur {bunga_baru}: {predic_spesies_nama}")
