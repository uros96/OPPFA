import sys

if __name__=="__main__":
    t1=(1234, 1.234, "first")
    t2=(2134, 12.34, "second")
    t3=(3124, 123.4, "third")
    t4=(4123, 1234.0, "fourth")
    l=[t1, t2, t3, t4];
    print(l)
    print('\n')
    l.remove(t1)
    print(l)
else:
    print("Something does not work. :/")
