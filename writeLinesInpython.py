# Python writelines in python
list = ['i am shiva\n', 'i am programmer\n', 'i am the reserver for the city']
with open('pro.txt', 'w') as file:
    content = file.writelines(list)
    print(content)