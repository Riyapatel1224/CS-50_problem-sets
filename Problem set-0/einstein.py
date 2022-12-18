#take input from the user mass
def main():
    m=int(input("m: "))
    joules(m)

#calculate the joules
def joules(m):
    c = 3 * (10**8)
    E = m * (c**2)
    print("E: ",E)

main()