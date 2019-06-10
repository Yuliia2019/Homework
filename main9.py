import math

const = 350
length = float(raw_input("What is the length of room?"))
width = float(raw_input("What is the width of room?"))
square = length*width
print square
result = float(square/const)
print result
result2 = math.ceil(result)
print result2
print ("You will need to purchase {0} gallons of paint to cover {1} square feet").format(result2, square)