number = 10

def plusOne():
    return number + 1

def minusOne():
    return number - 1

def multiplyTwo():
    global number
    number = 15
    return number * 2
print(plusOne())
print(minusOne())
print(multiplyTwo())