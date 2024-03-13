def process_input(str_in):
    if str_in.lower() == "y":
        return True
    else:
        return False

def decide(attendance):
    harminder = attendance[0]
    manisha = attendance[1]
    gemma = attendance[2]
    
    if (not harminder or (manisha and gemma)):
        return True
    else:
        return False

def check():
    harminder = process_input(input("Is Harminder coming? [Y/N] "))
    manisha = process_input(input("Is Manisha coming? [Y/N] "))
    gemma = process_input(input("Is Gemma coming? [Y/N] "))
    return [harminder, manisha, gemma]

def main():
    attendance = check()
    decision = decide(attendance)
    if decision:
        print("Coming to the concert")
    else:
        print("Not coming to the concert")

def test():
    print("H M G Decision")
    for i in range(0, 2):
        for j in range(0, 2):
            for k in range(0, 2):
                result = decide([i, j, k])
                print(f"{i} {j} {k} {result}")

if __name__ == "__main__":
    main() # Or test(), for testing
