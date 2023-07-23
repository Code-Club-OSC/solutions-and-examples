# You must remember that input returns a STRING.
# You cannot peform maths operations on STRINGS because Python considers them words, not numbers.
# We have to convert the input to numbers by placing input() inside int() which converts to an integer
first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
operation = input("Enter an operator (+,-,*,/): ")

# Standard if/elif conditions
if operation == '+':
    print(first_number + second_number)
# elif statements will only execute if the previous statement is false
elif operation == '-':
    print(first_number - second_number)
elif operation == '*':
    print(first_number * second_number)
elif operation == '/':
    print(first_number / second_number)
# If the user has entered an invalid operation then quit the program with a helpful message tagged onto it
else:
    quit("You need to enter a valid operation!")