def check(side1, side2, side3):
    if (side1 == side2 == side3):
        print("Equilateral triangle")
    elif (side1 == side2) or (side1 == side3) or (side2 == side3):
        print("Isosceles triangle")
    else:
        print("Scalene triangle")

side1 = int(input("Side 1 length: "))
side2 = int(input("Side 2 length: "))
side3 = int(input("Side 3 length: "))
check(side1, side2, side3)
