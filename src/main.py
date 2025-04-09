import DivisionAlgo
from DivisionAlgo import Restoring, NonRestoring
from utils import Hexadecimal

def main():
    """
    This is the main function of the program. It takes user input for two binary signed numbers.
    This program run for the signed binary numbers only.
    """
    print("\nWelcome to the Binary Divison Program for the Signed number")
    print("This program is only for signed binary numbers")

    dividend = str(input("\nPlease enter the signed Binary Number as dividend: "))#Take input from user
    divisor = str(input("Enter the signed Binary Number as divisor: "))

    print("\nRunning the Program......\n")

    D1 = Restoring(dividend, divisor)
    D1.displayResult()

    print()
    D2 = NonRestoring(dividend, divisor)
    D2.displayResult()

if __name__ == "__main__":
    main()