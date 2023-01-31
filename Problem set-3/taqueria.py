
menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
}
# addition will start with 0
total_amount = 0
while True:
    try:
        # take input from user title bcz it will formate the input into the given dict
        item = input("Item: ").title()
        # check if the inputes item is in the dict
        if item in menu:
            # add the item with inputed item key from the dict
            total_amount += menu[item]
            # print the total of
            print("Total: $", end="")
            print("{:.2f}".format(total_amount))
    except EOFError:
        print()
        break
