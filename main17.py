w = int(raw_input("What is your weight?"))
a1 = int(raw_input("What is the amount of alcohol by volume of the drinks consumed?"))
h = int(raw_input("What is the amount of time since your last drink?"))
g = str(raw_input("What is yor gender?"))
r = 0
if g == "man":
    r = 0.73
else:
    r = 0.66
bac = (a1*5.14/w*r)-0.015*h
print bac


