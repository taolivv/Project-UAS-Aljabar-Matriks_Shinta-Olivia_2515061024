def tampilkan(M):
    for baris in M:
        print(baris)
        
def penjumlahan(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def pengurangan(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def perkalian(A, B):
    hasil = [[0] * len(B[0]) for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(A[0])):
                hasil[i][j] += A[i][k] * B[k][j]
    return hasil

def transpose(M):
    return [[M[j][i] for j in range(len(M))] for i in range(len(M[0]))]

def determinan(M):
    n = len(M)
    if n == 1:
        return M[0][0]
    if n == 2:
        return M[0][0] * M[1][1] - M[0][1] * M[1][0]