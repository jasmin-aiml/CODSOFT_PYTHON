# Task 3: My Password Generator
import random

print("--- Welcome to the Password Generator Tool ---")
user_len = int(input("How many characters long do you want your password? "))

# Manually defining characters to make it look standard beginner-built
letters_lower = "abcdefghijklmnopqrstuvwxyz"
letters_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
nums = "0123456789"
syms = "!@#$%^&*()_+"

all_pool = letters_lower + letters_upper + nums + syms

generated_pass = ""
for count in range(user_len):
    random_char = random.choice(all_pool)
    generated_pass = generated_pass + random_char

print("----------------------------------------")
print("Your secure random password is:", generated_pass)
print("----------------------------------------")

