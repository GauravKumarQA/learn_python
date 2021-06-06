#Base string check 
baseString = "Hello i am string"
print("i" in baseString)
#String check contains with if clause
checkString = "Hello"
if checkString in baseString:
    print(baseString + " contains " + checkString)
 
notContains="Gaurav"
if notContains not in baseString:
    print(baseString + " not contains " + notContains)
    