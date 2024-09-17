rooms: dict[str, str] = {"D1": "45",
                         "D2": "43",
                         "D3": "15",
                         "D4": "51",
                         "D5": "26",
                         "D6": "29",
                         "D7": "46",
                         "D8": "5",
                         "F1": "24",
                         "F2": "36",
                         "F3": "28",
                         "F4": "18",
                         "F5": "47",
                         "F6": "16",
                         "F7": "13",
                         "F8": "52",
                         "S1": "CGL",
                         "S2": "21",
                         "S3": "37",
                         "S4": "40",
                         "S5": "34",
                         "S6": "12",
                         "W1": "42",
                         "W2": "39",
                         "W3": "32",
                         "W4": "48",
                         "W5": "30",
                         "W6": "44",
                         "W7": "22",
                         "W8": "DS",
                         "7K": "49",
                         "7E": "<unknown>",
                         "7S": "48"}

name: str = input("Please enter your name: ")
form: str = input("Please enter your form: ").upper()
if form not in rooms:
    print("Invalid form! Please enter a valid form.")
    form = input("Please enter your form: ")
print(f"Hello {name}, please go to room {rooms[form]}")
input("[Enter] - Quit")
