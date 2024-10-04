import random

print("Two Dice v0.1.0 (3 Oct 2024) - Oliver Nguyen")
input("Press [Enter] to roll")

die_1 = random.randint(1, 6)
die_2 = random.randint(1, 6)

if die_1 != die_2:
    score = die_1 + die_2
else:
    # At this point, die_1 == die_2.
    if die_1 == 6:
        score = 0
    else:
        score = 2 * (die_1 + die_2)

print(f"You rolled: {die_1} and {die_2}")
print(f"Score: {score}")
input("Press [Enter] to finish")
