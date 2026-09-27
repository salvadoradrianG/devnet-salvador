
"""
Module 2 — Lesson 4: Functions
Student: [Salvador, Adrian G.]
Date: [9/27/2026]

============================================
WHAT IS THIS TOPIC? 
============================================
A function is a reusable block of code that is made
to perform a specific task. Instead of writing the same
code many times, we can put it inside a function and
call the function whenever we need it.

A function can receive information, process it, and
return a result. In Python, we create a function using
the "def" keyword.


============================================
KEY VOCABULARY
============================================
- function: A reusable block of code that performs a
  specific task.

- def: A Python keyword used to create or define a
  function.

- parameter: A variable written inside the parentheses
  of a function definition that receives a value.

- argument: The actual value given to a parameter when
  the function is called.

- return: Sends a value or result back from a function.

- function call: Using the function to run the code
  inside it.
============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

# --- your code example goes here ---

def coffee_total(price, quantity):
    total = price * quantity
    return total


price = 150
quantity = 3

total_price = coffee_total(price, quantity)

print("Price:", price)
print("Quantity:", quantity)
print("Total:", total_price)


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
One mistake I want to avoid is confusing a parameter
with an argument. A parameter is the variable used
when defining the function, while an argument is the
actual value given to the function when it is called.

============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
Functions connect to loops and lists because we can
use functions to process items from a list or perform
the same task repeatedly. This can make a program
more organized and easier to reuse.
"""