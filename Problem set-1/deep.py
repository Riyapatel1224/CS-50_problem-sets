def main():
    deep = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    thoughts(deep)


def thoughts(deep):
    if deep.strip() == "42":
        print("Yes")
    elif deep.lower().strip() == "forty-two":
        print("Yes")
    elif deep.lower().strip() == "forty two":
        print("Yes")
    else:
        print("No")


main()
