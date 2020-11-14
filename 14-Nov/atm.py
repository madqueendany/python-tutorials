
# Using while to get a valid input

# define a variable called balance
# Assign a value in balance
# Ask the user for a number, 
# If number is greater than balance
# Print an error and ask user
# to enter another number

balance = 10000.0

number = input("Hello, Enter number: ")
number = float(number)

while(number > balance):
  number = input("You've entered a value higher than the balance! Enter another number: ")
  number = float(number)
