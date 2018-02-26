import sys

if __name__=="__main__":
        n=input("Enter an number: ")
        n=int(n)
        i=0
        sum=0
        for i in range (0,n+1):
            sum+=i
        print("Sum of first "+ str(n) +" numbers is: "+ str(sum))
else:
    print("Something does not work. :/")
