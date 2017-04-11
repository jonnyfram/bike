#model the bicycle industry

class Bicycle(object):
    
    def __init__(self, name):
        self.name = name
        
    def weight(self, weight):
        self.weight = weight
    
    def cost(self, cost):
        self.cost = cost
        
class BikeShop(object):
    def __init__(self, shop_name):
        self.shop_name = shop_name
        self.customers = {}
    
    def bikestock(self, stock):
        self.stock = stock
    
    def sellbike(self):
        #sell bike
        #
        #remove bike from stock
        #
        #show profit (20% over cost)
        pass

        
class Customer(object):
    def __init__(self, name):
        self.name = name
    def wallet(self, amount):
        self.amount = amount
    def bikeowner(self):
        #show if owns bike
        pass

#create bike models:
model1 = Bicycle("Trashbike")
model1.weight(25)
model1.cost(70)

model2 = Bicycle("Okaybike")
model2.weight(21)
model2.cost(250)

model3 = Bicycle("Awesomebike")
model3.weight(15)
model3.cost(700)

model4 = Bicycle("Superbike")
model4.weight(14)
model4.cost(1000)

model5 = Bicycle("Amazebike")
model5.weight(13)
model5.cost(1300)

model6 = Bicycle("SuperAmazeBikePlus")
model6.weight(10)
model6.cost(2000)

#create a bike shop
bikeshop = BikeShop("Bikey Bike Shop")
#TODO
#add 6 different bike models to it's stock

#create 3 customers:
customer1 = Customer("Bob")
customer1.wallet("200")
customer2 = Customer("Mo")
customer2.wallet("500")
customer3 = Customer("Larry")
customer3.wallet("1000")
#add them to a list within bike shop:

#Print the name of each customer 


#and a list of the bikes offered by the bike shop 
#that they can afford given their budget. 
#Make sure you price the bikes in such a way that each customer can afford at least one.

#Print the initial inventory of the bike shop for each bike it carries.

#Have each of the three customers purchase a bike then print the name of the bike 
#the customer purchased, the cost, and how much money they have left over in their bicycle fund.

#After each customer has purchased their bike, the script should print out the bicycle shop's remaining inventory 
#for each bike, and how much profit they have made selling the three bikes.