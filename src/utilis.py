def addBinary(BinNum1, BinNum2):
    """
    Takes two strings called BinNum1 and BinNum2
    and converts them into decimal numbers first,
    then adds them, and converts the result back to binary.
    The result is trimmed to remove any overflow bit if it exceeds the original length.
    """

    #sum the binary num after converting the string into decimal 
    BinarySum = bin(int(BinNum1, 2) + int(BinNum2, 2))

    #trim the extra 0b
    BinarySum = BinarySum[2:]

    #find the maximum length from two binary number
    max_len = max(len(BinNum1), len(BinNum2))

    #Discard the overflow bit if the BinarySum has one
    if len(BinarySum) != max_len:
        x = len(BinarySum) - max_len
        return BinarySum[x:]
    
    return BinarySum

def FindTwosComplement(BinNum):
    """
    Takes the Binary number and convert it into 2S complement
    """
    one_s_comp = ""
    for i in BinNum:
        if i == "1":
            i = "0"
            one_s_comp += i
        else:
            i = "1"
            one_s_comp += i
    TwoS_com = addBinary(one_s_comp, "1")
    print(TwoS_com)
    return one_s_comp

def subtractBinary():
    return -1 

def shiftLeft():
    return -1

def sequenceCounter():
    return -1

def checkOverflow():
    return -1