#sum of first n numbers (without n)
def sumN ():
    n=input("Enter a number: ")
    n=int(n)
    sum=0
    for i in range (n):
        sum+=i
    print("Sum of first " + str(n) + " elements is " + str(sum))

#sum of first n number, each number squared (without n)
def sumNsqr():
    n=input("Enter a number: ")
    n=int(n)
    sum=0
    for i in range (0, n):
        sum+=i**2
    print("Sum of squares of first " + str(n) + " elements is " + str(sum))

#first 3 chars from string1 and last 3 chars from string2 repeated twice after original 
def stringRep():
    string1 = input("Enter first string: ")
    string2 = input("Enter second string: ")
    tmp1 = string1[0:3]*2
    tmp2 = string2[(len(string2)-3):len(string2)]*2
    concatenated = (tmp1 + string1 + string2 + tmp2)
    print(concatenated)

#reverse iterate first 100 elements [0, n-1] (n - easily can be changed) 
def first100(): 
    n=100
    A=[]
    for i in range (0, n):
        A.append(n-i-1)
    print(A)

#add tuples in list, print it and remove from list
def tuples():
    A=[]
    n = input("Enter number of tuples in a list: ")
    n = int(n)
    for i in range (n):
        print("For tuple " + str(i))
        A.append((int(input("Enter an integer: ")), float(input("Enter a float: ")), input("Enter a char: ")))             
    print(A)
    A.remove(A[int(input("Remove selected tuple: [0-" + str(n-1) + "]: "))])
    print(A)

#add sets in list, print it and remove from list
def sets():
    A=set()
    n = input("Enter number of sets in a list: ")
    n = int(n)
    for x in range (n):
        print("For tuple " + str(x))
        A.add((int(input("Enter an integer: ")), float(input("Enter a float: ")), input("Enter a char: "))) #float conversion problem
    print(A)
    A.remove(list(A)[int(input("Remove selected set: [0-" + str(n-1) + "]: "))])
    print(A)
