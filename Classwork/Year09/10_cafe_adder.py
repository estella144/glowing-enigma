def process_fees():
    fees_applied = {"take_out": False,
                    "pensioner": False}

    choice = input("Is the order to take out? [Y/N, default: N] ")
    if choice.lower() == "y":
        fees_applied["take_out"] = True

    choice = input("Is the customer a pensioner? [Y/N, default: N] ")
    if choice.lower() == "y":
        fees_applied["pensioner"] = True

    return fees_applied

def create_bill():
    fees = [["take_out", 0.2, "Take out: VAT - 20%"],
            ["pensioner", -0.1, "Pensioner discount - 10%"]]
    items = []
    prices = []

    items_number = int(input("How many items were ordered? "))
    for i in range(0, items_number):
        item_name = input(f"Item {i+1} name: ")
        item_up = float(input(f"Item {i+1} unit price: "))
        item_qty = int(input(f"Item {i+1} quantity: "))
        item_price = item_up * item_qty
        items.append([item_qty, item_name, str(item_price)])

    for i in items:
        prices.append(float(i[2]))

    fees_applied = process_discounts()

    for fee_data in fees:
        if fees_applied[fee[0]]:
            fee_price = round(total * fee[1], 2)
            items.append([1, fee[2], fee_price])
            prices.append(fee_price)

    total = sum(prices)

    # Print receipt
    print("Receipt\n")
    for i in items:
        print(f"{str(i[0])} {i[1]} {i[2]:.2f}")
    print(f"\nTotal: {str(total)}")

if __name__ == "__main__":
    print("Cafe Adder 0.2.0, 21 Sep 2024 - Oliver Nguyen")
    create_bill()
    input("[Enter] - Quit")