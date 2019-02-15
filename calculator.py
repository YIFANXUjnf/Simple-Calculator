import math

accum = 0.0

state = True
while state:
    print 'Accumulator = '+str(accum)
    print 'Please choose one of the following options:'
    print '1) Addition'
    print '2) Subtraction'
    print '3) Multiplication'
    print '4) Division'
    print '5) Square root'
    print '6) Clear'
    print '0) Exit'
    opt = int(raw_input("What is your option? "))
    if opt == 0:
        state = False
    elif opt == 1:
        #do addition
        added = float(raw_input("Enter a number: "))
        accum = added + accum
    elif opt == 2:
        #do substraction
        subed = float(raw_input("Enter a number: "))
        accum = accum - subed
    elif opt == 3:
        #do multiplication
        mult = float(raw_input("Enter a number: "))
        accum = accum * mult
    elif opt == 4:
        #do division
        div = float(raw_input("Enter a number: "))
        if div == 0:
            print 'Not dividing by zero'
        else:
            accum = accum / div
    elif opt == 5:
        #do square root
        if accum < 0:
            print 'Not taking square root of negative number'
        else:
            accum = math.sqrt(accum)
    elif opt == 6:
        #clear
        accum = 0.0
    else:
        print "Illegal option "+str(opt)

print 'Program finished'

