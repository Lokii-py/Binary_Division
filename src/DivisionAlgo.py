import utils

class Restoring:
    e_bit = "0"

    def __init__(self, dividend, divisor):
        self.dividend = dividend
        self.divisor = divisor
        self.accumulator = "0" * (8-len(dividend))
        self.iteration_count = 0

    def run(self):
        self.sequence_counter = True
        print("Running the Restoring Division Methond...")
        while self.sequence_counter:
            checkOverflow()


    
    def displayResult(self):
        return -1

class NonRestoring:
    def __init__(self, dividend, divisor):
        return -1
    