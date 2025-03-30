import utils
from utils import checkOverflow, shiftLeft, subtractBinary, restore, sequenceCounter, addBinary

class Restoring:
    def __init__(self, dividend, divisor):
        """
        Initializes the Restoring Division instance with the given binary dividend and divisor.
        
        Arguments:
        dividend (str): The binary dividend for the division.
        divisor (str): The binary divisor for the division.
        """
        self.dividend = "0" + dividend  # Add a leading zero for proper two's complement handling
        self.divisor = "0" + divisor  # Add a leading zero for proper two's complement handling
        self.quotient = dividend  # Initialize quotient with the dividend
        self.accum = "0" * len(self.dividend)  # Initialize the accumulator with zeros
        self.iteration_count = 0  # Count the number of iterations
        self.operation_count = 0  # Count the number of binary operations (additions/subtractions)

    def run(self):
        """
        Runs the Restoring Division Algorithm to divide the binary dividend by the binary divisor.
        
        The algorithm works by shifting the accumulated value and performing subtraction, followed by
        restoration if needed, until the division is complete.
        """
        # Perform the overflow check
        print("Checking overflow...")
        if not checkOverflow(self.dividend, self.divisor):
            print("Overflow detected. Cannot proceed.")
            return
        else:
            print("No overflow detected.")

        print("Running the Restoring Division Method...")

        sequence_counter = True
        while sequence_counter:
            # Update the number of iterations
            self.iteration_count += 1

            # Perform shift operation (shift left the combined accumulator and quotient)
            combined = self.accum + self.quotient
            shifted = shiftLeft(combined)

            operation1 = shifted  # Store the shifted value for the restore operation

            # Extract the part of the shifted number that should be subtracted from the divisor
            self.Remainder = shifted[:(len(self.quotient) + 1)]  # Add 1 to quotient length

            # Perform subtraction with the divisor
            subtracted = subtractBinary(self.Remainder, self.divisor)
            self.operation_count += 1  # Increment the operation count for the subtraction

            # Prepare for the restore operation (if needed)
            operation2 = subtracted + operation1[len(subtracted):]

            # Check the most significant bit (MSB) of the result after subtraction
            if int(subtracted[0]) == 1:
                # If MSB is 1, restore the original value (as the result was negative)
                operation1 = restore(operation1)
                # Update the quotient and accumulator after the restore
                self.quotient = operation1[len(self.dividend):]
                self.accum = operation1[:-len(self.quotient)]
            else:
                # If MSB is 0, update the quotient and accumulator without restoring
                operation2 += "1"
                self.quotient = operation2[len(self.dividend):]
                self.accum = operation2[:-len(self.quotient)]

            # Update the remainder (excluding the sign bit)
            self.rem = self.accum[1:]

            # Continue the loop until the maximum number of iterations is reached
            sequence_counter = sequenceCounter((len(self.divisor) - 1), self.iteration_count)

    def displayResult(self):
        """
        Displays the quotient and remainder of the division in binary format.
        """
        print("Quotient: ", self.quotient)
        print("Remainder: ", self.rem)
        print("Number of Subtraction performed: ", self.operation_count)

#debug
c1 = Restoring("1111", "0011")
c1.run()
c1.displayResult()


class NonRestoring:
    def __init__(self, dividend, divisor):
        return -1
    