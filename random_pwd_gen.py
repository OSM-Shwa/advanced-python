# Create a random password generator!

# import random
import random

# gather our characters
lower = "abcdefghijklmnopqrstuvwxyz"
upper = lower.upper()
symbols = "!@#$%^&*()-_=+]}[{;:/?.>,<"
numbers = "1234567890"
all = "".join([lower,upper,symbols,numbers])

# set password length
length = 20

# loop through each character
password = ""
for _ in range(length):
    password = "".join([password, random.choice(all)])

print(password)
