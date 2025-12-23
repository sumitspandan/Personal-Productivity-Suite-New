class Calculator:
    def run(self):
        while True:
            print("\nCALCULATOR")
            print("1. Add")
            print("2. Subtract")
            print("3. Multiply")
            print("4. Divide")
            print("5. Back")

            choice = input("Choose: ")

            if choice == '5':
                break

            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            if choice == '1':
                print("Result:", a + b)
            elif choice == '2':
                print("Result:", a - b)
            elif choice == '3':
                print("Result:", a * b)
            elif choice == '4':
                print("Result:", a / b if b != 0 else "Cannot divide by zero")
