table_number = 0

while table_number not in range(1, 13):
    try:
        table_number = int(input("Which table (1-12)? "))
        if table_number not in range(1, 13):
            print("Invalid table! Enter an integer between 1 and 12.")
    except ValueError:
        print("Invalid table! Enter an integer between 1 and 12.")

for i in range(1, 13):
    print(f"{i} x {table_number} = {i * table_number}")
