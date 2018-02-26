import sys

if __name__=="__main__":
    t1=(1, 0.1, "one")
    t2=(2, 0.2, "two")
    t3=(3, 0.3, "three")
    t4=(4, 0.4, "four")
    l=[t1, t2, t3, t4];
    print(l)
    print('\n')
    l.remove(t1)
    print(l)
else:
    print("Something does not work. :/")
