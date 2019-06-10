while 1==1:
    try:
        r = int(raw_input("What is the rate of return?"))
        if r>0:
           year = 72/r
           print "That's a valid input"
           print year
           break
    except ValueError:
        pass
    print "Sorry. That's not a valid input"