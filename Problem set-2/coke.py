amount_due = 50
while amount_due > 0:
    print("Amount Due: ", amount_due)
    coin = int(input("Insert Coin: "))
    # subtracting if the value of coin is 25 10 5
    if coin in [25, 10, 5]:
        # amount_due=amount_due-coin
        amount_due -= coin
# converting the negetive value to positive
changed_owed = abs(amount_due)
# print the remaining chnage machine has to give the user
print("Changed Owed: ", changed_owed)
