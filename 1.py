def input_x():
    x=int(input('Input a number to check:'))
    return x


def check_prime(x):
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


if __name__ == "__main__":
    x=input_x()
    print(check_prime(x))


    
