people = int(raw_input("How many people?"))
pizzas = int(raw_input("How many pizzas do you have?"))
slices = int(raw_input("How many slices of pizzas?"))
print ("{0} people with {1} pizzas and {2} slices").format(people, pizzas, slices)
num = pizzas*slices
num2= int (num/people)
num3 = num - (num2*people)
print ("Each person gets {0} pieces of pizza").format(num2)
print ("There are {0} leftover pieces.").format(num3)


