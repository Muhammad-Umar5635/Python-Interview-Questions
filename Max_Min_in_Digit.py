#Check Max and Min in digit
while True:
    try:
        num = int(input("Enter a number: "))
        if num <= 0:
            raise ValueError
        max_digit = 0
        min_digit = 9
        while num > 0:
            digit = num % 10
            if digit > max_digit:
                max_digit = digit
            if digit < min_digit:
                min_digit = digit
            num //= 10
        print(f"Maximum digit in: {max_digit}")
        
        print(f"Minimum digit in: {min_digit}")
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")