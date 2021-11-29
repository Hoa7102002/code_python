def readFileDubaothoitiet():
    data=open('dubaothoitiet.txt') #read file dubaothoitiet
    data1=data.read()
    data.close()
    return data1
print(readFileDubaothoitiet())


def readFileKyhieu():
    data=open('kyhieu.txt') #read file kyhieu
    data1=data.read()
    data.close()
    return data
print(readFileKyhieu())

def weatherForecast():
    data=open('dubaothoitiet.txt') #read file dubaothoitiet
    data1=data.read()
    dat=open('dubaothoitiet.txt')
    data2=dat.read()
    weekdays=[ 'Monday','Tuesday','Wednesday','Thursday', 'Friday', 'Saturday', 'Sunday']
    Forecast=dict(
        (key.strip(),value.strip())
            for key, value in (tmp.split(':')
                for tmp in data1.split('\n'))
    )
  
    weatherSymbol=dict(
        (Key.strip(), Value.strip())
            for Key, Value in (temp.split(':')
                for temp in data2.split('\n'))
    )

    print("Today:")
    print("ex: Wednesday-11/9/2022")
    Today=input()
    print("input the next n days: ")
    n=int(input())
    while(n<=0): n=int(input())
    Today=Today.split('-')# :2(day and weekdays)
    weeks=Today[0]
    days=Today[1]
    if(weeks in weekdays and days in Forecast):
        tmp=list(Forecast)
        for i in range(1, len(tmp)):
            if(days==tmp[i]):
                break
        for k in range(0, len(weekdays)):
            if(weeks==weekdays[k]):
                break
        for i in range(i, i+n):
            if(i>=len(tmp)):
                break
            print(weekdays[i], end="-")
            print(tmp[i],end=":")
            print(weatherSymbol[Forecast[tmp[i]]])
            k+=1
            if(k==7): k=0
    else:
        print("no information")
    data.close()
    dat.close()
print(weatherForecast())
