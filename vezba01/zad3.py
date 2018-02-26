import sys

if __name__=="__main__":
    if len(sys.argv)<3:
        print("There is not enough arguments. :/")
    else:
        str1=sys.argv[1]
        str2=sys.argv[2]
        strt1=str1[0:3]*2
        strlen=int(len(str2))
        strt2=str2[(strlen-3):strlen]*2
        strng=strt1+str1+str2+strt2
        print(strng)
else:
    print("Something does not work :(")
