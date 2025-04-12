import time
from utils import checkOverflow, shiftLeft, subtractBinary, restore, sequenceCounter, addBinary, Hexadecimal

class Division:
    def __init__(self, dividend, divisor):
        """
        Initializes the Restoring Division instance with the given binary dividend and divisor.
        
        Arguments:
        dividend (str): The binary dividend for the division.
        divisor (str): The binary divisor for the division.

        Steps:
        1. Pull the sign bit from the dividend and divisor
        2. Remove the sign bit from the dividend and divisor
        3. Add a leading zero to the dividend as an extended bit
        4. Initialize the quotient with the dividend
        5. pad zeros to the accum as the double register if needed
        6. Initialize the iteration and operation counters
        """
        self.signDividend = dividend[0]
        self.signDivisor = divisor[0]
        divisor = divisor[1:]
        dividend = dividend[1:]
        self.dividend = "0" + dividend 
        self.divisor = "0" + divisor
        self.quotient = dividend
        self.accum = "0" * len(self.divisor)
        self.iteration_count = 0
        self.operation_count = 0

    def determineSigns(self):
        """
        Determines the final outputs after performing division on the magnitude of the sign numbers
        Logical operator XOR will be performed between Numbers.
        Sign of quotient is XOR of the signs of dividend and divisor and Sign of remainder is same as the sign of dividend
        """
        self.signQuotient = int(self.signDividend) ^ int(self.signDivisor)
        self.signRemainder = self.signDividend

    def displayResult(self):
        """
        Displays the quotient and remainder of the division in binary format.
        Doesn't process if overflow is detected.
        
        This prints:
        - The quotient and remainder of the division in both binary considering sign bit and hexadecimal.
        - The total number of operations performed.
        - The total number of iterations executed during the division.
        - The execution time of the division process.
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
        Executes the Restoring Division Algorithm to divide the binary dividend by the binary divisor.

        The algorithm involves:
        1. Shifting the combined accumulator and quotient left.
        2. Subtracting the divisor from the accumulator.
        3. Restoring the accumulator if the subtraction results in a negative value.
        4. Don't Restore if the subtaraction results in 0 as extended bit.
        5. Repeating the process until sequence counter flag the end.
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

        #No need to pad zeros to the accum as the double register if dividend's length is twice the divisor's length minus 1
        if len(self.dividend) - 1 == 2 * (len(self.divisor) - 1):
            self.accum = "0"

        sequence_counter = True
        while sequence_counter:

            combined = self.accum + self.quotient                               #Perform shift operation (shift left the combined accumulator and quotient)
            shifted = shiftLeft(combined)
            self.iteration_count += 1
            operation1 = shifted                                                #Store the shifted value for potential restoration

            self.Remainder = shifted[:len(self.divisor)]                        #Extract the remainder portion for subtraction

            subtracted = subtractBinary(self.Remainder, self.divisor)
            self.operation_count += 1

            operation2 = subtracted + operation1[len(subtracted):]

            #Check the most significant bit (MSB) to determine restoration
            if int(subtracted[0]) == 1:
                operation1 = restore(operation1)                                #Restore if subtraction resulted in a negative value (MSB = 1)
                self.operation_count += 1
                self.quotient = operation1[len(self.divisor):]
                self.accum = operation1[:-len(self.quotient)]
            else:
                operation2 += "1"                                               #No restore needed, update values and set quotient bit to 1
                self.quotient = operation2[len(self.divisor):]
                self.accum = operation2[:-len(self.quotient)]

            sequence_counter = sequenceCounter((len(self.divisor) - 1), self.iteration_count)

        self.rem = self.accum[1:]                                               #Extract remainder
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
        Executes the Non-Restoring Division Algorithm to divide the binary dividend by the binary divisor.

        The algorithm involves:
        1. Shifting the combined accumulator and quotient left.
        2. Subtracting the divisor from the accumulator.
        3. Checking the most significant bit (MSB) of the accumulator:
            - If MSB is 1, set the quotient's LSB bit to 0 and add the divisor
            - If MSB is 0, set the quotient's LSB bit to 1.
        4. Repeating the process until the sequence counter signals the end of the division.
        5. Extracting the final remainder and updating the quotient.
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

        #No need to pad zeros to the accum as the double register if dividend's length is twice the divisor's length minus 1
        if len(self.dividend) - 1 == 2 * (len(self.divisor) - 1):
            self.accum = "0"

        sequence_counter = True
        while sequence_counter:

            combined = self.accum + self.quotient
            shifted = shiftLeft(combined)
            self.iteration_count += 1                                                               #Update the number of iterations

            self.Remainder = shifted[:len(self.divisor)]                                            #Extract the remainder portion for subtraction

            new_iteration = subtractBinary(self.Remainder, self.divisor)
            self.operation_count += 1

            iteration1 = new_iteration + shifted[len(new_iteration):]

            #Check the most significant bit (MSB) to determine if addition is needed
            while int(iteration1[0]) == 1:
                iteration1 += "0"                                                                   #Add zeros to iteration1
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

            if int(iteration1[0]) == 0 and self.operation_count <= (len(self.divisor) - 1):         #If MSB is 0 and iteration count is within the limit
                iteration1 += "1"                                                                   #Update the iteration with '1'

            self.quotient = iteration1[len(self.divisor):]                                          #Update quotient and accumulator
            self.accum = iteration1[:-len(self.quotient)]

            sequence_counter = sequenceCounter((len(self.divisor) - 1), self.iteration_count)

        self.rem = self.accum[1:]                                                                   #Extrac remainder (ignoring the sign bit)
        self.end_time = time.time()

    def displayResult(self):
        self.run()
        super().determineSigns()
        super().displayResult()