print("calc 0.1.0 (KES) 15 Feb 2023")

while True:
    n1 = float(input("First number: "))
    op = input("Operation (+ - * /): ")
    n2 = float(input("Second number: "))
    
    if op not in ("+", "-", "*", "/"):
        input("Invalid operation")

    r = "ERROR"
    
    if op == "+":
        r = n1 + n2
    elif op == "-":
        r = n1 - n2
    elif op == "*":
        r = n1 * n2
    elif op == "/" :
        try:
            r = n1 / n2
        except ZeroDivisionError:
            input("Error: division by zero. Press enter to continue")

    print(f"{str(n1)} {op} {str(n2)} = {str(r)}")
