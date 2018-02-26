import sys

if __name__=="__main__":
    if len(sys.argv)<2:
        print("Please, give me an argument. :)")
    else:
        n=int(sys.argv[1])
    def sumofsqrs(x):
        i=0
        sum=0
        for i in range (0,x+1):
            sum+=i**2
        print("Sum of squares of first "+ str(n) +" numbers is: "+ str(sum))
else:
    print("Something does not work. :/")

sumofsqrs(n)
