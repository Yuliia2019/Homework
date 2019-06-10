print "Press C to convert from Fahrenheit to Celsius"
print "Press F to to convert from Celsius to Fahrenheit"
x = raw_input()
temperature = int(raw_input("Please enter the temperature"))
if x == "C" or x == "c":
    print (temperature-32)*5/9
else:
    print (temperature*9/5)+32

