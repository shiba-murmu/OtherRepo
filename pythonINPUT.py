# Python input here..
def userName():
    while True:
        try:
            name = str(input('Name : '))
            return name
        except :
            print('Invalid input.')

def userAge():
    while True:
        try:
            age = int(input('Age : '))
            return age
        except:
            print('Invalid age.')

def userSalary():
    while True:
        try:
            salary = float(input('Salary : '))
            return salary
        except:
            print('Invalid salary.')

def user():
    while True:
       name = userName()
       age = userAge()
       salary = userSalary()
       return {
           name , age, salary
       }

userData = user() # get access here to.
# print(userData[name])
print('Enter the prime factor.')

