from DivisionAlgo import Restoring, NonRestoring
from utils import Hexadecimal

def main():
    """
    This is the main function of the program. It takes user input for two binary signed numbers.
    This program run for the signed binary numbers only
    """
    print("\nWelcome to the Binary Divison Program for the Signed number\n")

    exit = False
    while(not(exit)):
        print("Binary Divsion Simulator")
        print(" 1. Binary Division")
        print(" 2. Quit\n")

        choice = input("Please enter your choice: ").strip()

        if choice == '2':
            exit = True
            break
        elif choice != '1': #check for the valid choice
            print("\nPLEASE ENTER A VALID CHOICE\n")
            continue
        else:
            try:
                dividend = input("\nPlease enter the signed Binary Number as dividend: ").strip() #Take input from user
                divisor = input("Enter the signed Binary Number as divisor: ").strip()

                D1 = Restoring(str(dividend), str(divisor))
                D1.displayResult()
                D2 = NonRestoring(str(dividend), str(divisor))
                D2.displayResult()

            except (ValueError, IndexError):
                print("\nNo Reult for the invalid inputs. Please enter only a valid binary number\n")
                continue

if __name__ == "__main__":
    main()