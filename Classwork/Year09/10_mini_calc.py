def main():
    while True:
        number_1 = float(input("First number: "))
        operation = input("operation (+ - * /): ")
        number_2 = float(input("Second number: "))

        if operation not in ("+", "-", "*", "/"):
            input("Invalid operation. Press [Enter] to continue")

        r = "ERROR"

        if operation == "+":
            r = number_1 + number_2
        elif operation == "-":
            r = number_1 - number_2
        elif operation == "*":
            r = number_1 * number_2
        elif operation == "/" :
            try:
                r = number_1 / number_2
            except ZeroDivisionError:
                input("Error: division by zero. Press [Enter] to continue")

        print(f"{str(number_1)} {operation} {str(number_2)} = {str(r)}")

if __name__ == "__main__":
    print("Mini Calc 0.1.0: 21 Sep 2024 - Oliver Nguyen")
    print("Press [Ctrl-C] to exit")
    main()
