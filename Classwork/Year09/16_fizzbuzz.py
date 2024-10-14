length = 0

while length <= 0:
    try:
        length = int(input("Numbers to display in sequence: "))
        if length <= 0:
            print("Invalid sequence length")
            print("Enter a positive integer")
    except ValueError:
        print("Invalid sequence length")
        print("Enter a positive integer")

for i in range(1, length + 1):
    replacement_string = ""
    replacement_performed = False
    if i % 3 == 0:
        replacement_string += "FIZZ"
        replacement_performed = True
    if i % 5 == 0:
        replacement_string += "BUZZ"
        replacement_performed = True

    if replacement_performed:
        replacement_string += "!"
        print(replacement_string)
    else:
        print(i)
