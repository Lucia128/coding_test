N, M = map(int, input().split())

A = []
B = []

for i in range(N):
    a = list(map(int, input().split()))
    A.append(a)

for i in range(N):
    b = list(map(int, input().split()))
    B.append(b)

# 덧셈
for i in range(N):
    for j in range(M):
        sum = A[i][j] + B[i][j]
        print(sum, end = ' ')
    print()   # 줄바꿈