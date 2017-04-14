#model the bicycle industry
from random import *
#for seperating print outs during test:
print("###########################################")

class Bicycle(object):
    
    def __init__(self, name, weight, cost):
        self.name = name
        self.weight = weight
        self.cost = cost
        
class BikeShop(object):
    def __init__(self, name, stock, stock_numbers):
        self.name = name
        self.stock = stock
        self.stock_numbers = stock_numbers

    def print_stock_numbers(self):
        print("The shop has these models for sale:")    
        for bikes in range(len(self.stock)):
            print("                                 "+self.stock[bikes].name)
            print("                                      Number in stock: "+str(self.stock_numbers[bikes]))
                
    def sell_bike(self, customer):
        
        markup = 1.2
        
        self.customer = customer
    
        for bike in range(len(bikeshop.stock)):
            bike_cost = bikeshop.stock[bike].cost
        
            if customer.money >= bike_cost*markup:
                print(customer.name+" can afford: "+bikeshop.stock[bike].name)
                can_afford = bikeshop.stock[bike]
            elif customer.money < bike_cost:
                #print(customer3.name+" cannot afford: "+bikeshop.stock[bike].name)
                pass
            
        #establish what bike is being purchased using the previous var + the markup   
        print(customer.name+" decides to buy a "+can_afford.name+", this costs $"+str(can_afford.cost*markup)+".")
        
        customer.money -= can_afford.cost
        #print how much the customer has left in their wallet:
        print(customer.name+" has $"+str(customer.money)+" left!")
        
        #remove that bike from the bike shop's inventory
        #get the position in list, then in the corresponding position in the stock numbers then remove it then print remaining inventory:
        
        removed_bike = bikeshop.stock.index(can_afford)
        bikeshop.stock_numbers[removed_bike] -= 1
        bikeshop.print_stock_numbers()
        
        #profit made
        print("Profit made selling "+can_afford.name+" to "+customer.name+": "+str(can_afford.cost*markup-can_afford.cost))
        
 
class Customer(object,):
    def __init__(self, name, money):
        self.name = name
        self.money = money
        
#create bike models:
model1 = Bicycle("Trashbike", 25, 70)
model2 = Bicycle("Okaybike", 21, 250)
model3 = Bicycle("Awesomebike", 15, 700)
model4 = Bicycle("Superbike", 14, 999)
model5 = Bicycle("Amazebike", 13, 1300)
model6 = Bicycle("SuperAmazeBikePlus", 10, 2000)

#create a bike shop
#add 6 different bike models to it's stock
bike_model_list = [model1, model2, model3, model4, model5, model6]
bike_stock = bike_model_list
stock_numbers = []
#create initial stock numbers based on models from bike_stock:
for bikes in bike_stock:
    stock_numbers.append(3)

bikeshop = BikeShop("Bikey Bike Shop", bike_stock, stock_numbers)

#create 3 customers:
customer1 = Customer("Bob", 200)
customer2 = Customer("Mo", 500)
customer3 = Customer("Larry", 1000)
customer_list = [customer1, customer2, customer3]

#Print the name of each customer- why do I format it customer_list[customer].name and not customer_list[customer.name]?
#Does the for loop treat customer_list[customer].name as a single customer from the list?
print("Three guys walk into "+bikeshop.name+"!")
for customer in range(len(customer_list)):
    print(customer_list[customer].name)
        
bikeshop.print_stock_numbers()

#each customer buys a bike:
for customer in customer_list:
    bikeshop.sell_bike(customer)
