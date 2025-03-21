# with open('text.txt' , 'r') as file:

#     content = file.read()
#     print(content)
import time
with open('text.txt' , 'r') as file:
    line = file.readline()
    # print(line
    while line:
        time.sleep(2)
        print(line , end='')
        line = file.readline()