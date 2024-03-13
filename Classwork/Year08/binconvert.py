def dec_to_bin(number):
    return bin(number).split(sep="b")[1]

def bin_to_dec(number):
    return int(number, base=2)

def main():
    while True:
        choice = input("1. DEC to BIN\n2. BIN to DEC\nConversion no.: ")
        number = input("Number to convert: ")
        try:
            if choice == "2":
                print(bin_to_dec(number))
            else:
                print(dec_to_bin(int(number)))
        except ValueError:
            print("invalid number!")

main()
