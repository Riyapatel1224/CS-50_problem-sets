def main():
    time=input("What time is it? ")
    f=convert(time)
    if f>=7.0 and f<=8.0:
        print("breakfast time")
    elif f>=12.0 and f<=13.0:
        print("lunch time")
    elif f>=18.0 and f<=19.0:
        print("dinner time")
    else:
        print("")

def convert(time):
    hours, minutes = time.split(":")
    hours=(float(hours)*60)+ float(minutes)
    f=int(hours)/60
    return f

    

main()