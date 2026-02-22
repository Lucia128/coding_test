submit = []

for i in range(28):
    num = int(input())
    submit.append(num)

for j in range(1, 31):
    if not j in submit:
        print(j)