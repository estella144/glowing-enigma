charge_rate = 10

current_charge = int(input("current battery charge (%): "))

if current_charge == 100:
    print("full")
elif (current_charge > 100) or (current_charge < 0):
    print("invalid charge %")
else:
    charge_time = (100 - current_charge) * charge_rate
    charge_time_hours = charge_time // 60
    charge_time_minutes = charge_time % 60
    print(f"{charge_time_hours} hours, {charge_time_minutes} minutes to full charge")
