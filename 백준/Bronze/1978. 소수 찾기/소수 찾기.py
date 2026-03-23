n = int(input())
nums = list(map(int, input().split()))

count = 0

for num in nums:
    if num == 1:
        continue   # 1은 소수가 아니므로 제외
    
    is_prime = True
    # 2부터 num-1까지 나누어 보며 약수가 있는지 확인
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    # is_prime이 True이면 소수이므로, count 증가
    if is_prime:
        count += 1

print(count)