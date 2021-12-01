def input_n():
    print('Input n:')
    n=int(input())
    while(n<=0):
        n=int(input())
    return n

def pynamid(n):
    tmp=2*n-2
    for i in range(n,0,-1):
        for j in range(tmp,0,-1):
                print(end="  ")
        tmp+=1
        for j in range(1, 2*i):
            print('*', end=" ")
        print('\t')
        

if __name__ == "__main__":
    n=input_n()   
    pynamid(n)