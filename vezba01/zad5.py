import sys

if __name__=="__main__":
    dict_file=open("dict_test.txt", 'r')
    line=dict_file.readline()

    word=""
    d = {}
    while line:
        for i in line:
            if ((i==',') or (i==' ') or (i=='.')):
                if word=="":
                    continue
                if word in d:
                    counter=d[word]
                    counter+=1
                    d[word]=counter
                else:
                    d[word]=1
                word=""
            else:
                word+=i
        line=dict_file.readline()

    for key, value in d.items():
        print(key,value)
    dict_file.close()
else:
    print("Something does not work. :/")
