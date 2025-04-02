# Check if a number is a palindrome
def is_palindrome(s):
    return str(s) == str(s)[::-1]

result = is_palindrome(888)
print(f"888 is a palindrome: {result}")

# Check if a given input is a polindrome
def is_palindrome(s):
    return s == s[::-1]

UserInput = input("Enter a string: ")
result = is_palindrome(UserInput)
print(f"{UserInput} is a palindrome: {result}")