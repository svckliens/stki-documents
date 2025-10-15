# ============================================================
# Mata Kuliah : Sistem Temu Kembali Informasi
# Topik       : Document Preprocessing
# Dosen       : Tim STKI
# Deskripsi   : Latihan Parsing, Tokenisasi, Stopword Removal, dan Stemming
# ============================================================

import re
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

# ============================================================
# 1. INPUT TEKS (bisa kamu ubah sesuai kebutuhan)
# ============================================================
text = """
yang menjadi salah satu syarat untuk bisa ujian kompre adalah sertifikat TOEIC,
sehingga jika belum lulus toeic maka tidak bisa melakukan ujian kompre. Saya rasa ini sangat menghambat
teman-teman yang memang lemah dibidang bahasa inggris (atau yang kurang beruntung dalam ujian toeic-nya),
sehingga mereka tidak bisa fokus untuk ujian kompre-nya.
"""

# ============================================================
# 2. PARSING
#    Menghapus karakter non-huruf dan ubah ke huruf kecil
# ============================================================
parsed_text = re.sub(r'[^a-zA-Z\s]', '', text)  # hapus karakter selain huruf dan spasi
parsed_text = parsed_text.lower()  # ubah ke huruf kecil
print("=== HASIL PARSING ===")
print(parsed_text)
print()

# ============================================================
# 3. TOKENISASI
#    Memecah teks menjadi kata-kata
# ============================================================
tokens = parsed_text.split()
print("=== HASIL TOKENISASI ===")
print(tokens)
print()

# ============================================================
# 4. STOPWORD REMOVAL
#    Menghapus kata-kata tidak penting (umum)
# ============================================================
factory = StopWordRemoverFactory()
stopword = factory.create_stop_word_remover()
clean_text = stopword.remove(parsed_text)
filtered_tokens = clean_text.split()
print("=== HASIL STOPWORD REMOVAL ===")
print(filtered_tokens)
print()

# ============================================================
# 5. STEMMING
#    Mengubah kata menjadi bentuk dasarnya
# ============================================================
stem_factory = StemmerFactory()
stemmer = stem_factory.create_stemmer()
stemmed_text = stemmer.stem(clean_text)
stemmed_tokens = stemmed_text.split()
print("=== HASIL STEMMING ===")
print(stemmed_tokens)
print()

# ============================================================
# 6. SIMPAN HASIL KE FILE
# ============================================================
with open("hasil_preprocessing.txt", "w", encoding="utf-8") as f:
    f.write("=== HASIL PARSING ===\n")
    f.write(parsed_text + "\n\n")

    f.write("=== HASIL TOKENISASI ===\n")
    f.write(str(tokens) + "\n\n")

    f.write("=== HASIL STOPWORD REMOVAL ===\n")
    f.write(str(filtered_tokens) + "\n\n")

    f.write("=== HASIL STEMMING ===\n")
    f.write(str(stemmed_tokens) + "\n")

print("✅ Semua hasil telah disimpan ke file 'hasil_preprocessing.txt'")
