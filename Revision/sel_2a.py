n1 = float(input("First number: "))
op = input("Operation (+ - * /): ")
n2 = float(input("Second number: "))

if op == "+":
    ans = n1 + n2
elif op == "-":
    ans = n1 - n2
elif op == "*":
    ans = n1 * n2
else:
    ans = n1 / n2

print(n1, op, n2, "=", ans)
