discounts = [["PVFC7", 10],
             ["CPU5", 5],
             ["BGF2", 15]]

def check_discount(price, code):
    new_price = price
    size = len(discounts) - 1
    for i in range(0, size):
        if discounts[i][0] == code:
            new_price = price - discounts[i][1]
    return new_price

final_item_prices = []
item_price = int(input("Item price (or 0 to finish): "))

while item_price != 0:
    discount_code = input("Discount code: ")
    final_item_prices.append(check_discount(item_price, discount_code))
    item_price = int(input("Item price (or 0 to finish): "))

print(f"Total: {sum(final_item_prices)}")
