T = int(input())
results = []
for _ in range(T):
    N,M = map(int, input().split())
    students_left = max(0, N -M)
    results.append(students_left)
for res in results:
    print(res)
