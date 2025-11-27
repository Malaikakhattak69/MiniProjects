import math

# -----------------------------
#  Calculation Functions
# -----------------------------
def add(a, b): 
    return a + b

def subtract(a, b): 
    return a - b

def multiply(a, b): 
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

def modulus(a, b):
    try:
        return a % b
    except ZeroDivisionError:
        return "Error: Cannot perform modulus by zero."

def power(a, b):
    return a ** b

def floor_div(a, b):
    try:
        return a // b
    except ZeroDivisionError:
        return "Error: Cannot perform floor division by zero."

def square_root(a):
    if a < 0:
        return "Error: Cannot find square root of a negative number."
    return math.sqrt(a)


# -----------------------------
#  MAIN CALCULATOR
# -----------------------------
def calculator():
    history = []

    while True:
        print("\n===== ADVANCED PYTHON CALCULATOR =====")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Modulus (%)")
        print("6. Power (a^b)")
        print("7. Square Root")
        print("8. Floor Division (//)")
        print("9. Show History")
        print("0. Exit")

        choice = input("\nEnter choice: ")

        if choice == "0":
            print("\nGoodbye! 👋")
            break

        elif choice == "9":
            print("\n--- Calculation History ---")
            if len(history) == 0:
                print("History is empty.")
            else:
                for h in history:
                    print(h)
            continue

        # Square root needs only one number
        if choice == "7":
            try:
                num = float(input("Enter number: "))
                result = square_root(num)
                print(f"Result: {result}")
                history.append(f"sqrt({num}) = {result}")
            except ValueError:
                print("Error: Please enter numbers only.")
            continue

        # Other operations require two numbers
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Error: Please enter valid numbers.")
            continue

        if choice == "1":
            result = add(num1, num2)
        elif choice == "2":
            result = subtract(num1, num2)
        elif choice == "3":
            result = multiply(num1, num2)
        elif choice == "4":
            result = divide(num1, num2)
        elif choice == "5":
            result = modulus(num1, num2)
        elif choice == "6":
            result = power(num1, num2)
        elif choice == "8":
            result = floor_div(num1, num2)
        else:
            print("Invalid choice! Try again.")
            continue

        print(f"Result: {result}")
        history.append(f"{num1} op {num2} = {result}")


# Start program
calculator()
