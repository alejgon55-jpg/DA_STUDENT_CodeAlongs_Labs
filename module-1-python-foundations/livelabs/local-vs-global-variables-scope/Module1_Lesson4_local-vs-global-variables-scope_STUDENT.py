#!/usr/bin/env python3
"""Day 4 code-along: Local vs. Global Variables & Scope. Run: python3 <file>"""

# ===== 1. Local Scope, Live =====
<<<<<<< HEAD
# Find out whether a variable made inside a function still exists outside of
# it.
# This is supposed to raise NameError: run it, read the traceback, then comment
# out the raising line so the rest of the file runs.
#
# DISCUSS: Before you run the Local Scope code, put these in the order they
#          happen. A: total stops existing. B: make_total() is called. C: total
#          is created and set to 100.
# Your answer: B, C, A
=======
# Find out if a variable made inside a function exists outside it.
# TODO: run it, read the NameError, then comment out the raising line
# DISCUSS: Order: A: total disappears. B: make_total() runs. C: total = 100.
# Your answer:
>>>>>>> upstream/main
#
print('----- 1. Local Scope, Live -----')
# TODO: define make_total(): set a local total to 100 and return it
# TODO: print total outside the function and see what happens

<<<<<<< HEAD
num_val = 0 #global

def make_total(): 
    total = 100 #local variable
    return total * num_val
    #print(total) 

x = make_total()
print(x)


# DISCUSS: Now try a new function. set_x() runs and sets x = 5 inside it, but
#          print(x) outside raises NameError. Why?
=======
# DISCUSS: set_x() sets x = 5, but print(x) outside raises NameError. Why?
>>>>>>> upstream/main
# Your answer:
#


# ===== 2. Reading a Global, Live =====
# Price a $100 item with 8% tax, using a tax rate stored outside the function.
print('----- 2. Reading a Global, Live -----')
# TODO: define tax_rate as a global
# TODO: write price_with_tax(price) that reads tax_rate directly

<<<<<<< HEAD
tax_rate = .08 #0.08875 NYS Tax

def price_with_tax(price):
    x = price + (price * tax_rate)
    return x

print(price_with_tax(5.00))
print(price_with_tax(100.00))
# DISCUSS: Copy the price_with_tax function from the Reading a Global code into
#          a new file, without the tax_rate = 0.08 line. It worked here. Why
#          does it break there?
=======
# DISCUSS: Move price_with_tax to a file with no tax_rate. Why does it break?
>>>>>>> upstream/main
# Your answer:
#


# ===== 3. Refactor: Global to Parameter =====
# Pass the tax rate in as a parameter. It should still print 108.0.
print('----- 3. Refactor: Global to Parameter -----')
# TODO: rewrite price_with_tax to take tax_rate as a parameter
tax_rate = 0.08

def price_with_tax(price, tax_rate):
    return price + (price * tax_rate)

print(price_with_tax(20, tax_rate )) 