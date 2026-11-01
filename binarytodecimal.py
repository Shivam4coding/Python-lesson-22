def binaryToDecimal(binaryInput):
    resultDecimal = 0

    for digit in binaryInput:
        resultDecimal = resultDecimal * 2 + int(digit)

    return resultDecimal

binary = input("Input binary number : ")

print("Decimal equivalent : ", binaryToDecimal(binary))