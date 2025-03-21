# polymorphisms
class SmartPhone:
    def classMethodHere(self):
        print('I am the class method or parent method.')

class ChildClass(SmartPhone):
    def classMethodHere(self):
        print('I am override the method here.')


child = ChildClass()
child.classMethodHere()
child.classMethodHere()
parent = SmartPhone()
parent.classMethodHere()