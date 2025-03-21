name = 'shiba murmu'

with open('file.txt', 'w') as file:
    content = file.write(f'{name}')
    print('File writes correctly.')