#Advanced topics in python
"""
summary
*Regular expression
*Generators and iterators
*Decorators
*Context managers
*Multithreading and multiprocessing
"""
# Regular 
# Regular expressions (regex) in Python are powerful tools for pattern matching and manipulating strings
"""
summary
\d: matches any digit (0-9)
\w: matches any alpanumeric character (0-9, a-z, A-Z, and other underscores)
\s: matches any whitespace character (space, tab, newline)
.: matches any character except a newline
^: matches the beginning of a line
$: matches the end of a line
"""

#Example1
import re

text = "I have 5 apples and 2 oranges."

# Matching digits
digits = re.findall(r"\d", text)
print(digits)  # Output: ['5', '2']

# Matching non-digits
non_digits = re.findall(r"\D", text)
print(non_digits)  # Output: ['I', ' ', 'h', 'a', 'v', 'e', ' ', ' ', 'a', 'p', 'p', 'l', 'e', 's', ' ', 'a', 'n', 'd', ' ', ' ', 'o', 'r', 'a', 'n', 'g', 'e', 's', '.']

# Matching word characters
word_chars = re.findall(r"\w", text)
print(word_chars)  # Output: ['I', 'h', 'a', 'v', 'e', '5', 'a', 'p', 'p', 'l', 'e', 's', 'a', 'n', 'd', '2', 'o', 'r', 'a', 'n', 'g', 'e', 's']

# Matching non-word characters
non_word_chars = re.findall(r"\W", text)
print(non_word_chars)  # Output: [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '.']

# Matching whitespace characters
whitespace_chars = re.findall(r"\s", text)
print(whitespace_chars)  # Output: [' ', ' ', ' ', ' ', ' ', ' ']

# email validation

def validate_email(email):
    pattern= r'^[\w\.\-]+@[\w\.\-]+.\w$'
    if re.match(pattern, email):
        return True
    else:
        return False
    
email = input("Enter your email: ")
if validate_email(email):
    print("Valid email")

print(validate_email(email))


# Generators and iterators
# generators
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
        yield result

# Using the generator function
factorial_gen = factorial(5)

# Iterating over the generator using a for loop
for num in factorial_gen:
    print(num)
