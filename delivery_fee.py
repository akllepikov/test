

#// BEGIN_TODO [Send_a_parcel] Send a parcel 
global AFRICA 
global AMERICA 
global ANTARCTICA 
global ASIA 
global EUROPE 
global OCEANIA 
     

class Continent:
    def __init__(self, name, price0_5, price6_10, price11_15, price16_20):
        self.name = name
        self.price = {"Price0_5" : price0_5, 
                      "Price6_10" : price6_10,
                      "Price11_15" : price11_15,
                      "Price16_20" : price16_20,
                      }
        
class Package:
    def get_price(self, destination, weight):
        if weight >0 and weight <= 5 :
            return destination.price["Price0_5"] * weight
        elif weight >= 6 and weight <= 10 :
            return destination.price["price6_10"] * weight
        elif weight >= 11 and weight <= 15 :
            return destination.price["Price11_15"] * weight
        elif weight >= 16 and weight <= 20 :
            return destination.price["Price16_20"] * weight
        else:
            return -1
    
    def __init__(self, destination, weight):
        self.destination = destination
        self.weight = weight
        self.price = self.get_price(destination, weight)

AFRICA = Continent("Africa", 13, 7.5, 6.5, 5)
AMERICA = Continent("America",13,7.5,6.5,5)
ANTARCTICA = Continent("Antarctica",20, 10 ,7.5 ,7) 
ASIA = Continent("Asia",12, 7, 5.5, 4) 
EUROPE = Continent("Europe", 5, 4, 2.5, 1.5) 
OCEANIA = Continent("Oceania",12, 7, 5.5, 4) 

continent = AFRICA
kg = 5
package = Package(continent, kg)
    
#// END_TODO [Send_a_parcel]

print(package.price)
