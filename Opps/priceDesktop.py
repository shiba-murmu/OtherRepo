# class desktop prices modifications
class Desktop:
    # constructor
    def __init__(self):
        self.__max_price = 25000
    
    def sell(self):
        return f"selling price {self.__max_price}"
    
    def price_setter(self, price):
        if price > self.__max_price:
            self.__max_price = price 

sellerUser = Desktop()

# accessing prices 
print(sellerUser.sell())

# modifying directly prices
sellerUser.__max_price = 30000
print(sellerUser.sell())

# modifying using setter method 
sellerUser.price_setter(40000)
print(sellerUser.sell())

print(sellerUser._Desktop__max_price , "I am new attributes here.")
print(sellerUser.__dict__)