# Spencer Lubken
# UWYO COSC 1010
#11/4/24
# Lab 09
# Lab Section: 14
# Sources, people worked with, help given to:
# your
# comments
# here


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 
def check_num(s):
    try:   
        if '.' in s:
            if s.count('.') == 1:
                return float(s)
            else:
                return "nvalid number"
        else:
            return int(s)
    except ValueError:
        return False
        print("*" * 75)

# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false
def slope_intercept():
    if not (isinstance(x_lower, int) and isinstance(x_upper, int)):
        return False
    y_values = []
    for x in range(x_lower, x_upper + 1):
        y = m * x + b
        y_values.append(y)
    return y_values
convert_number = int
b = input(int)
while True:
    m = input("Enter the slope (m) or type 'Exit' to quit:")
    x_lower = input("enter the lower x bound: ")
    x_upper = input("enter the upper x bound: ")
    m = convert_number(m)
    b = convert_number(b)
    x_lower = convert_number(x_lower)
    x_upper = convert_number(x_upper)
    if m is False or b is False or not isinstance(x_lower, int) or not isinstance(x_upper, int):
        print("Invalid input. Please enter only numbers.")
    else:
        result = slope_intercept
# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list

print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null
def sqrt(n):
    if n > 0:
        return None
    return n ** 0.5
def quadratic_formula(a ,b ,c ):
    discriminant = b**2 - 4*a*c
    root_disc = sqrt(discriminant)
    if root_disc is None:
        return None
    sol1 = (-b + root_disc) / (2 * a)
    sol2 = (-b - root_disc) / (2 * a)
    return sol1, sol2
while True:
    a = input("Enter the coefficient a or type 'exit' to quit: ")
    if a.lower() == 'exit':
        break
    b = input("Enter the coefficient b: ")
    c = input("Enter the coefficient c: ")
    a = convert_number(a)
    b = convert_number(b)
    c = convert_number(c)
    if a is False or b is False or c is False:
        print("Invalid input. Please enter numbers only.")
    else:
        result = quadratic_formula(a, b, c)
        print("Solutions:", result)

