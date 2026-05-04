def solution(n):
    answer = 0
    if n % 2 != 0:
        for i in range(n+1):
            if i % 2 != 0:
                answer += i
    elif n % 2 == 0:
        for j in range(n+1):
            if j % 2 == 0 and j != 0:
                answer += j ** 2
    return answer