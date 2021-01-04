
from datetime import date, timedelta

#---------------------------------| CONTINUE STATEMENT EXAMPLE |------------------------------

# Set today and tomorrow times
#
today= date.today()
tomorrow= today + timedelta(days=1)

# Set products and their expiration times and price
#
products= [
            {'sku': '1', 'expiration_date': today, 'price': 400.00},
            {'sku': '2', 'expiration_date': tomorrow, 'price': 45.00},
            {'sku': '3', 'expiration_date': today, 'price': 73.00}
          ]

# Scan each product and modify its price if its expiration time is today
#
for product in products:
    if product['expiration_date'] != today:
        continue
    product['price'] *= 0.8
    print("Price for ", product['sku'], 
          "is now: ", product['price'])



#---------------------------------| BREAK STATEMENT EXAMPLE |------------------------------

found= False
items= [0.0, True, 5.6, 0, 1]

# Scan each item to found at least one that satisfy TRUE condition
#
for item in items:
    if item:
        found= True
        print("Exiting while loop...")
        break

if found:
    print("Found at least an item that is TRUE")
else:
    print("Not found any element that is TRUE")