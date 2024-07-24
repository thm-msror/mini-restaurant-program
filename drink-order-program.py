def nonNegativeIntegerValidation(prompt,errorMessage):
    while True:
        try:
            num=int(input(request))
            assert num>=0
            break
        except:
            print(errorMessage)
    return num

MENU_ITEMS=['karak','tea','coffee']
PRICE_LIST=[2,1,5]
amt=0
orders=[]
for item in range(len(MENU_ITEMS)):
    request="How many "+MENU_ITEMS[item]+" do you want? "
    error="Age should be a non-negative integer!"
    order=nonNegativeIntegerValidation(request,error)
    orders.append(order)
    
    amt+=PRICE_LIST[item]*order

for i in range(len(orders)):
    print("    -",orders[i],MENU_ITEMS[i])
print("Your total bill is",amt,"QAR.")
    

