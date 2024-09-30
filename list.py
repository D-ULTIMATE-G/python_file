# try catch and except

def div42By(divideBy):
    try:
        return 42/divideBy
    except ZeroDivisionError:
        return ("error:you try to divide by Zero")
    
print(div42By(2))
print(div42By(3))
print(div42By(0))