import random 
import string

password = ""

all_character = (
    string.ascii_letters + 
    string.digits + 
    string.punctuation
)
password_length = int(input("Enter Your Password Length : "))

for i in range(password_length):
    password += random.choice(all_character)

print("Password : ", password)