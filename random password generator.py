import random
import string
print("Welcome to our Ramdom Password Generator \n")

length = int(input("Enter the length of password :"))
lower = string.ascii_lowercase
upper = string.ascii_uppercase
digit = string.digits
symbols = string.punctuation
x = lower + upper + digit + symbols
y = random.sample(x , length)
password = "".join(y)
print(password)
