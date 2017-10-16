
'''
Conditional in Python,
This can be also called as Booleans '''

# Comparisons:
# Equal:               == 
# Not Equal:           != 
# Greater Than:         >
# Less Than:            < 
# Greater or Equal:    >=
# Less or Equal:       <=
# Object Identity:     is

# and
# or
# not

fruit = "Mango"

if fruit == 'Mango':
    print("Yes this is a Mango") # This will print "Yes this is a Mango".

# Else Condition
if fruit == 'Mango':
    print("Yes this is a Mango") 
else:
    print("This is not Mango") # This else statement will get printed.

# Elif Condition
if fruit == 'Mango':
    print("Yes this is a Mango")
elif fruit == "Banana":
    print("Yes is Banana") # This else statement will get printed.
else:
    print("Not Found") 

# Using 'And','Or' & 'Not'

role = 'Data Analyst'
passwd = False

if role == 'Data Analyst' or passwd:
    print('Logging In')
else:
    print("Wrong Password") # Here You'll be getting printed "Logging In"

# You can simply check the conditions like this as well
True and False
>>False
True and True
>>True
False and False
>>False
False and True
>>False

# Checking the ID's
table = [5,2,7,52,30]
table2 = [7,8,9,23,41]

print(table in table2)
>>> False
print(id(table))
>>> 4597098824
print(id(table2))
>>> 4597190024

# Assigning the table in the same value
table = [5,2,7,52,30]
table2 = table

print(id(table))
print(id(table2))
print(id(table) == id(table))

# False Values:
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. For example, '', (), [].
    # Any empty mapping. For example, {}.

python = False # Try Here python = with diff e.g like = {},[],0,10,'Text'

if python:
    print('True Evaluation')
else:
    print('False Evaluation')


