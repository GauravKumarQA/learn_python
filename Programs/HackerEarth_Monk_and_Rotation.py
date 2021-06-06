'''
This is a solution for monk and rotation problem
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here

testCases = input()
for i in range(0, testCases):
    inputarr = []
    numbersOfElementsandRotaion = input()
    numberOfElement = int(numbersOfElementsandRotaion.split(" ")[0])
    numberOfrotation = int(numbersOfElementsandRotaion.split(" ")[1])
    array = input()
    array = array.split(" ")
    newEmptyList = []
    for j in range(numberOfElement-numberOfrotation, numberOfElement):
        newEmptyList.append(array[j])

    for k in range(0, numberOfElement-numberOfrotation-1):
        newEmptyList.append(array[k])

    for l in newEmptyList:
        print(l, end=" ")

    print("\n")