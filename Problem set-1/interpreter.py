def main():
    expression = input("Expression: ")
    math(expression)


def math(expression):
    x, y, z = expression.split(" ")
    if y=="+":
        a =int(x)+int(z)
        print(float(a))
    elif y=="-":
        a =int(x)-int(z)
        print(float(a))
    elif y=="*":
        a =int(x)*int(z)
        print(float(a))
    elif y=="/":
        a =int(x)/int(z)
        print(float(a))
main()
