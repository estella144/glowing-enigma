print("tables2")

current_table = int(input("What table do you want to practice? "))
command = ""
i = 0
correct_answers = 0
wrong_answers = 0

while command.lower() != "finished":
    while command.lower() != "done":
        answer = current_table * i
        attempt = input(f"{current_table} x {i} = ")
        try:
            attempt = int(attempt)
            if attempt == answer:
                print("Correct")
                correct_answers += 1
                i += 1
            else:
                print("Incorrect")
                wrong_answers += 1
                i += 1
        except ValueError:
            command = str(attempt)
            if command in ("done", "finished"):
                break

    current_table += 1
    if command == "finished":
        break

print(f"Correct: {correct_answers}")
print(f"Wrong:   {wrong_answers}")
            
        
