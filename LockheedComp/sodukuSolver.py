import math,sys,os

sodukuInput = input("input")
splitIn = sodukuInput.split(" ")
testcase = splitIn[0].rstrip()
print(splitIn)
print("Testcase:",testcase)

def getTestCase(testcase):
    for i in testcase:
        for row in range(len(splitIn)-1):
            print(splitIn[row])
            if row % 3:
                print("divisible")
                continue

getTestCase(testcase)

