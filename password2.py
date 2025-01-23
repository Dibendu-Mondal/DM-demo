import random
import string
try:
    length =int(input("Enter the length of password : "))
    n=int(input("Enter the length of lower : "))
    y = int(input("Enter the length of upper: "))
    z = int(input("Enter the length of digits : "))
    x = length-n-z-y
    lower = string.ascii_lowercase
    a=random.sample(lower,n)
    upper = string.ascii_uppercase
    b = random.sample(upper,y)
    num = string.digits
    c = random.sample(num,z)
    symbol = string.punctuation
    d = random.sample(symbol,x)
    
    all = a + b + c + d

    password = "".join(random.sample(all,length))
                                            

    print("The Generated Password is : ",password)
    
except ValueError as e :
    print("Error :",e)