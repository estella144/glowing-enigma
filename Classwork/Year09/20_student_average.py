students = []

for i in range(10):
    student = {"name": "uh", "tests": [-1, -1, -1]}
    while not student["name"]:
        student["name"] = input(f"Student {i+1} name (leave blank to end input): ")
    for j in range(3):
        while (student["tests"][j] < 0) or (student["tests"][j] > 20):
            try:
                length = int(input(f"Student {i+1} test {j+1} score: "))
                if (student["tests"][j] < 0) or (student["tests"][j] > 20):
                    print("Invalid test score")
                    print("Enter an integer between 0 and 20")
            except ValueError:
                print("Invalid test score")
                print("Enter an integer between 0 and 20")
            
