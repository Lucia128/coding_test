import sys

N = int(sys.stdin.readline())

arr = []
for _ in range(N):
    nums = int(sys.stdin.readline())
    arr.append(nums)

arr.sort()

for i in arr:
    print(i)