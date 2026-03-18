given = list(map(int, input().split()))
compos = [1, 1, 2, 2, 2, 8]

result = []
for i, j in zip(given, compos):
    result.append(-(i -j))
    
print(*result)