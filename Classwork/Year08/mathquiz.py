from random import randint

restart = ""
score = 0

print("Welcome to Oliver's Maths Quiz!")
print("Can you get a good score?")
input("[ENTER=Continue]")

while restart.lower() != "n":
    score = 0
    for i in range(5):
        op = randint(1,3)
        if op == 1:
            a1 = randint(1,100)
            a2 = randint(1,100)
            correct_ans = a1 + a2
            ans = int(input(f"{a1} + {a2} = "))
        elif op == 2:
            a1 = randint(1,12)
            a2 = randint(1,12)
            correct_ans = a1 * a2
            ans = int(input(f"{a1} * {a2} = "))
        elif op == 3:
            a1 = 0
            a2 = 0
            while a1 <= a2:
                a1 = randint(1,100)
                a2 = randint(1,100)
            correct_ans = a1 - a2
            ans = int(input(f"{a1} - {a2} = "))
        
        if ans == correct_ans:
            score += 1
            print(f"Correct! Score: {score}")
        else:
            print(f"Incorrect. Correct answer was: {correct_ans}")
    print(f"Congratulations, you scored {score}/5")
    restart = input("Do you want to restart and try to beat your score? [y/n]")
    
input("Thank you for playing, goodbye [ENTER=Quit]")
