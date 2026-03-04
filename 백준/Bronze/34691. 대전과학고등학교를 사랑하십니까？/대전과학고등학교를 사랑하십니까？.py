symbols = {
    'animal':'Panthera tigris',
    'tree':'Pinus densiflora',
    'flower':'Forsythia koreana'
    }

while True:
    words = input()
    if words == 'end':
        break
    else:
        print(symbols[words])