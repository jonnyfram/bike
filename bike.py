#model the bicycle industry

class Bicycle(object):
    
    def __init__(self, name, weight, cost):
        self.name = name
        self.weight = weight
        self.cost = cost
        
class BikeShop(object):
    def __init__(self, shop_name, stock):
        self.shop_name = shop_name
        self.customers = {}
        self.stock = stock
    
    def sellbike(self):
        #sell bike
        #
        #remove bike from stock
        #
        #show profit (20% over cost)
        pass

        
class Customer(object,):
    def __init__(self, name, money):
        self.name = name
        self.money = money
        
#create bike models:
model1 = Bicycle("Trashbike", 25, 70)
model2 = Bicycle("Okaybike", 21, 250)
model3 = Bicycle("Awesomebike", 15, 700)
model4 = Bicycle("Superbike", 14, 1000)
model5 = Bicycle("Amazebike", 13, 1300)
model6 = Bicycle("SuperAmazeBikePlus", 10, 2000)

#create a bike shop
#add 6 different bike models to it's stock
bike_model_list = [model1, model2, model3, model4, model5, model6]
bike_stock = {}
#create a dictionary of the bikes with a stock number
for x in bike_model_list:
    bike_stock[x] = 10

print(bike_stock)

bikeshop = BikeShop("Bikey Bike Shop", bike_stock)

#create 3 customers:
customer1 = Customer("Bob", 200)
customer2 = Customer("Mo", 500)
customer3 = Customer("Larry", 1000)
#add them to a list
customer_list = [customer1, customer2, customer3]
#Print the name of each customer- why do I format it customer_list[customer].name and not customer_list[customer.name]?
#Does the for loop treat customer_list[customer].name as a single customer from the list?
for customer in range(len(customer_list)):
    print(customer_list[customer].name)

#and a list of the bikes offered by the bike shop 
#that they can afford given their budget. 
#Make sure you price the bikes in such a way that each customer can afford at least one.

#Print the initial inventory of the bike shop for each bike it carries.

#Have each of the three customers purchase a bike then print the name of the bike 
#the customer purchased, the cost, and how much money they have left over in their bicycle fund.

#After each customer has purchased their bike, the script should print out the bicycle shop's remaining inventory 
#for each bike, and how much profit they have made selling the three bikes.