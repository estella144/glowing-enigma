numbers: list[float] = []

for i in range(3):
    n: float = float(input("Number: "))
    numbers.append(n)

max_number: float = max(numbers)
print(f"Largest number: {max_number}")
