def read_file_dubaothoitiet():
    data=open('dubaothoitiet.txt') #read file dubaothoitiet
    data1=data.read()
    data.close()
    return data1



def read_file_kyhieu():
    data=open('kyhieu.txt') #read file kyhieu
    data1=data.read()
    data.close()
    return data1



def weather_forecast():
    days=read_file_dubaothoitiet().split("\n") 
    keys=read_file_kyhieu()
    keys=keys.strip("\n").split("\n")
    keys = {
        key.split(": ")[0]: key.split(": ")[1] for key in keys
    }
    forecast = {
        day.split(":")[0]: keys[day.split(":")[1]] for day in days
    }
    days = [day.split(":")[0] for day in days]
    weekdays=[ 'Monday','Tuesday','Wednesday','Thursday', 'Friday', 'Saturday', 'Sunday']

    print("Today:")
    print("ex: Wednesday-11/9/2022")
    today=input()
    print("input the next n days: ")
    n=int(input())
    today=today.split('-')# :2(day and weekdays)
    cur_day=today[0]
    day=today[1]
    if(cur_day in weekdays and day in forecast):
        week_idx = weekdays.index(cur_day)
        day_idx = days.index(day) + 1
        print("Weather forecast for the next {0} days".format(n))
        for i in range(week_idx+1, week_idx+n+1):
            print(weekdays[i%7], "-", str(days[day_idx])+":", forecast[days[day_idx]])
            day_idx += 1
    else:
        print("no information")


if __name__ == "__main__":
    print(read_file_kyhieu())
    print(read_file_dubaothoitiet())
    weather_forecast()
