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
        self.accum = "0" * len(self.divisor)  # Initialize the accumulator with zeros
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

        # Special case: if the dividend's length is twice the divisor's length minus 1
        if len(self.dividend) - 1 == 2 * (len(self.divisor) - 1):
            self.accum = "0"

        sequence_counter = True
        while sequence_counter:
            # Update the number of iterations
            self.iteration_count += 1

            # Perform shift operation (shift left the combined accumulator and quotient)
            combined = self.accum + self.quotient
            shifted = shiftLeft(combined)
            operation1 = shifted  # Store the shifted value for the restore operation

            # Extract the remainder portion for subtraction
            self.Remainder = shifted[:len(self.divisor)]

            # Perform subtraction
            subtracted = subtractBinary(self.Remainder, self.divisor)
            self.operation_count += 1  # Increment the subtraction count

            # Prepare for potential restore operation
            operation2 = subtracted + operation1[len(subtracted):]

            # Check the most significant bit (MSB) to determine restoration
            if int(subtracted[0]) == 1:
                # Restore if subtraction resulted in a negative value (MSB = 1)
                operation1 = restore(operation1)
                self.quotient = operation1[len(self.divisor):]
                self.accum = operation1[:-len(self.quotient)]
            else:
                # No restore needed, update values and set quotient bit to 1
                operation2 += "1"
                self.quotient = operation2[len(self.divisor):]
                self.accum = operation2[:-len(self.quotient)]

            # Continue until the sequence counter indicates completion
            sequence_counter = sequenceCounter((len(self.divisor) - 1), self.iteration_count)

        # Extract and print the final remainder (ignoring the sign bit)
        self.rem = self.accum[1:]

    def displayResult(self):
        """
        Displays the quotient and remainder of the division in binary format.
        """
        print("Quotient: ", self.quotient)
        print("Remainder: ", self.rem)
        print("Number of Subtraction performed: ", self.operation_count)


class NonRestoring:
    def __init__(self, dividend, divisor):
        self.dividend = "0" + dividend  # Add a leading zero for proper two's complement handling
        self.divisor = "0" + divisor  # Add a leading zero for proper two's complement handling
        self.quotient = dividend  # Initialize quotient with the dividend
        self.accum = "0" * len(self.divisor)  # Initialize the accumulator with zeros
        self.iteration_count = 0  # Count the number of iterations
        self.operation_count = 0  # Count the number of binary operations (additions/subtractions)
    
    def run(self):
        # Perform the overflow check
        print("Checking overflow...")
        if not checkOverflow(self.dividend, self.divisor):
            print("Overflow detected. Cannot proceed.")
            return
        else:
            print("No overflow detected.")

        print("Running the Restoring Division Method...")

        # Special case: if the dividend's length is twice the divisor's length minus 1
        if len(self.dividend) - 1 == 2 * (len(self.divisor) - 1):
            self.accum = "0"

        sequence_counter = True
        while sequence_counter:
            #update the number of iterations
            self.iteration_count += 1

            # Perform shift operation (shift left the combined accumulator and quotient)
            combined = self.accum + self.quotient

            shifted = shiftLeft(combined)

            # Extract the remainder portion for subtraction
            self.Remainder = shifted[:len(self.divisor)]

            #Perform subtraction
            new_iteration = subtractBinary(self.Remainder, self.divisor)

            self.operation_count += 1

            iteration1 = new_iteration + shifted[len(new_iteration):] #operation 2

            #check the most significant bit (MSB) to determiine restoration
            while int(iteration1[0]) == 1:
                iteration1 += "0"
                self.iteration_count += 1
                if self.iteration_count > (len(self.divisor) -1):
                    print("Exceeded maximum iterations.")
                    new_iteration = addBinary(iteration1[:len(self.divisor)], self.divisor )
                    self.operation_count += 1
                    iteration1 = new_iteration + iteration1[len(new_iteration):]
                    print(iteration1)
                    break
                else:
                    shifted = shiftLeft(iteration1)
                    new_iteration = addBinary(shifted[:len(self.divisor)], self.divisor )
                    iteration1 = new_iteration + shifted[len(new_iteration):]
                    self.operation_count += 1

            if int(iteration1[0]) == 0 and (self.iteration_count <= (len(self.divisor) -1)):
                iteration1 += "1"

            
            self.quotient = iteration1[len(self.divisor):]
            self.accum = iteration1[:-len(self.quotient)]

            # Continue until the sequence counter indicates completion
            sequence_counter = sequenceCounter((len(self.divisor) - 1), self.iteration_count)
            if self.iteration_count > (len(self.divisor) -1):
                sequence_counter = False

        # Extract and print the final remainder (ignoring the sign bit)
        self.rem = self.accum[1:]

    def displayResult(self):
        """
        Displays the quotient and remainder of the division in binary format.
        """
        print("Quotient: ", self.quotient)
        print("Remainder: ", self.rem)
        print("Number of Subtraction/Addition performed: ", self.operation_count)
        print(self.iteration_count)

#debuggging example
c1 = Restoring("1101111100", "11101")
c1.run()
c1.displayResult()