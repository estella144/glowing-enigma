price = float(input("Please enter price: "))
vat = round(price * 0.2)
total_price = price + vat
print(f"VAT: {vat:.2f}, total price: {total_price:.2f}")
