def addBinary(BinNum1, BinNum2):
    """
    Takes two binary numbers as strings (BinNum1 and BinNum2) and performs binary addition.

    Steps:
    1. Convert both binary strings to decimal using base 2.
    2. Perform the addition.
    3. Convert the result back to a binary string.
    4. Trim any overflow bit if the result exceeds the original input length.
    5. return the final binary sum.
    """
    #sum the binary num after converting the string into decimal
    BinarySum = bin(int(BinNum1, 2) + int(BinNum2, 2))
    
    #trim the extra 0b
    BinarySum = BinarySum[2:]


    #find the maximum length from two binary number
    max_len = max(len(BinNum1), len(BinNum2))
    
    #Discard the overflow bit if the BinarySum has one
    if len(BinarySum) > max_len:
        x = len(BinarySum) - max_len
        return BinarySum[x:]
    
    BinarySum = BinarySum.zfill(max_len)
    return BinarySum

def FindTwosCom(BinNum):
    """
    Takes a binary number (as a string) and returns its two's complement.

    Steps:
    1. Compute the one's complement by flipping each bit (0 to 1 and 1 to 0).
    2. Add 1 to the one's complement using the addBinary() function to obtain the two's complement.
    3. return the result.
    """
    one_s_comp = ""

    #Create 1S complement of the given Binary Digit
    for i in BinNum:
        if i == "1":
            i = "0"
            one_s_comp += i
        else:
            i = "1"
            one_s_comp += i
    
    #Convert the 1S complement to 2S complement adding 1
    TwoS_com = addBinary(one_s_comp, "1")

    return TwoS_com

def subtractBinary(BinNum1, BinNum2):
    """
    Takes two binary numbers as strings (BinNum1 and BinNum2) and performs binary subtraction.

    Steps:
    1. Find the two's complement of BinNum2 using the FindTwosCom() function to negate it.
    2. Add BinNum1 and the two's complement of BinNum2 using the addBinary() function.
    3. Return the result as the binary subtraction output.
    """
    twoS_BinNum = FindTwosCom(BinNum2)
    SubBin = addBinary(BinNum1, twoS_BinNum)
    return SubBin


def shiftLeft(BinNum):
    """
    Performs a left shift operation on a binary number represented as a string.

    Steps:
    1. Remove the first bit (leftmost bit) from the binary string.
    2. Return the remaining binary string.
    """
    BinNum = BinNum[1:]
    return BinNum


def sequenceCounter(num1, num2):
    """
    Compares two numbers to determine if the maximum number of iterations is reached.

    Steps:
    1. Compare the integers and return the True of False based on that.
    Returns:
    - bool: True if iterations should continue, False if the limit is reached.
    """
    if num1 == num2 or num1 < num2:
        return False
    return True

def restore(BinNum):
    """
    Restores the binary number by adding a '0' to the right, simulating a shift.

    Steps:
    1. Append '0' to the end of the binary string to simulate a restore step.
    2. Return the updated binary number.
    """
    BinNum = BinNum + "0"
    return BinNum

def checkOverflow(BinNum1, BinNum2):
    """
    Checks for overflow during binary division using two's complement arithmetic.

    Steps:
    1. Extract the leftmost bits of BinNum1 (equal to the length of the divisor) to check for overflow.
    2. Find the two's complement of BinNum2 using the FindTwosCom function.
    3. Perform binary addition using the addBinary function.
    4. Check the most significant bit (leftmost bit) of the result. 
       - If it is '1', overflow has occurred (indicating a negative result in two's complement).
       - Otherwise, no overflow.
    """

    num1 = BinNum1[:-(len(BinNum2)-1)]
    num2 = FindTwosCom(BinNum2)

    output = addBinary(num1, num2)

    if output[0] == "1":
        return True
    else:
        return False
    
def Hexadecimal(BinNum):
    """
    converts a binary number to hexadecimal.
    
    steps: 
    1. convert it to decimal using int() function
    2. convert the decimal number to hex using hex() function
    4. return the final hex number
    """

    HexNum = hex(int(BinNum, 2))
    HexNum = HexNum[2:].upper()
    return "0x" + HexNum 


# Test case
Hexadecimal = Hexadecimal("101010")
print(Hexadecimal)
