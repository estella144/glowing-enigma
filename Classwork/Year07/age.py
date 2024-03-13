from math import inf

categories = [[0, 5, "a baby"],
              [5, 11, "a child"],
              [12, 17, "a teenager"],
              [18, inf, "an adult"]]
while True:
    try:
        age = int(input("What is your age? "))
    except ValueError:
        print("Invalid value!")
        iv = True

    iv = False
    match = False

    if not iv:
        for i in categories:
            if (age >= i[0]) and (age <= i[1]):
                print("You are " + i[2])
                match = True

    if not match:
        print("Invalid value!")
    
