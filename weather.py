# This program want to ask about the weather condition in your area
print("HELLO WORLD")
print("what is the weather condition in your area? {rainy,cloudy,sunny and normal}")
weather = input()
if weather == "rainy":
   print("NICE,it's rainy,use a cadigan")
elif weather == "cloudy":
   print("GOOD,it's cloudy,get indoor before it start raining")
elif weather == "sunny":
   print(" NOT NICE,go and get an umbrella cause it's very hot")
elif weather == "normal":
   print("thanks,the weather is very good")
else:
    print("You did not input a weather condition")
print("Thanks you for your cooperation")