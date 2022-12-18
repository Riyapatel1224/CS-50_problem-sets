#input greet form the user
def main():
    greet = input("Greeting: ")
    balance(greet)

def balance(greet):
#if greeting stats with hello output is $0
    if greet.lower().strip().startswith("hello",0,10):
        print("$0")
#if greeting starts with "h" but no hello output $20
    elif greet.lower().startswith("h",0,10):
        print("$20")
#oyherwise output $100
    else:
        print("$100")

main()