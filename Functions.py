
# Functions in Python

# we can define a function with 'def'.

def hello_python():
    pass
print(hello_python()) # It prints a 'None Value'

# It will prints the print statement

def hello_python():
    print('Namaste Python..!')
hello_python()

# One More Method

def hello_python():
    return 'Namaste Python..!'
print(hello_python())

# defining a function with args & kwargs

def cust_details(*args, **kwargs):
    print(args)
    print(kwargs)

products = ['Sauce','Meat','Beer']
cust_info = {'Name': 'Sachin','Age':45,'Address': '1818 Road'}

cust_details(*products, **cust_info)
