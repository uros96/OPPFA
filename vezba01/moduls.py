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

#print nubmer if nubmer%2==0
def oddOrEven():
    
    l=[]
    for i in range (10):
        n=int(input("Enter an number: "))
        if n%2!=0:
            l.append()
            
    print(l)
#prints sum of (0,n) sum(1+1/(n^n))
def sumOfOnePerSqr():
    n=int(input("Enter a number: "))
    suma=0
    for i in range (1,n):
        suma+=1/i**i

    print(suma)

#prints string in reverse
def stringReverse():
    string=input("Enter a string: ")
    temp=""
    for i in string[::-1]:
        temp+=i
    print(temp)

#find student in list and print grades
def student_list():
    studentList = {'Milos Matic':{'biologija':'5','matematika':'5','srpski':'5','nemacki':'5'},
    'Marija Jelic':{'biologija':'2','matematika':'1','srpski':'2'},
    'Pera Peric':{'biologija':'2','matematika':'4','srpski':'5'},
    'Milica Jelic':{'biologija':'4','matematika':'5','srpski':'5'},
    'Mika Lazic':{'biologija':'5','matematika':'5','srpski':'5'}}
    flag=0
      
    trytofind=""
    searchFor=True
    while searchFor:
        trytofind=input("Enter a name: ")
        if trytofind in studentList:
            name=trytofind
            
            for student in studentList:
                if student==name:
                    points=0
                    subs=0
                    for subject in studentList[student]:
                        subs+=1
                        if int(studentList[student][subject])==1:
                            flag=1
                        else: 
                            points+=int(studentList[student][subject])
                    if flag==0:
                        if (round(1.0*points/subs,2)>4.5):
                            print(name + " excellent: " + str(round(1.0*points/subs,2)))
                        elif(round(1.0*points/subs,2)>3.5):
                            print(name + " very good: " + str(round(1.0*points/subs,2)))
                        elif(round(1.0*points/subs,2)>2.5):
                            print(name + " okay: " + str(round(1.0*points/subs,2)))
                        else:
                            print("Student failed!")
        elif trytofind=="end":
            searchFor=False
        else:
            print("Student not found in a list.")
        
    
    