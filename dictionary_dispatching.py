
# Intialize a list of customers
#
customers= [
            dict(id= 1 , total= 200, coupon_code= 'F20'),
            dict(id= 2 , total= 150, coupon_code= 'P30'),
            dict(id= 3 , total= 100, coupon_code= 'P50'),
            dict(id= 4, total= 110, coupon_code= 'F15')
           ]

# Initialize a list of discounts codes
#
discounts= {
            'F20': (0.0, 20.0),
            'P30': (0.3, 0.0),
            'P50': (0.5, 0.0),
            'F15': (0.0, 15.0)
           }

print('\n')
print("All customer's data: \n")

# Print all customers
#
for customer in customers:
    print(customer)
print('\n')

# Print all coupons' data
#
print(discounts)
print('\n')

# Apply discount for each customer, basing on its coupon
#
for customer in customers:
    code= customer['coupon_code'] # get customer coupon code
    percent, fixed= discounts.get(code, (0.0, 0.0)) # retrieve coupon discount
    customer['discount']= percent * customer['total'] + fixed # apply discount on customer's total

# Print all customers' data
#
for customer in customers:
    print(customer['id'], customer['total'], customer['discount'])
print('\n')