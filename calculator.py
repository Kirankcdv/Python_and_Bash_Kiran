# Menu-Driven Python Calculator

def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


while True:
    print("\n===== PYTHON CALCULATOR =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "5":
        print("Thank you for using the calculator!")
        break

    if choice in ["1", "2", "3", "4"]:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                result = addition(num1, num2)
                print("Result:", result)

            elif choice == "2":
                result = subtraction(num1, num2)
                print("Result:", result)

            elif choice == "3":
                result = multiplication(num1, num2)
                print("Result:", result)

            elif choice == "4":
                try:
                    result = division(num1, num2)
                    print("Result:", result)
                except ZeroDivisionError as error:
                    print("Error:", error)

        except ValueError:
            print("Error: Please enter valid numbers.")

    else:
        print("Invalid choice. Please select 1 to 5.")