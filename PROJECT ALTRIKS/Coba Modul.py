"""
====================================================
  FILE DEMO - PENGGUNAAN MODULE nta123
  Nama File  : demo_matriks.py
  Deskripsi  : Mendemonstrasikan seluruh fungsi
               yang tersedia di module nta123.py
====================================================
"""

import nta123   # <-- import module buatan sendiri

# ── Definisi matriks contoh ─────────────────────
A = [
    [1, 2, 3],
    [0, 1, 4],
    [5, 6, 0]
]

B = [
    [2, 0, 1],
    [3, 1, 0],
    [0, 2, 4]
]

print("=" * 50)
print("   DEMO MODULE nta123 - ALJABAR MATRIKS 3x3")
print("=" * 50)

# 1. Tampilkan matriks awal
nta123.tampilkan(A, "Matriks A")
nta123.tampilkan(B, "Matriks B")

# 2. Penjumlahan
print("\n── 1. PENJUMLAHAN A + B ──")
C = nta123.penjumlahan(A, B)
nta123.tampilkan(C, "Hasil A + B")

# 3. Perkalian
print("\n── 2. PERKALIAN A x B ──")
D = nta123.perkalian(A, B)
nta123.tampilkan(D, "Hasil A x B")

# 4. Transpose
print("\n── 3. TRANSPOSE A ──")
T = nta123.transpose(A)
nta123.tampilkan(T, "Transpose A")

# 5. Determinan
print("\n── 4. DETERMINAN A ──")
det_A = nta123.determinan(A)
print(f"  det(A) = {det_A}")

# 6. Invers
print("\n── 5. INVERS A ──")
inv_A = nta123.invers(A)
nta123.tampilkan(inv_A, "Invers A")

# Verifikasi: A x A^-1 harus = Matriks Identitas
print("\n── VERIFIKASI: A x A⁻¹ (seharusnya = Matriks Identitas) ──")
I = nta123.perkalian(A, inv_A)
nta123.tampilkan(I, "A x A⁻¹")

# 7. Contoh error handling: matriks singular
print("\n── BONUS: Contoh Matriks Singular (det = 0) ──")
S = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
nta123.tampilkan(S, "Matriks Singular S")
det_S = nta123.determinan(S)
print(f"  det(S) = {det_S}")
try:
    nta123.invers(S)
except ValueError as e:
    print(f"  Error: {e}")

print("\n" + "=" * 50)
print("   SELESAI - Semua fungsi berjalan dengan baik!")
print("=" * 50)