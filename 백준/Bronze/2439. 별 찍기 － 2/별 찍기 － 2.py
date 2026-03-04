N = int(input())

for i in range(1, N+1):
    stars = '*' * i
    # print(f"{stars:>{N}}")
    print(stars.rjust(N))