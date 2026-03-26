a = int(input())
b = int(input())
c = int(input())
d = int(input())

list = [a, b, c, d]
result = sum(list)

x = result // 60
y = result % 60

print(x)
print(y)