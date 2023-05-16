#Testing to work with some classes and instances/objects of a class. 

#CLASS DEFINITIONS

class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus
  
  def __repr__(self):
    return self.address
  
  #returns menus that are availble at a given time
  def available_menus(self, time):
    menu_object = []
    for menu in self.menus:
      if (time >= menu.start_time) and (time <=menu.end_time):
        menu_object.append(menu)
    return menu_object

class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time 
  
  def __repr__(self):
    return self.name + ' menu is available from ' + str(self.start_time) + " - "  + str(self.end_time)
  
  #calculates the bill from the purchased items at the restaurant
  def calculate_bill(self, purchased_items):
    price =0
    for item in purchased_items:
      if item in self.items:
        price += self.items[item]
    return price

#MENUS
#Brunch menu
brunch_items = {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}

brunch = Menu("brunch", brunch_items, 11, 16)

#Early bird menu
early_bird_items = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}
early_bird = Menu("early bird",early_bird_items, 15, 18)

#Dinner menu
dinner_items = {
  'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}
dinner = Menu("dinner", dinner_items, 17, 23)

#Kids menu
kids_items = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}
kids = Menu("kids", kids_items, 11, 21)

#Prices
price_brunch = brunch.calculate_bill(["pancakes", "home fries", "coffee"])
print(price_brunch) #just to test/display

price_early_bird = early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)'])
print(price_early_bird) #just to test/display

#FRANCHISES

menus_list = [brunch, early_bird, dinner, kids]

flagship_store = Franchise("1232 West End Road", menus_list)

new_installment = Franchise("12 East Mulberry Street", menus_list)

send_menu= new_installment.available_menus(12)
print(send_menu) #just to test/display

send_menu2 = flagship_store.available_menus(17)
print(send_menu2) #just to test/display

#BUSINESS

#new business
basta_business = Business("Basta Foolin' with my Heart", [flagship_store, new_installment])

arepas_items = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}

arepas_menu = Menu("arepas",arepas_items, 10, 20)

arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])

business_arepa = Business("Take a' Arepa", [arepas_place])

print(business_arepa.franchises[0].menus[0]) #just to test/display