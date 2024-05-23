#random password generator

import random
import string
all_characters=string.ascii_letters + string.digits + string.punctuation
length=int(input("Enter the required password length: "))
password="".join(random.sample(all_characters,length))
print(f"Your Generated Password is : {password}")
