import time

terms = [0, 1]
length = 0

t1 = time.time()
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
    pass
else:
    current_idx = 0
    for i in terms:
        current_idx += 1
        if (current_idx >= 2) and not (current_idx == length):
            terms.append(terms[current_idx-2] + terms[current_idx-1])
    
t2 = time.time()
duration = t2 - t1

print(f"Done. (Took {duration} seconds)")
input("Press [Enter] to display results")
print(sequence)
input("Done. Press [Enter] to quit")

