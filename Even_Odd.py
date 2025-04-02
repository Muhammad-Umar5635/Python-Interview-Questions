# Check the numner is odd or even
while True:
    try:
        num = int(input("Enter a number: "))
        if num < 0:
            raise ValueError
        if num % 2 == 0:
            print(f"{num} is even.")
        else:
            print(f"{num} is odd.")
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")