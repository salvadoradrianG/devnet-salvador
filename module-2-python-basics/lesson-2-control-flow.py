"""
Module 2 — Lesson 2: Control Flow (if / elif / else)
Student: [Salvador, Adrian G.]
Date: [9/27/26]

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
Control flow is used to make decisions in a program. 
It allows Python to check a condition and choose what code to run based on the result.
 The if statement checks the first condition. 
 If it is not true, Python can check another condition using elif. 
If none of the conditions are true, else can be used to run another block of code.


============================================
KEY VOCABULARY
============================================
- condition: A rule or situation that Python checks.
- if / elif / else: Statements used to make decisions in a program.
- comparison operator: A symbol used to compare values, such as >, <, ==, and !=.
- boolean expression: An expression that results in True or False.
(add more as needed)


============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

rate = 4

if rate >= 8:
    print("good")
elif rate >= 5:
    print("moderate")
else:
    print("bad")

"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
One mistake I made was using if several times instead
of using elif when I had multiple conditions. 
This can cause more than one condition to be checked separately, 
even when I only wanted one result.


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
"""
