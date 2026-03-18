N = int(input())

arr = []
for _ in range(N):
    nums = int(input())
    arr.append(nums)

arr.sort()

for i in arr:
    print(i)