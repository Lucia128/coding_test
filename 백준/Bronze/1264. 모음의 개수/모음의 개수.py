vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

while True:
    sentence = input()
    count = 0

    if sentence == '#':
        break
    
    for i in sentence:
        if i in vowel:
            count += 1
    print(count)