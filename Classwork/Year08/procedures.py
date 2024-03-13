def welcome():
    name = input("What is your name? ")
    print(f"Hello {name}, welcome to my quiz")
    return name

def goodbye(name):
    print(f"Goodbye {name}")

def quiz():
    current_idx = 0
    questions = ["What data type is True or False? ",
                 "What data type is a whole number? ",
                 "What does the '=' symbol do? "]
    answers = ["boolean",
               "integer",
               "assignment"]
    for i in questions:
        answer = input(questions[current_idx]) 
        if answer == answers[current_idx]: 
            print("correct") 
        else: 
            print("wrong")
        current_idx += 1

name = welcome() 
repeat = "yes" 
while repeat == "yes": 
    quiz() 
    repeat = input("Try again?") 
goodbye(name)
