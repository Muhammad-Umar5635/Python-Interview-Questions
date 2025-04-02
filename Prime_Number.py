# Check the given number is prime number
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
try:
    num = int(input("Enter a number: "))
    if is_prime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")
except ValueError:
    print("Invalid input. Please enter a valid number.")

# Give the prime number in a given range
while True:
    try:
        User_Input = int(input("Enter a number: "))
        if User_Input > 0:
            break
    except ValueError:
        print("Invalid input. Please enter a valid number.")
print("Prime numbers between 1 and", User_Input, "are:", end=" ")
for i in range(2, User_Input + 1):
    if is_prime(i):
        print(i , end=" ")