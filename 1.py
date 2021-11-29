
print('Input a number to check:')
x=int(input())
def checkPrime(x):
    tmp=0
    if( x<2):
        return False
    if (x==2):
        return True
    else:
        for i in range(2, x-1):
            if(x%i==0):
               tmp+=1
        if(tmp!=0): return False
    return True   
print(checkPrime(x))
    
