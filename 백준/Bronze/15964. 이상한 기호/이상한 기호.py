a, b = map(int, input().split())

def easy_math(a, b):
    result = (a + b) * (a - b)
    return result

print(easy_math(a, b))