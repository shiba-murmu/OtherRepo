# Animal 
class Animal:
    # constructor
    def __init__(self, animal, color, vorus, eatingItems, crying):
        self.animal = animal
        self.vorus = vorus
        self.color = color
        self.eatingItems = eatingItems
        self.crying = crying
    
    def crying(self):
        return f"Crying : {self.crying}"

dog = Animal('DOG', "GREEN", "CARNIVORUS", "CHICKEN-MEAT", 'WAOO-WAOO')
dog.crying()
    
    