# Homework 2: Control Structures and Numerical Computation

# Problem 1: Classifying Numbers
def describe(n):
    """
    Classifies the integer n as 'positive' or 'negative' and 
    as 'large' or 'small'. Returns a string containing both classifications.
    """
    # Determine if the number is positive or negative
    if n >= 0:
        sign = "positive"
    else:
        sign = "negative"
    
    # Determine if the number is large or small
    if abs(n) >= 1000:
        size = "large"
    else:
        size = "small"
    
    return sign + " " + size

# Problem 2: Leap Year Determination
def is_leap_year(year):
    """
    Determines if the given year is a leap year based on the following conditions:
    - A year is a leap year if it is divisible by 4.
    - If the year is also divisible by 100, it must also be divisible by 400.
    Returns True if it is a leap year, otherwise False.
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True  # Divisible by 400 -> Leap year
            else:
                return False  # Divisible by 100 but not 400 -> Not a leap year
        else:
            return True  # Divisible by 4 but not 100 -> Leap year
    else:
        return False  # Not divisible by 4 -> Not a leap year

# Problem 3: Income Tax Calculation
def tax(income):
    """
    Computes the tax for a given income based on the U.S. tax brackets.
    The tax is calculated incrementally based on the defined income ranges.
    """
    # Tax brackets
    brackets = [
        (9875, 0.10),
        (40125, 0.12),
        (85525, 0.22),
        (163300, 0.24),
        (207350, 0.32),
        (518400, 0.35),
        (float('inf'), 0.37)
    ]
    
    tax_amount = 0 
    previous_bracket = 0  # Track previous income bracket

    for bracket, rate in brackets:
        if income > bracket:
            tax_amount += (bracket - previous_bracket) * rate
            previous_bracket = bracket
        else:
            tax_amount += (income - previous_bracket) * rate
            break  # No need to process further brackets

    return round(tax_amount, 2)

# Problem 4: Square Root Approximation
def square_root(n, tolerance):
    """
    Approximates the square root of n using the Babylonian method (Heron's method).
    Iterates until the absolute difference between x^2 and n is within the tolerance.
    """
    x = n  # Initial guess
    while abs(x * x - n) >= tolerance:
        x = (x + n / x) / 2 
    return x

# Problem 5: Collatz Sequence
def collatz(n):
    """
    Computes the number of steps required for n to reach 1 following the Collatz sequence.
    If n is even: n -> n/2
    If n is odd: n -> 3n + 1
    """
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2  # Even case: Divide by 2
        else:
            n = 3 * n + 1  # Odd case: Multiply by 3 and add 1
        steps += 1 
    return steps
