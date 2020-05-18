#Algorithm Case Study

def naive(a,b):
    x=a; y=b
    z =0
    while(x > 0):
        z = z+y
        x = x-1
    return z

def testnaive():
    i=0
    while(i < 10):
        j=0
        while(j < 10):
            print(i,j)
            print(naive(i,j))
            j += 1
        i += 1
        

if __name__ == "__main__":
    testnaive()
