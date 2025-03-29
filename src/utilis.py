def addBinary(BinNum1, BinNum2):
    """
    Takes two binary numbers as strings (BinNum1 and BinNum2) and performs binary addition.

    Steps:
    1. Convert both binary strings to decimal using base 2.
    2. Perform the addition.
    3. Convert the result back to a binary string.
    4. Trim any overflow bit if the result exceeds the original input length.
    5. Print and return the final binary sum.
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
    3. Print and return the result.
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

    twoS_BinNum = FindTwosCom(BinNum2)
    SubBin = addBinary(BinNum1, twoS_BinNum)
    return SubBin


def shiftLeft():
    return -1

def sequenceCounter():
    return -1

def checkOverflow():
    return -1