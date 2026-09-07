# Ask the user to input a number and convert it to an integer
x = int(input("input a number: ")) 

# Check if the number is divisible by 2 with no remainder
if x % 2 == 0: 
    print("The number is even")
# If there is a remainder, the number is odd
else: 
    print("The number is odd")

