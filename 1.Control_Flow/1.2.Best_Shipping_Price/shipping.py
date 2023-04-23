
#Any weight can be placed below
weight = 41.5

#Ground Shipping (price per pound + a flat charge)
if weight <=2:
  ground_cost = (weight * 1.50) + 20.00
elif weight > 2 and weight <= 6:
  ground_cost = (weight * 3.00) + 20.00
elif weight > 6 and weight <= 10:
  ground_cost = (weight * 4.00) + 20.00
else:
   ground_cost = (weight * 4.75) + 20.00

print("Ground shipping cost: $",ground_cost)

#Ground Premium Shipping (has a flat charge only)
premium_shipping_cost = 125.00
print("Ground shipping premium cost: $",premium_shipping_cost)

#Drone Shipping (only price per pound but triple the rate of ground shipping)
if weight <=2:
  drone_cost = weight * 4.50
elif weight > 2 and weight <= 6:
  drone_cost = weight * 9.00
elif weight > 6 and weight <= 10:
  drone_cost = weight * 12.00
else:
  drone_cost = weight * 14.25

print("Drone shipping cost: $",drone_cost)