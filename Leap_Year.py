# Find a leap year

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
try:
    year = int(input("Enter a year: "))
    if year < 0:
        raise ValueError
    if is_leap(year):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
except ValueError:
    print("Invalid input. Please enter a valid year.")