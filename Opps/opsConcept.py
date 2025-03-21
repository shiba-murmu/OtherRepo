# defining class 
class SmartPhone:
    # constructor
    def __init__(self, device, brand):
        self.device = device 
        self.brand = brand
    
    def description(self):
        return f"{self.device} of {self.brand} support Android 14 "

# creating object of the class
phoneObj = SmartPhone("Smartphone", "Samsung")
print(phoneObj.description())