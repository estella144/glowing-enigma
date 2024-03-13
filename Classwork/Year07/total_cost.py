subscriptions = {"a": 4.99,
                 "b": 6.99,
                 "s": 10.99,
                 "p": 15.99}
def main():
    global subscriptions
    
    print("Basic with [A]dverts\n[B]asic\n[S]tandard\n[P]remium")
    sub_type = input("What type of Netflix subscription did you purchase? ").lower()
    sub_type = sub_type[0]

    price = 0
    
    try:
        price = subscriptions[sub_type]
    except KeyError:
        print("Invalid subscription")
    
    year_price = price * 12
    print(f"This year, your subscription will cost: {str(year_price)}")
    main()

main()

    
