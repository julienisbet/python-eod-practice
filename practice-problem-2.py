# DICTIONARY
#

prices = [1.25, 0.75, 2, 4, 2.25, 1.10, 1.10]
toppings = ['pepperoni', 'mushrooms', 'pineapple', 'sausage', 'bell peppers', 'olives']

def formatted_price(price):
    return "$%.2f" % price

## Part 1
# Create a dictionary called topping_prices using zip that has the topping
# name as a key and its floating point price as the value

# Part 2
# Create a function called topping_info that accepts a topping as an argument
# and returns a dictionary containing the keys 'topping', 'price', 'formatted_price'
# Example: topping_info('pepperoni') should output:
#  {'topping': 'pepperoni', 'price': 1.25, 'formatted_price': '$1.25'}

# Part 3
# Use the topping_info function to generate a list of topping info