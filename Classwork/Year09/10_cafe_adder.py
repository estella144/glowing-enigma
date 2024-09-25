def process_fees():
    fees_applied = {"take_out": False,
                    "pensioner": False}

    choice = input("Is the order to take out? [Y/N, default: N] ").lower()
    while choice not in ['y', 'n', '']:
        choice = input("Invalid input. Please enter Y for Yes or N for No: ").lower()
    if choice.lower() == "y":
        fees_applied["take_out"] = True

    choice = input("Is the customer a pensioner? [Y/N, default: N] ").lower()
    while choice not in ['y', 'n', '']:
        choice = input("Invalid input. Please enter Y for Yes or N for No: ").lower()
    if choice.lower() == "y":
        fees_applied["pensioner"] = True

    return fees_applied

def create_bill():
    fees = [["take_out", 0.2, "Take out: VAT - 20%"],
            ["pensioner", -0.1, "Pensioner discount - 10%"]]
    items = []
    prices = []

    items_number = int(input("How many items were ordered? "))
    while items_number <= 0:
        items_number = int(input("Invalid number. Please enter a positive, nonzero number of items: "))
    for i in range(0, items_number):
        item_name = input(f"Item {i+1} name: ").strip()
        while not item_name:
            item_name = input("Item name cannot be empty. Please enter a valid name: ").strip()

        item_up = float(input(f"Item {i+1} unit price: "))
        while item_up < 0:
            item_up = float(input("Invalid price. Please enter a positive price: "))

        item_qty = int(input(f"Item {i+1} quantity: "))
        while item_qty <= 0:
            item_qty = int(input("Invalid quantity. Please enter a positive quantity: "))

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
    print(f"\nTotal: {total:.2f)}")

if __name__ == "__main__":
    print("Cafe Adder 0.2.1, 25 Sep 2024 - Oliver Nguyen")
    create_bill()
    input("[Enter] - Quit")
