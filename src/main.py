from DivisionAlgo import Restoring, NonRestoring

def main():
    """
    This is the main function of the program. It allows the user to perform binary division
    on signed binary numbers using both the Restoring and Non-Restoring algorithms.
    The program runs only for signed binary numbers and can give wrong results for unsigned numbers.
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
                dividend = input("\nPlease enter the signed Binary Number as dividend: ").strip()
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