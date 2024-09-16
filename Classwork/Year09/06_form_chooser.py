# wip lol
forms: dict[str, str] = {"D1": "45",
                         "D2": "43",
                         "D3": "15",
                         "D4": "51",
                         "D5": "26",
                         "D6": "29",
                         "D7": "46",
                         "D8": "5",
                         "F1": "24",
                         "F2": "36"}

name = input("Please enter your name: ")
form = input("Please enter your form: ")
if form not in forms:
    print("Invalid form! Please enter a valid form.")
    form = input("Please enter your form: ")
print(f"Hello {name}, please go to room {forms[form]}")
