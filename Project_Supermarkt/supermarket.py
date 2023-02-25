# (Aufgabe 1) 

class Supermarket():
    def __init__(self,name,street,city):
        self.name = name
        self.street = street
        self.city = city
        self.employees = []
        self.products = []
        
        
# (Aufgabe 2)
import datetime

class Employee():
    def __init__(self,name,age,pers_id,job):
        self.name = name.title()
        self.age = int(age)
        self.pers_id = pers_id
        self.job = job
        
        
    def greet_customer(self):
        time = datetime.datetime.now().strftime("%H:%M")
        (f"Guten Tag. Mein Name ist {self.name} und ich bin {self.job} in diesem Supermarkt. Es ist momentan {time}  Uhr - wie kann ich Ihnen helfen?")
        
    def celebrate_birthday(self):
        self.age += 1
        (f"Juhu! Heute werde ich {self.age} Jahre!")
        
# (Aufgabe 3)

class Product():
    def __init__(self,name , prod_id , category , price):
        self.name = name
        self.prod_id = prod_id
        self.price = price
        
        if category in ["food","drinks","others"]:
            self.category = category
        
        else:
            self.category = "others"
            
    def apply_discount(self,discount):
        
        if 0 <= discount <= 100:
            self.price = self.price - (discount/100)
        
        else:
            print("der Discount ist ungültig, es werden 5 % Rabatt berechnet")
            self.price = self.price - self.price * 0.05
            
if __name__ == "__main__":
    new_product = Product("Kinderschockolade", 5, "food", 2)
    print(new_product.price)
    new_product.apply_discount(1)
    print(new_product.price)
    
    
        
    
        
    
    