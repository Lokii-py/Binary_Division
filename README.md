# Binary Division Simulator
This repository implements Restoring and Non-Restoring Division algorithms in Python for binary signed numbers. It simulates step-by-step binary division using custom utility functions and visual output to better understand low-level division logic used in computer architecture.

# Features
- Signed binary division with sign bit handling
- Restoring Division Algorithm
- Non-Restoring Division Algorithm
- Binary to Hexadecimal output
- Overflow detection
- Operation and iteration counters
- Execution time tracking

# File Structure
main.py: Contains the implementation of Division, Restoring, and NonRestoring classes.
utils.py: Contains helper functions for bitwise operations like:
shiftLeft
subtractBinary
addBinary
checkOverflow
restore
sequenceCounter
Hexadecimal

# How It Works
Input
Each division method takes:
dividend: Signed binary string (e.g., 01101)
divisor: Signed binary string (e.g., 00011)

Output
The program displays:

Quotient (binary and hexadecimal)
Remainder (binary and hexadecimal)
Number of arithmetic operations
Total iterations
Execution time

**Restoring Method**
Left shift combined accumulator and quotient
Subtract divisor from accumulator
If result is negative, restore previous value
Repeat until counter ends

**Non-Restoring Method**
Left shift combined accumulator and quotient
Subtract or add divisor based on accumulator sign
Update quotient accordingly
Repeat until counter ends

Example

dividend = "01101"  # +13 in binary
divisor = "00011"    # +3 in binary

r = Restoring(dividend, divisor)
r.displayResult()

nr = NonRestoring(dividend, divisor)
nr.displayResult()

# Requirements
Python 3.x
Make sure utils.py is present in the same directory.

This project is open-source and free to use under the MIT License.