from time import sleep

start_number = int(input("Number to start at: "))
for i in range(start_number, -1, -1):
    print(i)
    if i > 0:
        sleep(1)
    else:
        print("COUNTDOWN DONE!")

input("Press [Enter] to finish")
