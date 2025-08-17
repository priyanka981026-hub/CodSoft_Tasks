# PASSWORD GENERATOR
import random
import string
length = (input("Enter password length:"))
if length.isdigit():                       
    length = int(length)   
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters)
                    for _ in range(length))
print("Generated password:",password)