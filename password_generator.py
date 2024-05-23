#random password generator
"""
import random
import string

def generate_password(length):
    if length < 4:
        return "password length should be atleast 4 char" 
    
        characters=string.ascii_letters+ string.digits+ string.punctuation
        password="".join(random.choices(characters,k=length))

        return password

length=int(input("Enter the length of password: "))
print(f"Your generated password is : {generate_password(length)}")

"""
"""
import random
lower_case="abcdefghijklmnopqrstuvwxyz"
upper_case="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits="1234567890"
symbols="&*%$3@!?\/."
all=lower_case + upper_case + digits +symbols
length=10
password="".join(random.sample(all,length))
print(f"Your generated password is : {password}")
"""

import random
import string
all_characters=string.ascii_letters + string.digits + string.punctuation
length=int(input("Enter the required password length: "))
password="".join(random.sample(all_characters,length))
print(f"Your Generated Password is : {password}")