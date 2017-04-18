def intMultiplier(initNum, lastNum):
    for multiplier in range(initNum,lastNum+1):
        for i in range(1,10):
            print multiplier, " x ", i, " = ", multiplier*i
        print "==================== "

intMultiplier(3,5)
