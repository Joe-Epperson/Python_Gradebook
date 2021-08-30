########################################################################
##
## CS 101
## Program #09
## Joe Epperson IV
## jee4cf@umsystem.edu
##
## PROBLEM : This program accepts test and assignment scores and outputs the students grades
##
## ALGORITHM : 
##      1. Write out the algorithm
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################
import math


#This is to add a test
def atest():
    test = input("Enter the new Test score 0-100 : ")
    while True:
        if test.isdigit() == True:
            break
        else:
            print("The test value must be an integer or a float and greater than zero.")
            test = input("Enter the new Test score 0-100 : ")
    test = float(test)
    return (test)

#This is to remove a number from the tests
def rtest(tests):
    test = input("Enter the test score to remove : ")
    while True:
        if test.isdigit() == True:
            break
        else:
            print("The test value must be an integer or a float and greater than zero.")
            test = input("Enter the test score to remove : ")
    test = float(test)
    try:
        tests.remove(test)
    except:
        print("Value is not in the list.")
    return (tests)

#This is to clear the tests
def ctest(tests):
    tests = []
    return (tests)

#This is to add an assignment
def aassign():
    assign = input("Enter the new Assignment score 0-100 : ")
    while True:
        if assign.isdigit() == True:
            break
        else:
            print("The assignment value must be an integer or a float and greater than zero.")
            assign = input("Enter the new Assignment score 0-100 : ")
    assign = float(assign)
    return (assign)

#This is to remove a number from the assignments
def rassign(assignments):
    assign = input("Enter the assignment to remove : ")
    while True:
        if assign.isdigit() == True:
            break
        else:
            print("The assignment value must be an integer or a float and greater than zero.")
            assign = input("Enter the assignment to remove : ")
    assign = float(assign)
    try:
        assignments.remove(assign)
    except:
        print("Value is not in the list.")
    return (assignments)

#This is to clear the assignments
def cassign(assignments):
    assignments = []
    return (assignments)

#This is to display the scores
def dscores(assignments,tests):
    #This is getting all of the necessary test values for the table
    numtests = len(tests)
    mintests = min(tests)
    maxtests = max(tests)
    avgtests = sum(tests) / numtests
    svalt = []
    for i in tests:
        valt = (i - avgtests)**2
        svalt.append(valt)
    sumvalt = sum(svalt)
    stdtests = math.sqrt(sumvalt / numtests)

    #This is getting all of the necessary test values for the table
    numassignments = len(assignments)
    minassignments = min(assignments)
    maxassignments = max(assignments)
    avgassignments = sum(assignments) / numassignments
    svala = []
    for i in assignments:
        vala = (i - avgassignments)**2
        svala.append(vala)
    sumvala = sum(svala)
    stdassignments = math.sqrt(sumvala / numassignments)

    #This is for the weighted grades
    wtests = avgtests * .6
    wassignments = avgassignments * .4
    weighted = wtests + wassignments

    print("{:<10}{:<5}{:<5}{:<5}{:<5}{:<5}".format("Type", "#", "min", "max", "avg", "std"))
    print("{:<}".format("=" * 35))
    print("{:<10}{:<10.2f}{:<10.2f}{:<10.2f}{:<10.2f}{:<10.2f}".format("Tests", numtests, mintests, maxtests, avgtests, stdtests))
    print("{:<10}{:<10.2f}{:<10.2f}{:<10.2f}{:<10.2f}{:<10.2f}".format("Programs", numassignments, minassignments, maxassignments, avgassignments, stdassignments))
    print("The weighted grade is : {:.2f}".format(weighted))

#This is the main program
tests = []
assignments = []
while True:
    print("Grade Menu")
    print("1 - Add Test")
    print("2 - Remove Tests")
    print("3 - Clear Tests")
    print("4 - Add Assignments")
    print("5 - Remove Assignments")
    print("6 - Clear Assignments")
    print("D - Display Scores")
    print("Q - Quit")
    choice = input("What is your choice : ")
    if choice == "1":
        numt = atest()
        tests.append(numt)
    elif choice == "2":
        print(rtest(tests))
    elif choice == "3":
        print(ctest(tests))
    elif choice == "4":
        numa = aassign()
        assignments.append(numa)
    elif choice == "5":
        print(rassign(assignments))
    elif choice == "6":
        print(cassign(assignments))
    elif choice == "D" or choice == "d":
        print(dscores(assignments,tests))
    elif choice == "Q" or choice == "q":
        break
    else:
        continue




    
    
