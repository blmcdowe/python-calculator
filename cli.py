from calculator import add, subtract, multiply, divide

def main():
    print("Welcome to the CLI Calculator!")

    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if operator == '+':
            result = add(num1, num2)
        elif operator == '-':
            result = subtract(num1, num2)
        elif operator == '*':
            result = multiply(num1, num2)
        elif operator == '/':
            result = divide(num1, num2)
        else:
            print("Invalid operator")
            return

        print(f"Result: {result}")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
