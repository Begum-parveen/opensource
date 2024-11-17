N = int(input())
matrix =[]
for _ in range(N):
    row = input().strip()
    matrix.append(row)
mirrored_matrix = []
for row in matrix:
    mirrored_matrix.append(row[::-1])
for row in mirrored_matrix:
    print(row)
