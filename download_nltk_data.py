# download_nltk_data.py
import nltk
import os

# Tentukan direktori target
nltk_data_dir = os.path.join(os.getcwd(), 'nltk_data')
if not os.path.exists(nltk_data_dir):
    os.makedirs(nltk_data_dir)

# Tambahkan direktori ini ke path pencarian NLTK sementara
nltk.data.path.append(nltk_data_dir)

# Unduh paket yang diperlukan
try:
    nltk.data.find('tokenizers/punkt')
    print("Punkt sudah ada.")
except nltk.downloader.DownloadError:
    print("Mengunduh Punkt...")
    nltk.download('punkt', download_dir=nltk_data_dir)
    print("Punkt berhasil diunduh.")

try:
    nltk.data.find('corpora/stopwords')
    print("Stopwords sudah ada.")
except nltk.downloader.DownloadError:
    print("Mengunduh Stopwords...")
    nltk.download('stopwords', download_dir=nltk_data_dir)
    print("Stopwords berhasil diunduh.")

print(f"Data NLTK telah diunduh/diverifikasi di: {nltk_data_dir}")
