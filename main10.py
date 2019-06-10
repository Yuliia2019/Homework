const = 0.055
price1 = int(raw_input("Enter the price of item1: "))
quantity1 = int(raw_input("Enter the quantity of item1"))
price2 = int(raw_input("Enter the price of item2: "))
quantity2 = int(raw_input("Enter the quantity of item2"))
price3 = int(raw_input("Enter the price of item3: "))
quantity3 = int(raw_input("Enter the quantity of item3"))
subtotal = (price1*quantity1)+(price2*quantity2)+(price3*quantity3)
tax = subtotal*const
total= (subtotal+tax)
print ("Subtotal price = {0}, tax = {1}, total price = {2}").format(subtotal, tax, total)