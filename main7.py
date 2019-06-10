length = int(raw_input("What is the length of the room in feet? "))
width = int(raw_input("What is the width of the room in feet?"))
print ("You entered dimensions of {0} feet by {1} feet").format(length, width)
feet = length*width
num = feet*0.09290304
print ("The area is {0} square feet {1} square meters").format(feet, num)


