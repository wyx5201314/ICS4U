

def getDigit(x,n):
    return x// (10 ** n) % 10


def ea4(x):
    a= getDigit(x,3)
    b= getDigit(x,2)
    c= getDigit(x,1)
    d= getDigit(x,0)
    print(a+b+c+d)
    print(d,c,b,a,sep="")
    print(d,a,b,c,sep="")
    print(a,c,b,d,sep="")

ea4(1234)