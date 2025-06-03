Weight = float(input("Enter Weight: "))
Unit = input ("Enter 'K' for kg or 'L' for LB: ")
if Unit == 'K' or 'k':
    conversion = Weight / .45359237
    print (" the weight in LB is " + str(conversion))
elif Unit == 'L' or 'l':
    conversion = Weight / 2.205
    print (" the weight in KG is " + str(conversion))