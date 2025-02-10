import csv
import os
import random
import re
from time import sleep

savefile = "rpssave.csv"
prohibited_name_regex = ","

def get_name() -> str:
    print("Welcome to Rock, Paper, Scissors")
    print("Please enter your username to begin.")
    print("Warning: This username is case sensitive.")
    name = input()
    while re.findall(prohibited_name_regex, name):
        print("That name is not allowed due to technical reasons.")
        name = input("Please enter another username: ")
    return name

def get_high_score(name) -> int:
    if not os.path.isfile(savefile):
        with open(savefile, 'x') as f:
            print("No savefile found. New savefile created.")
    
    with open(savefile) as csvfile:
        reader = csv.reader(csvfile)
        savedata = list(reader)
        player_games = [game for game in savedata if len(game) > 0 and game[0] == name]
        if not player_games:
            return -1
        player_scores = [int(game[1]) for game in player_games]
        return max(player_scores)

def save_score(username, score) -> None:
    fields = [username, score]
    with open(savefile, 'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(fields)
    print("Data successfully saved")

def print_tutorial(name) -> None:
    print(f"\nWelcome, {name}, to Rock, Paper, Scissors!")
    sleep(1)
    print("The rules of this game are simple.")
    print("You make a move: rock, paper or scissors.")
    sleep(2)
    print("Paper beats rock,")
    sleep(1)
    print("Rock beats scissors,")
    sleep(1)
    print("But scissors beats paper.")
    sleep(1)
    print("The player who beats their opponent with their move wins.")
    sleep(2)
    print(f"Good luck, {name}!\n")
    sleep(1)
    print("Do you wish to continue?")
    input("Press [Enter] to start playing, or [Ctrl-C] to quit.")

def main_loop() -> int:
    score = 0
    choices = ["R", "P", "S"]
    full_choices = {"R": "Rock", "P": "Paper", "S": "Scissors"}
    defeated = False

    while not defeated:
        player_move = ""
        try:
            player_move = input("Make a move: [R]ock, [P]aper, [S]cissors. ")[0].upper()
        except IndexError:
            player_move = ""
        while player_move not in choices:
            print("Invalid move")
            try:
                player_move = input("Make a move: [R]ock, [P]aper, [S]cissors.")[0].upper()
            except IndexError:
                player_move = ""
        opponent_move = random.choice(choices)
        print(f"Opponent chose: {full_choices[opponent_move]}")
        player_victory = (player_move == "R" and opponent_move == "S") \
                         or (player_move == "S" and opponent_move == "P") \
                         or (player_move == "P" and opponent_move == "R")
        tie = (player_move == opponent_move)
        
        if player_victory:
            score += 1
            print("You won!")
            print(f"Your score is now: {score}")
            try:
                next_round = input("Next round? [Y/N, default: Y]")[0].upper()
            except IndexError:
                next_round = "Y"
            if next_round == "N":
                defeated = True
        elif tie:
            print("Tie!")
            print(f"Your score is: {score}")
            try:
                next_round = input("Next round? [Y/N, default: Y]")[0].upper()
            except IndexError:
                next_round = "Y"
            if next_round == "N":
                defeated = True
        else:
            print("You lost!")
            defeated = True
    return score
 
def main() -> None:
    name = get_name()
    high_score = get_high_score(name)
    play_again = "Y"

    if high_score == -1:
        # Placeholder value for new player
        print_tutorial(name)
    else:
        print(f"Welcome back, {name}.")
        print(f"Your current high score is {high_score}.")
        print("Do you wish to continue?")
        input("Press [Enter] to start playing, or [Ctrl-C] to quit.")

    while play_again == "Y":
        score = main_loop()
        print("Game over!")
        if score > high_score:
            print("New high score attained")
        print(f"Your final score is: {score}")
        try:
            save = input("Save score? [Y/N, default: Y]")[0].upper()
        except IndexError:
            save = "Y"
        if save == "Y":
            save_score(name, score)
        try:
            play_again = input("Play again? [Y/N, default: N]")[0].upper()
        except IndexError:
            play_again = "N"

    print("All data has been saved")
    input("Press [Enter] to quit")

if __name__ == "__main__":
    main()
