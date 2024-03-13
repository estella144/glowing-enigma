print("Cafe Adder 0.1.0, 6 Mar 2023, by Oliver Nguyen")
print("Test release, First commit")


def create_bill():
    take_out = False
    pensioner = False

    items_number = int(input("How many items were ordered? "))
    items = []
    for i in range(0, items_number):
        item_name = input(f"Item {i+1} name: ")
        item_up = float(input(f"Item {i+1} unit price: "))
        item_qty = int(input(f"Item {i+1} quantity: "))
        item_price = item_up * item_qty
        items.append([item_qty, item_name, str(item_price)])
        
    to = input("Is the order to take out? [Y/N, default: N] ")
    if to.lower() == "y":
        take_out = True

    p = input("Is the customer a pensioner? [Y/N, default: N] ")
    if p.lower() == "y":
        pensioner = True

    prices = []
    for i in items:
        prices.append(float(i[2]))

    total = sum(prices)

    if take_out:
        take_out_fee = round(total * 0.2, 2)
        items.append([1, "Take out: VAT @ 20%", str(take_out_fee)])
        prices.append(take_out_fee)
        total = sum(prices)

    if pensioner:
        pensioner_discount = round(-total * 0.1, 2)
        items.append([1, "Pensioner discount @ 10%", str(pensioner_discount)])
        prices.append(pensioner_discount)
        total = sum(prices)

    # Print receipt
    print("=====RECEIPT=====")
    for i in items:
        print(f"{str(i[0])} {i[1]} {i[2]}")
    print(f"TOTAL {str(total)}")
    input("Press ENTER to finish")

create_bill()
                     
