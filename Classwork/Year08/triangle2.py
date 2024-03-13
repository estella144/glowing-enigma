def check(side1, side2, side3):
    if (side1 == side2 == side3):
        print("Equilateral triangle")
    elif (side1 == side2) or (side1 == side3) or (side2 == side3):
        print("Isosceles triangle")
    else:
        print("Scalene triangle")

def validate(side1, side2, side3):
    sides = [side1, side2, side3]
    max_side = max(sides)
    equal_sides = 0
    
    for i in sides:
        if i == max_side:
            equal_sides += 1
            del i
    
    if equal_sides != 1:
        return True
    
    side_a = sides[0]
    side_b = sides[1]
    
    if max_side >= side_a + side_b:
        return False

    return True

side1 = int(input("Side 1 length: "))
side2 = int(input("Side 2 length: "))
side3 = int(input("Side 3 length: "))

valid = validate(side1, side2, side3)
if valid:
    check(side1, side2, side3)
else:
    print("Not a triangle")
input()
