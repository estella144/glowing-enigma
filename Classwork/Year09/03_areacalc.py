width = -1
length = -1

while (width < 0) or (length < 0):
    print("Enter a number greater than or equal to 0!")
    try:
        width = float(input("Width: "))
        length = float(input("Length: "))
    except ValueError:
        print("Invalid input: width and length must be integers")

area = round(width * length, ndigits=10)
print(f"Area: {area}")
