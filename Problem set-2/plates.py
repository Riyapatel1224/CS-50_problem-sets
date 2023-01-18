def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # vanity plates have to be maximum of 6 letters
    # and a minimum of 2 character at start
    if len(s) < 2 or len(s) > 6:
        return False

    # starts with atleast two letters
    if s[0].isalpha() == False or s[1].isalpha() == False:
        return False



    # first number cant be 0
    i = 0
    while i < len(s):
        if s[i].isalpha() == False:
            if s[i] == '0':
                return False
            else:
                break
        i += 1

    #no periods spaces and puntuations are alllowed
    for c in s:
        if c in ["."," ","!","?"]:
            return False

     # numbers cant be in middle of plate
    for i in range(len(s)):
        if s[i].isdigit():
            if not s[i:].isdigit():
                return False
    #if all the above condition returns false means everything is up to date
    return True


main()
