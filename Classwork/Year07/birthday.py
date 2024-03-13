from datetime import date

year_of_birth = int(input("What year were you born? "))
current_year = date.today().year
years = current_year - year_of_birth

current_year = str(current_year)
years = str(years)

print("The year is " + current_year + ". You will turn " + years + " this year.")
input("Press enter to quit")
