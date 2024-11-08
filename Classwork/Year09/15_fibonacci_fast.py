import time

def fib(n):

    def fib_doubling(k):
        """Helper function using fast doubling to compute numbers."""
        if k == 0:
            return (0, 1)
        else:
            a, b = fib_doubling(k // 2)
            c = a * (2 * b - a)
            d = a * a + b * b
            if k % 2 == 0:
                return (c, d)
            else:
                return (d, c + d)

    sequence = []
    for i in range(n):
        sequence.append(fib_doubling(i)[0])

    return sequence

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

t1 = time.time()
sequence = fib(length)
t2 = time.time()
duration = t2 - t1
print(f"Done. (Took {duration} seconds)")
input("Press [Enter] to display results")
print(sequence)
input("Done. Press [Enter] to quit")
