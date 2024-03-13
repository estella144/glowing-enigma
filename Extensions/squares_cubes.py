print("Squares and Cubes")
print("Oliver Nguyen, 20 March 2023")

while True:
    print("Enter s [number] or c [number] to show [number] numbers in the squared or cubed sequence")
    command = input("> ").lower().split(sep=" ")

    valid = True
    
    if len(command) != 2:
        print("Invalid arguments: expected exactly 2")
        valid = False

    if command[0] not in ("s", "c"):
        print("Invalid argument: expected \"s\" or \"c\"")
        valid = False

    try:
        command[1] = int(command[1])
    except IndexError:
        print("Invalid arguments: expected exactly 2")
        valid = False
    except ValueError:
        print("Invalid argument: expected an integer")
        
    numbers = []

    if valid:
        for i in range(1, command[1]+1):
            if command[0] == "s":
                print(i**2)
            else:
                print(i**3)

    
