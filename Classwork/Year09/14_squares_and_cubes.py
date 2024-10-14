sequence_choice = ""
length = 0

while sequence_choice not in ("s", "c"):
    sequence_choice = input("Sequence to display ([s]quares/[c]ubes): ").lower()
    if sequence_choice not in ("s", "c"):
        print("Invalid sequence choice")
        print("Enter 's' to display squares and 'c' to display cubes.")

while length <= 0:
    try:
        length = int(input("Numbers to display in sequence: "))
        if length <= 0:
            print("Invalid sequence length")
            print("Enter a positive integer")
    except ValueError:
        print("Invalid sequence length")
        print("Enter a positive integer")

if sequence_choice == "s":
    exponent = 2
else:
    exponent = 3

for i in range(1, length + 1):
    print(i^exponent)
