def checkPosNeg(n):
    if n > 0:
        return 'Positive'
    elif n < 0:
        return 'Negative'
    else:
        return 'Value is zero'

def printPrimes():
    printedPrimes = 0
    notPrime = False
    for i in range(2, 100):
        notPrime = False
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                notPrime = True
                break
        if notPrime == False:
            print(i)
            printedPrimes += 1
        if printedPrimes >= 10:
            break

def sum1to100():
    sum = 0
    for i in range(1, 101):
        sum = sum + i
    return sum

