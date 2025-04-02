# Give the list of factorial of a given number
while True:
    try:
        User_Input = int(input("Enter a number: "))
        if User_Input > 0:
            break
    except ValueError:
        print("Invalid input. Please enter a valid number.")
print("Factorial of", User_Input, "is:", end=" ")
factorial = 1
for i in range(1, User_Input + 1):
    factorial *= i
print(factorial , end=" ")
