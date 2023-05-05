#Mini project working with lists, for loops and list comprehensions for a hair salon.

hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
#price of each hairstyle
prices = [30, 25, 40, 20, 20, 35, 50, 35]
#last week purchases per hairstyle
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

#sum of all prices together with help of for loop
total_price = 0
for price in prices: total_price += price

#Calculating average price
average_price = total_price / len(prices)
print("Average Haircut Price: ${0}".format(average_price))

#creating a new list with list comprehension where we cut each price by 5
new_prices = [price - 5 for price in prices]
print(new_prices)

#REVENUE

total_revenue = 0
#calculate revenues from last week with for loop
for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
print("Total Revenue: ${0}".format(total_revenue))

#Daily average
average_daily_revenue = total_revenue / 7
print("Average Daily Revenue: ${0}".format(average_daily_revenue))

#create list that only contains haircuts under 30 dollars
cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)) if new_prices[i] < 30 ]
print(cuts_under_30)