def bin8(number):
    """Q: Why does this exist? A: JJW didn't want me to use builtins..."""
    out = ""
    power = 128
    
    for i in range(8):
        if number >= power:
            out += "1"
            number -= power
        else:
            out += "0"
        power = power / 2

    return out
            
def dec_to_bin(number):
    if number > 255:
        return "Number too high! [0-255 expected]"
    if number < 0:
        return "Number too low! [0-255 expected]"
    return bin8(number)

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
