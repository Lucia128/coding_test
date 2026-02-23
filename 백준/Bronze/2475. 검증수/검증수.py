a, b, c, d, e = map(int, input().split())

def validate_num(n1, n2, n3, n4, n5):
    result = (pow(a, 2) + pow(b, 2) + pow(c, 2) + pow(d, 2) + pow(e, 2)) % 10
    return result

print(validate_num(a, b, c, d, e)) 