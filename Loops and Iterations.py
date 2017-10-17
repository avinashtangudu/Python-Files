

even_no = [2,4,6,8,10,12,14]

# Here You going to print all the numbers are in even numbers
for numbers in even_no:
    print(numbers)

# In this snippet we can find the particular number is present or not by using break statement
for numbers in even_no:
    if numbers == 8:
        print("It's Available")
        break
    print(numbers)

# Here we can continue even after printing statement.

for numbers in even_no:
    if numbers == 8:
        print("It's Available")
        continue
    print(numbers)

# It will print 'ABC' all the even along with alphabets

for numbers in even_no:
    for alphabets in 'ABC':
        print(numbers, alphabets)

# This while loop, which goes through and increments the value until the given value.

avi = 1

while avi < 10:
    print(avi)
    avi += 2
        




