print("enter your number")
try:
    number = int(input())
    if number %2 == 1:
        print("you ave entered an even number")
    else:
        print("you have entered an odd number")

except ValueError:
    print("Error:you've refuse to enter a number")
          