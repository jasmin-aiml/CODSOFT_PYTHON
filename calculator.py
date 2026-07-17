# Custom Calculator Project
print("=== WELCOME TO MY CALCULATOR ===")

# Getting inputs from user
val1 = float(input("Please enter number 1: "))
val2 = float(input("Please enter number 2: "))

print("Operations available: add (+), subtract (-), multiply (*), divide (/)")
op = input("What do you want to do? ")

# Processing logic
if op == "+":
    answer = val1 + val2
    print("The final total is:", answer)
elif op == "-":
    answer = val1 - val2
    print("The final result is:", answer)
elif op == "*":
    answer = val1 * val2
    print("Multiplication result:", answer)
elif op == "/":
    if val2 == 0:
        print("Oops! You cannot divide a number by zero.")
    else:
        answer = val1 / val2
        print("Division result:", answer)
else:
    print("Invalid operation selected.")
