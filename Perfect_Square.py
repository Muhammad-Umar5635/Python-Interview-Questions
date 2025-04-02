# Check the numbe is perfect square
def is_perfect_square():
    while True:
        try:
            num = int(input("Enter a number: "))
            if num < 0:
                raise ValueError
            if num**0.5 == int(num**0.5):
                print(f"{num} is a perfect square.")
            else:
                print(f"{num} is not a perfect square.")
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

is_perfect_square()

#Give the list of perfect square in a given range
while True:
    try:
        User_Input = int(input("Enter a range you want to print perfect square: "))
        if User_Input > 0:
            break
    except ValueError:
        print("Invalid input. Please enter a valid number.")
print("Perfect squares between 1 and", User_Input, "are:", end=" ")
for i in range(1, User_Input + 1):
    if i**0.5 == int(i**0.5):
        print(i , end=" ")