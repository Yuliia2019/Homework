tax = 0.055
state = "married"
amount = float(raw_input("What is the order amount?"))
statement = str(raw_input("What is the state?"))
if state == statement:
    tax = amount*tax
    total = amount+tax
    print "The subtotal is {0}, the tax is {1}".format(amount, tax)
print "The total is {0}".format(amount)