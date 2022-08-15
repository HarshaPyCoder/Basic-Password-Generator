import random 
import string

print("Welcome to Password Generator")

length = int(input("Type the length of the Password:  "))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

# def 
fullpass = lower + upper + num + symbols

temp = random.sample(fullpass,length)

password = " " .join(temp)

print(password)





