#input from user
def main():
    user_input=input("Input: ")
    without(user_input)
    
#output without a,e,i,o,u
def without(no_vovel):
    print("Output: ",end="")
    for c in no_vovel:
        if not c.lower() in ["a","e","i","o","u"]:
            print(c,end="")
main()