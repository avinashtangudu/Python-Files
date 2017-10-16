
# List Method in Python

Fruits = ["Mango","Pineapple","Banana","Watermelon","Papaya","Orange"]

print(Fruits) # Print all the fruits in the list

print(Fruits[2:]) # Slicing a lists Here the "2:" is slicing after banana

print(Fruits[:2]) # Slicing a list Here the ":2" is slicing before banana

# Appending a new fruits in list

Fruits.append('Jackfruit') # This will add inside a fruit list along with previous lists

print(Fruits)

# Insert a fruit in the particular location

Fruits.insert(1, 'Cherry') # This will overwrite in the place of 'Pineapple'.

print(Fruits)

# Combinig two different lists, Create a different list of variable.

New_Fruits = ['Grapes','Strawberry']

Fruits.insert(0, New_Fruits) # This is will add in the "0th" location.

print(Fruits)

# One More Method for Combining

Fruits.extend(New_Fruits) # This will add at the end of the first variable.

# Removing a values in the list

Fruits.remove('Banana') # Removes particular value which is mentioned in this.

Fruit.pop() # Here the pop will pop the intial value

# Index or Position

print(Fruits.index('Mango')) # This will give the position of that value

print('Cherry' in Fruits) # This will give "True"

for index, fruit in  enumerate(Fruits):
    print(index, fruit)     # This will print the position along with the values(Usually in python it starts with 0) in it
    
for index, fruit in  enumerate(Fruits, start=1):
    print(index, fruit)   # This will print from the position 1 not from the 0

# Sorting

Fruits.reverse() # reverse the list of values
print(Fruits)

Fruits.sort() # Sorting the order in ascending
print(Fruits)

Fruits.sort(reverse=True) # Sorting in reverse order
print(Fruits)

nums = [2,4,5,6,7,9]

print(sum(nums)) # You'll get the sum of the values

print(max(nums)) # You'll get the maximum value which is "9"

print()
