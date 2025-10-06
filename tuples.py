#7. Tuples: creating, accessing, slicing, immutable nature

##1. Creating a tuple
# Create a tuple to hold the coordinates of a location: `(19.0760, 72.8777)`. Print the tuple.

cords = (19.0760, 72.8777)
print(cords, type(cords))

##2. Accessing elements of a tuple
# From the `coordinates` tuple, print the first element (the latitude).

cords[0]

##3. Tuple unpacking
# Assign the two elements of the `coordinates` tuple to two new variables, `latitude` and
# `longitude`, in a single line. Print both variables.

(latitude, longitude) = cords #unpacking
print(f"Latitude is {latitude}")
print(f"longitude is {longitude}")

##4. Slicing a tuple
# You have a tuple of product codes `('P101', 'P102', 'P103', 'P104', 'P105')`. Create a new
# tuple containing the first three product codes.

product_codes = ('P101', 'P102', 'P103', 'P104', 'P105')
first_3 = product_codes[:3]
first_3

##5. Immutability of tuples
# Try to change the second element of the `product_codes` tuple to 'P200'. What kind of
# error do you get? Add a comment explaining why this happens.

product_codes[1] = 'P200'
print(product_codes)

try:
  product_codes[1] = 'P200'
  print(product_codes)
except TypeError:
  print("Tuples does not support Item assignment or modification")

# ##6. Tuple in a `for` loop
# Iterate through the `product_codes` tuple and print each code on a separate line.

for i in product_codes:
  print(i)

##7. Tuple as a dictionary key
# Create a dictionary where the keys are employee names (strings) and the values are
# tuples containing their shift start and end times, e.g., `{'Priya': ('9 AM', '5 PM')}`. Access
# and print Priya's start time.



##8. Concatenating tuples
# You have two tuples: `t1 = (1, 2, 3)` and `t2 = (4, 5, 6)`. Create a new tuple that is a
# combination of these two.

t1 = (1, 2, 3)
t2 = (4, 5, 6)
t3 = t1 + t2
t3

##9. Nested tuples
# Create a tuple of orders where each order is itself a tuple of `(item_name, quantity)`. For
# example: `(('Vanilla', 2), ('Chocolate', 1))`. Access and print the quantity of the first item.

order1=input("Enter item name and quantity: ").split(" ")
order_1 = tuple(order1)
order2=input("Enter item name and quantity: ").split(" ")
order_2 = tuple(order2)
orders_tuple = (order_1, order_2)

orders_tuple[0][1]

##10. Finding an item in a tuple
# Check if the item 'P103' is in the `product_codes` tuple and print `True` or `False`.

product_codes = ('P101', 'P102', 'P103', 'P104', 'P105')
if 'P103' in product_codes:
  print(True)
else:
  print(False)
