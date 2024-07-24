def viewMenu(menu):
    for menuitem,price in menu.items():
        print(menuitem.ljust(15),price)
def addnewItem(menu):
    item=input("What item would you like to add? ").lower().strip()
    if item not in menu:
        price=int(input(f"What is the price of {item}? "))
        menu[item]=price
    else:
        print(item,"is in the menu. If you want to update item select operation 3.")
def updateItem(menu):
    update=input("What item would you like to update? ").lower().strip()
    if update in menu:
        price=int(input(f"What is the new price of {update}? "))
        menu[update]=price        
    else:
        print(update,"is not in the menu. If you want to add this item select operation 2.")
def deleteItem(menu):
    item=input("What item would you like to remove? ").lower().strip()
    if item in menu:
        menu.pop(item)


menuDict={'soup':12, 'salad':15,
'hummus':10, 'fattoush':13, 'tabbouleh':17,
'musakhan':32, 'maqluba':28, 'mansaf':40,
'kibbeh':52, 'kebab':45, 'mandi':34, 'biryani':25,
'pizza':19, 'burger':22, 'fries':12,
'kunefe':15, 'cheesecacke':23, 'brownie':21}


def getChoice():
    line="-"*30
    print(line)
    print("Welcome to restaurant management system")
    print("1: view menu")
    print("2: add new item")
    print("3: update existing item")
    print("4: delete item")
    print("0: exit")
    operation=int(input("Which operations do you want to perform (0 to 4)? "))
    return operation


operation=getChoice()    
while operation!=0:
    if operation==1:
        viewMenu(menuDict)
    elif operation==2:
        addnewItem(menuDict)
    elif operation==3:
        updateItem(menuDict)
    elif operation==4:
        deleteItem(menuDict)
    operation=getChoice()    
print("Goodbye")
        
