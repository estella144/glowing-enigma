terms = [0, 1]
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

if length <= 2:
    for i in terms[0:length-1]:
        print(i)
else:
    current_idx = 0
    for i in terms:
        print(i)
        current_idx += 1
        if (current_idx >= 2) and not (current_idx == length):
            terms.append(terms[current_idx-2] + terms[current_idx-1])
