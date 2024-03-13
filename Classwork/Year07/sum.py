print("sum 0.1.0")

numbers = []
entry = 0
num_sum = 0

while entry != -1:
    entry = int(input("Enter a number to add to the total..."))
    if entry != -1:
        numbers.append(entry)
    num_sum = sum(numbers)
    print(f"Current total: {num_sum}\n")

print(f"Total: {num_sum}")
input("Press enter to quit")
