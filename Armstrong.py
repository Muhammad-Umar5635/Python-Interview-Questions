#Check the Given number is Armstrong number
while True:
    try:
        num = int(input("Enter a number: "))
        if num < 0:
            raise ValueError
        sum = 0
        lenght = len(str(num))
        for i in str(num):
            sum += int(i)**lenght
        if sum == num:
            print(f"{num} is an Armstrong number.")
        else:
            print(f"{num} is not an Armstrong number.")
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Gvie the List of Armstrong Number in a given range
while True:
    try:
        User_Input = int(input("Enter a number: "))
        if User_Input > 0:
            break
    except ValueError:
        print("Invalid input. Please enter a valid number.")
print("Armstrong numbers between 1 and", User_Input, "are:", end=" ")
def is_armstrong(n):
    sum = 0
    lenght = len(str(n))
    for i in str(n):
        sum += int(i)**lenght
    if sum == n:
        return True
    else:
        return False
for i in range(1, User_Input + 1):
    if is_armstrong(i):
        print(i , end=" ")