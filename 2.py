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
    temp1 = a
    temp2 = b
    while (temp1 != temp2):
        if (temp1 > temp2):
            temp1 -= temp2
        else:
            temp2 -= temp1
    gcd = temp1
    return gcd


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
    lcm=int(lcm(a,b))

    print("The least common multiple of these two numbers is:",end=' ')
    print(lcm)
