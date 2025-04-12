import time
from utils import checkOverflow, shiftLeft, subtractBinary, restore, sequenceCounter, addBinary, Hexadecimal

class Division:
    def __init__(self, dividend, divisor):
        """
        Initializes the Restoring Division instance with the given binary dividend and divisor.
        
        Arguments:
        dividend (str): The binary dividend for the division.
        divisor (str): The binary divisor for the division.
        """
        self.signDividend = dividend[0]
        self.signDivisor = divisor[0]
        divisor = divisor[1:] #Remove the sign bit
        dividend = dividend[1:]
        self.dividend = "0" + dividend  # Add a leading zero as an extended bit
        self.divisor = "0" + divisor
        self.quotient = dividend  # Initialize quotient with the dividend
        self.accum = "0" * len(self.divisor)  # Initialize the accumulator with zeros
        self.iteration_count = 0  # Count the number of iterations
        self.operation_count = 0  # Count the number of binary operations (additions/subtractions)

    def determineSigns(self):
        """
        Determines the final outputs after performing division on the magnitude of the sign numbers
        Logical operator XOR will be performed between Numbers.
        Sign of quotient is XOR of the signs of dividend and divisor
        Sign of remainder is same as the sign of dividend
        """
        self.signQuotient = int(self.signDividend) ^ int(self.signDivisor)
        self.signRemainder = self.signDividend

    def displayResult(self):
        """
        Displays the quotient and remainder of the division in binary format.
        
        The method prints:
        - The quotient of the division.
        - The remainder of the division (ignoring the sign bit).
        - The total number of subtraction and addition operations performed.
        - The total number of iterations executed during the division.
        """
        if not checkOverflow(self.dividend, self.divisor):
            self.quotient = str(self.signQuotient) + self.quotient
            self.rem = self.signRemainder + self.rem

            print("Quotient:",self.quotient, "| In Hexadecimal:",Hexadecimal(self.quotient))
            print("Remainder:",self.rem, "| In Hexadecimal:",Hexadecimal(self.rem))
            print("Number of Subtraction/Addition performed: ", self.operation_count)
            print("Number of iteration: ", self.iteration_count)
            print("Execution Time: {:.6f} seconds\n".format(self.end_time - self.start_time))

class Restoring(Division):
    def __init__(self, dividend, divisor):
        super().__init__(dividend, divisor)

    def run(self):
        """
        Runs the Restoring Division Algorithm to divide the binary dividend by the binary divisor.
        
        The algorithm works by shifting the accumulated value and performing subtraction, followed by
        restoration if needed, until the division is complete.
        """
        # Perform the overflow check
        self.start_time = time.time()
        print("\nChecking overflow...")
        if checkOverflow(self.dividend, self.divisor):
            print("Overflow Status: Overflow detected. Division cannot be proceed.\n")
            return
        else:
            print("Overflow Status: No overflow detected.")

        print("\nRunning the Restoring Division Method...")

        # Special case: if the dividend's length is twice the divisor's length minus 1
        if len(self.dividend) - 1 == 2 * (len(self.divisor) - 1):
            self.accum = "0"

        sequence_counter = True
        while sequence_counter:

            combined = self.accum + self.quotient # Perform shift operation (shift left the combined accumulator and quotient)
            shifted = shiftLeft(combined)
            self.iteration_count += 1 #increment number of iterations
            operation1 = shifted    #Store the shifted value for potential restoration

            self.Remainder = shifted[:len(self.divisor)] #Extract the remainder portion for subtraction

            subtracted = subtractBinary(self.Remainder, self.divisor)
            self.operation_count += 1  #Increment the subtraction count

            operation2 = subtracted + operation1[len(subtracted):]

            #Check the most significant bit (MSB) to determine restoration
            if int(subtracted[0]) == 1:
                operation1 = restore(operation1) #Restore if subtraction resulted in a negative value (MSB = 1)
                self.operation_count += 1
                self.quotient = operation1[len(self.divisor):]
                self.accum = operation1[:-len(self.quotient)]
            else:
                operation2 += "1" #No restore needed, update values and set quotient bit to 1
                self.quotient = operation2[len(self.divisor):]
                self.accum = operation2[:-len(self.quotient)]

            sequence_counter = sequenceCounter((len(self.divisor) - 1), self.iteration_count) #Continue until the sequence counter indicates completion

        self.rem = self.accum[1:] #Extract and print the final remainder
        self.end_time = time.time()

    def displayResult(self):
        self.run()
        super().determineSigns()
        super().displayResult()

class NonRestoring(Division):
    def __init__(self, dividend, divisor):
        super().__init__(dividend, divisor)
    
    def run(self):
        """
        Runs the Non-Restoring Division Algorithm to divide the binary dividend by the binary divisor.
        
        The algorithm works by shifting the combined accumulator and quotient, performing subtraction, 
        and handling restoration if necessary based on the most significant bit (MSB).
        The loop continues until the division is complete or the maximum number of iterations is reached.
        """
        # Perform the overflow check
        self.start_time = time.time()
        print("Checking overflow...")
        if checkOverflow(self.dividend, self.divisor):
            print("Overflow Status: Overflow detected. Divison cannot be proceed.\n")
            return
        else:
            print("Overflow Status: No overflow detected.")

        print("\nRunning the Non-Restoring Division Method...")

        # Special case: if the dividend's length is twice the divisor's length minus 1
        if len(self.dividend) - 1 == 2 * (len(self.divisor) - 1):
            self.accum = "0"

        sequence_counter = True
        while sequence_counter:

            combined = self.accum + self.quotient
            shifted = shiftLeft(combined)
            self.iteration_count += 1  # Update the number of iterations

            self.Remainder = shifted[:len(self.divisor)] # Extract the remainder portion for subtraction

            new_iteration = subtractBinary(self.Remainder, self.divisor)
            self.operation_count += 1

            iteration1 = new_iteration + shifted[len(new_iteration):]  # Operation 2

            while int(iteration1[0]) == 1: # Check the most significant bit (MSB) to determine if restoration is needed
                iteration1 += "0"  # Add zeros to iteration1
                if self.iteration_count == (len(self.divisor) - 1):
                    new_iteration = addBinary(iteration1[:len(self.divisor)], self.divisor)
                    self.operation_count += 1
                    iteration1 = new_iteration + iteration1[len(new_iteration):]
                    break
                else:
                    shifted = shiftLeft(iteration1)
                    self.iteration_count += 1
                    new_iteration = addBinary(shifted[:len(self.divisor)], self.divisor)
                    self.operation_count += 1
                    iteration1 = new_iteration + shifted[len(new_iteration):]

            if int(iteration1[0]) == 0 and self.operation_count <= (len(self.divisor) - 1): # If MSB is 0 and iteration count is within the limit
                iteration1 += "1" # Update the iteration with '1'

            self.quotient = iteration1[len(self.divisor):] # Update quotient and accumulator
            self.accum = iteration1[:-len(self.quotient)]

            sequence_counter = sequenceCounter((len(self.divisor) - 1), self.iteration_count) # Continue until the sequence counter indicates completion

        self.rem = self.accum[1:] # Extract and print the final remainder (ignoring the sign bit)
        self.end_time = time.time()

    def displayResult(self):
        self.run()
        super().determineSigns()
        super().displayResult()