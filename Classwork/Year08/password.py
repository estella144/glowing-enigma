import hashlib
PASSWORD_HASH = 'd9201d3705a24a4fe403920bb2cf2a4d933676f68f6eff90015a46f9693d2d0d'
correct = False

def check_password(guess):
    global PASSWORD_HASH

    guess_bytes = bytes(guess, "utf-8")
    guess_hash = hashlib.sha256(guess_bytes).hexdigest()
    if guess_hash == PASSWORD_HASH:
        return True
    else:
        return False

guess = input("Enter password: ")
correct = check_password(guess)

while not correct:
    print("Incorrect password!")
    guess = input("Enter password: ")
    correct = check_password(guess)

print("Correct password. Welcome, comrade!")
