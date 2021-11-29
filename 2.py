print('Input the first positive integer:')
a=int(input())
while(a<0):
    a=int(input())
print('Input the second positive integer:')
b=int(input())
while(b<0):
    b=int(input())

if(a<b): 
    tmp=a
    a=b
    b=tmp


def GCD(a,b):
    for i in range(b, 1, -1):
        if(b%i==0 and a%i==0):
            return i

def LCM(a,b):
    if(b==1): return b
    lcm=a*b/GCD(a,b)
    return lcm

print('least common multiple:')
print(LCM(a,b))
