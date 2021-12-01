def input_n():
    a=int(input('Input the first positive integer:'))
    while(a<0):
        a=int(input())
    return a


def gcd(a,b):
    if(a<b): 
        tmp=a
        a=b
        b=tmp
    for i in range(b, 1, -1):
        if(b%i==0 and a%i==0):
            return i


def lcm(a,b):
    if(a<b): 
        tmp=a
        a=b
        b=tmp
    if(b==1): return b
    lcm=a*b/gcd(a,b)
    return lcm


if __name__ == "__main__":
    a=input_n()
    b=input_n()
    print(lcm(a,b))
