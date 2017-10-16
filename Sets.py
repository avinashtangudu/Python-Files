

# Sets in python

sports = {'Baseball','Football','Basketball','Cricket'}

outdoor = {'Hockey','Football','Volleyball','Cricket'}

print(sports.intersection(outdoor)) # Here You'll get {'Cricket', 'Football'}

print(sports.difference(outdoor)) # Here You'll get {'Basketball', 'Baseball'}

print(sports.union(outdoor)) # Here You'll get all games

# *** Very Important ***

# To create a empty list we can write

list_empty = []
list_empty = list[]

# To create a empty tuples we can write

tuple_empty = ()
tuple_empty = tuple()

# To create a empty sets we can't write like this:

set_empty = {}  # This will create a dictionary
set_empty = set()

