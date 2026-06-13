import shinta024 as ta

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

print("\nMatriks A:")
ta.tampilkan(A)
print("\nMatriks B:")
ta.tampilkan(B)
print("\nPenjumlahan A + B:")
ta.tampilkan(ta.penjumlahan(A, B))
print("\nPengurangan A - B:")
ta.tampilkan(ta.pengurangan(A, B))
print("\nPerkalian A x B:")
ta.tampilkan(ta.perkalian(A, B))
print("\nTranspose A:")
ta.tampilkan(ta.transpose(A))
print("\nDeterminan A:", ta.determinan(A))
