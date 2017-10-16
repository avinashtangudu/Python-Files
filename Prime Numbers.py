

# Getting a "Prime" Numbers in python with 3 simple steps

# Enter the range from which number you want to get
for num in range(1,101):
    if all(num%i!=0 for i in range(2,num)):
       print num
