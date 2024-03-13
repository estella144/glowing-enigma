conv = input("[I]nch -> cm or [C]m to inch").lower()

if conv == "f":
    m = float(input("Inches: "))
    print(m/2.54)
else:
    m = float(input("Cm: "))
    print(m*2.54)
