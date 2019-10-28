"""
Use a stack to check whether or not a string
has balanced usage of parenthesis.
Example:
    (), ()(), (({[]}))  <- Balanced.
    ((), {{{)}], [][]]] <- Not Balanced.
Balanced Example: {[]}
Non-Balanced Example: (()
Non-Balanced Example: ))
"""

# comment code with instance creation i stack_ex.py file
from stack_ex import Stack

def is_match(p1, p2):
    return (p1 == "(" and p2 == ")") or (p1 == "[" and p2 == "]") or (p1 == "{" and p2 == "}")

def is_parantesis_balanced(parenthesis_str):
    s = Stack()
    is_balanced = True
    index = 0

    while index < len(parenthesis_str) and is_balanced:
        parenthesis = parenthesis_str[index]
        if parenthesis in "[({":
            s.push(parenthesis)
        else:
            if s.is_empty():
                is_balanced = False
            else:
                top = s.pop()
                if not is_match(top, parenthesis):
                    is_balanced = False
        index += 1
        

    return s.is_empty() and is_balanced

print(is_parantesis_balanced("({[]})"))