class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def drive(self):
        print(f"{self.brand} {self.model} is driving.")

# Creating objects
#car1 = Car("Toyota", "Corolla")
#car2 = Car("Ford", "Fiesta")

#car1.drive()  # Output: Toyota Corolla is driving.
#car2.drive()  # Output: Ford Fiesta is driving.

class CitrusFruit:
    
    def __init__(self, name, color, taste):
        self.name = name
        self.color = color
        self.taste = taste 
        
    def describe(self):
        print(f"{self.name} is {self.color} and tastes {self.taste}.")
        
# Derived classes (inheritance)
class Orange(CitrusFruit):
    
    def __init__(self):
        super().__init__("Orange", "orange", "sweet and tangy")
    
    def juice(self):
        print("Fresh orange juice is delicious!")

class Lemon(CitrusFruit):
    
    def __init__(self):
        super().__init__("Lemon", "yellow", "sour")
    
    def zest(self):
        
        print("Lemon zest adds flavor to cakes!")

class Grapefruit(CitrusFruit):
    
    def __init__(self):
        super().__init__("Grapefruit", "pink", "bitter-sweet")
    
    def salad(self):
        print("Grapefruit segments are great in salads!")
        
orange = Orange()
lemon = Lemon()
grapefruit = Grapefruit()

orange.describe()     
lemon.describe()      
grapefruit.describe() 

orange.juice()        
lemon.zest()          
grapefruit.salad()    

# Create a class
class Person:
    def __init__(self, name, age):
     self.name = name
     self.age = age
        
    def greet(self):
        print(f"Hello, my name is", self.name)
#create objects
p1 = Person("John", 36)

#call the greet function
p1.greet()
