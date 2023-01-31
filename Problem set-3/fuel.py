def main():

    while True:
        try:
            # taking input from the user
            x, y = input("Fraction: ").split("/")
            # if the fraction is greater then 100% then it will ask the user for  input again
            if int(x) <= int(y):
                return percentage(x, y)
            else:
                pass
        except(ValueError, ZeroDivisionError):
            pass  # it will pass the exception for infinity loop until the user enters the reliable input


def percentage(x, y):
    # checking if the fuel is emply or full
    per = (round((int(x)/int(y))*100))
    if per <= 1:
        print("E")
    elif per >= 99 or per <= 100:
        print("F")
    else:
        print(per, "%", sep="")


main()
