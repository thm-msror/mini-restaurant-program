#validation for user input
def nonNegativeIntegerValidation(prompt,errorMessage):
    while True:
        try:
            num=int(input(prompt))
            assert num>=0
            break
        except:
            print(errorMessage)
    return num

#Main program

#constants - menu dictionary
MENU_ITEMS={'soup':12,'salad':15,'hummus':10, 'fattoush':13, 'tabbouleh':17,
'musakhan':32, 'maqluba':28, 'mansaf':40, 'kibbeh':52, 'kebab':45, 'mandi':34,
'biryani':25, 'pizza':19, 'burger':22, 'fries':12, 'kunefe':15, 'cheesecacke':23,
'brownie':21}

#Show the menu to the user at the start
print("Welcome to the restaurant!")
print("Please take a look at our menu, start your order and say 'done' when you complete your order.")
print("")

print("---------------------------------------------------------------------------")
for menuitem,price in MENU_ITEMS.items():
    print(menuitem.ljust(15),price)
print("---------------------------------------------------------------------------")
print("")

orderedDict={} 
totalPrice=0 #to compute the total bill
item = input("What would you like to order? ")
while item != 'done':
    if item not in MENU_ITEMS:
        print(f"We do not sell {item}. Please choose something else.")
        print("")
    else:
        numberItems=nonNegativeIntegerValidation("How many " + item+ "(s) do you want? ", "Please enter a valid quantity.")
        print("")
        if item not in orderedDict:
            orderedDict[item]=numberItems
        else:
            orderedDict[item]+=numberItems
        totalPrice += numberItems*MENU_ITEMS[item] #compute the price
    item = input("What would you like to order? ")

#final displays
print("")
print("---------------------------------------------------------------------------")
print("Here is a summary of your order:")

#summary of the order
for item,numberItems in orderedDict.items():
    print("-",item,":",numberItems)

#total bill
print("Your total bill is", totalPrice, "QAR.") 
print("")

print("Thank you!")
print("---------------------------------------------------------------------------")


