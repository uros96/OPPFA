import sys

if __name__=="__main__":
    t1=(1234, 1.234, "first")
    t2=(2134, 12.34, "second")
    t3=(3124, 123.4, "third")
    t4=(4123, 1234.0, "fourth")
    s={t1, t2, t3, t4};
    print(s)
    print('\n')
    s.remove(t1)
    print(s)
else:
    print("Something does not work. :/")

