"""
FUNGSI YANG TERSEDIA:
  - tampilkan(M)             : Menampilkan matriks ke layar
  - penjumlahan(A, B)        : Penjumlahan dua matriks 3x3
  - perkalian(A, B)          : Perkalian dua matriks 3x3
  - transpose(M)             : Transpose matriks 3x3
  - determinan(M)            : Determinan matriks 3x3 (metode Sarrus)
  - invers(M)                : Invers matriks 3x3 (metode adjoin)

CONTOH PENGGUNAAN:
  import nta123
  A = [[1,2,3],[4,5,6],[7,8,9]]
  nta123.tampilkan(A)
  hasil = nta123.perkalian(A, A)
"""


# ──────────────────────────────────────────────
#  HELPER: validasi bahwa input adalah matriks 3x3
# ──────────────────────────────────────────────
def _validasi_3x3(M, nama="Matriks"):
    """Memastikan M adalah list 3x3 yang valid."""
    if not isinstance(M, list) or len(M) != 3:
        raise ValueError(f"{nama} harus memiliki tepat 3 baris.")
    for i, baris in enumerate(M):
        if not isinstance(baris, list) or len(baris) != 3:
            raise ValueError(f"Baris ke-{i+1} pada {nama} harus memiliki tepat 3 kolom.")
        for j, val in enumerate(baris):
            if not isinstance(val, (int, float)):
                raise ValueError(
                    f"Elemen [{i}][{j}] pada {nama} harus berupa angka, bukan '{val}'."
                )


# ──────────────────────────────────────────────
#  1. TAMPILKAN
# ──────────────────────────────────────────────
def tampilkan(M, label=None):
    """
    Menampilkan matriks 3x3 dalam format grid rapi.

    Parameter:
        M     (list[list]) : Matriks 3x3 yang akan ditampilkan.
        label (str)        : Judul opsional yang dicetak di atas matriks.

    Contoh:
        import nta123
        A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        nta123.tampilkan(A, "Matriks A")
    """
    _validasi_3x3(M, "M")
    if label:
        print(f"\n{label}:")
    print("┌                       ┐")
    for baris in M:
        isi = "  ".join(f"{v:6.2f}" for v in baris)
        print(f"│  {isi}  │")
    print("└                       ┘")


# ──────────────────────────────────────────────
#  2. PENJUMLAHAN
# ──────────────────────────────────────────────
def penjumlahan(A, B):
    """
    Menghitung penjumlahan dua matriks 3x3.
    Rumus: C[i][j] = A[i][j] + B[i][j]

    Parameter:
        A (list[list]) : Matriks pertama 3x3.
        B (list[list]) : Matriks kedua 3x3.

    Return:
        list[list] : Matriks hasil penjumlahan 3x3.

    Contoh:
        import nta123
        A = [[1,0,0],[0,1,0],[0,0,1]]
        B = [[2,3,4],[5,6,7],[8,9,10]]
        C = nta123.penjumlahan(A, B)
    """
    _validasi_3x3(A, "A")
    _validasi_3x3(B, "B")

    hasil = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]

    for i in range(3):
        for j in range(3):
            hasil[i][j] = A[i][j] + B[i][j]

    return hasil


# ──────────────────────────────────────────────
#  3. PERKALIAN
# ──────────────────────────────────────────────
def perkalian(A, B):
    """
    Menghitung perkalian dua matriks 3x3.
    Rumus: C[i][j] = Σ A[i][k] * B[k][j]  untuk k = 0,1,2

    Parameter:
        A (list[list]) : Matriks pertama 3x3.
        B (list[list]) : Matriks kedua 3x3.

    Return:
        list[list] : Matriks hasil perkalian 3x3.

    Contoh:
        import nta123
        A = [[1,2,3],[4,5,6],[7,8,9]]
        B = [[9,8,7],[6,5,4],[3,2,1]]
        C = nta123.perkalian(A, B)
    """
    _validasi_3x3(A, "A")
    _validasi_3x3(B, "B")

    hasil = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]

    for i in range(3):
        for j in range(3):
            jumlah = 0
            for k in range(3):
                jumlah += A[i][k] * B[k][j]
            hasil[i][j] = jumlah

    return hasil


# ──────────────────────────────────────────────
#  4. TRANSPOSE
# ──────────────────────────────────────────────
def transpose(M):
    """
    Menghitung transpose matriks 3x3.
    Rumus: T[i][j] = M[j][i]  (baris dan kolom dipertukarkan)

    Parameter:
        M (list[list]) : Matriks 3x3 yang akan di-transpose.

    Return:
        list[list] : Matriks transpose 3x3.

    Contoh:
        import nta123
        A = [[1,2,3],[4,5,6],[7,8,9]]
        T = nta123.transpose(A)
        # T = [[1,4,7],[2,5,8],[3,6,9]]
    """
    _validasi_3x3(M, "M")

    hasil = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]

    for i in range(3):
        for j in range(3):
            hasil[i][j] = M[j][i]

    return hasil


# ──────────────────────────────────────────────
#  5. DETERMINAN  (metode Sarrus)
# ──────────────────────────────────────────────
def determinan(M):
    """
    Menghitung determinan matriks 3x3 menggunakan Metode Sarrus.

    Metode Sarrus:
      det(M) = (M[0][0]*M[1][1]*M[2][2])
             + (M[0][1]*M[1][2]*M[2][0])
             + (M[0][2]*M[1][0]*M[2][1])
             - (M[0][2]*M[1][1]*M[2][0])
             - (M[0][0]*M[1][2]*M[2][1])
             - (M[0][1]*M[1][0]*M[2][2])

    Parameter:
        M (list[list]) : Matriks 3x3.

    Return:
        float : Nilai determinan matriks.

    Contoh:
        import nta123
        A = [[1,2,3],[4,5,6],[7,8,10]]
        d = nta123.determinan(A)   # -3.0
    """
    _validasi_3x3(M, "M")

    diagonal_utama = (M[0][0] * M[1][1] * M[2][2]
                    + M[0][1] * M[1][2] * M[2][0]
                    + M[0][2] * M[1][0] * M[2][1])

    diagonal_sekunder = (M[0][2] * M[1][1] * M[2][0]
                       + M[0][0] * M[1][2] * M[2][1]
                       + M[0][1] * M[1][0] * M[2][2])

    return diagonal_utama - diagonal_sekunder


# ──────────────────────────────────────────────
#  HELPER: Kofaktor 2x2 (dipakai oleh invers)
# ──────────────────────────────────────────────
def _minor_2x2(M, baris_hapus, kolom_hapus):
    """Mengembalikan determinan minor 2x2 setelah menghapus baris & kolom tertentu."""
    sub = []
    for i in range(3):
        if i == baris_hapus:
            continue
        baris_sub = []
        for j in range(3):
            if j == kolom_hapus:
                continue
            baris_sub.append(M[i][j])
        sub.append(baris_sub)
    # Determinan 2x2: ad - bc
    return sub[0][0] * sub[1][1] - sub[0][1] * sub[1][0]


# ──────────────────────────────────────────────
#  6. INVERS  (metode Adjoin / Adjugate)
# ──────────────────────────────────────────────
def invers(M):
    """
    Menghitung invers matriks 3x3 menggunakan Metode Adjoin.

    Langkah:
      1. Hitung determinan. Jika det = 0, matriks singular (tidak punya invers).
      2. Hitung matriks kofaktor C[i][j] = (-1)^(i+j) * minor(i,j)
      3. Transpose kofaktor → matriks adjoin
      4. Invers = adjoin / determinan

    Parameter:
        M (list[list]) : Matriks 3x3.

    Return:
        list[list] : Matriks invers 3x3.

    Raises:
        ValueError : Jika determinan = 0 (matriks singular).

    Contoh:
        import nta123
        A = [[1,2,3],[0,1,4],[5,6,0]]
        inv = nta123.invers(A)
    """
    _validasi_3x3(M, "M")

    det = determinan(M)
    if det == 0:
        raise ValueError(
            "Matriks singular (determinan = 0): invers tidak ada."
        )

    # Hitung matriks kofaktor
    kofaktor = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]

    for i in range(3):
        for j in range(3):
            tanda = (-1) ** (i + j)
            kofaktor[i][j] = tanda * _minor_2x2(M, i, j)

    # Transpose kofaktor = adjoin
    adjoin = transpose(kofaktor)

    # Invers = adjoin / det
    hasil = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]

    for i in range(3):
        for j in range(3):
            hasil[i][j] = adjoin[i][j] / det

    return hasil