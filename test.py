customer_name= input('Please enter your name: ')
print(f'Hello,{customer_name},We hope you will enjoy shopping with us')

shopping_list={'book':20,'pen':15,'ruler':10}

money=int(input('How much do you have with you?: '))
item=input('what do you want to buy?:')
quantity=int(input(f'how many {item} do you want?: '))
def calculate():
    if item in shopping_list:
        print(f'Item is {shopping_list.get(item)} naira')
        cost = quantity * shopping_list.get(item)
        print(cost)
        if money > cost:
            change= money - cost
            print(f'You have {change} naira left')
        elif money == cost:
            print ('You have emptied your wallet')
        else:
            print('You dont have enough money')
    else:
        print('item not available')
calculate()


 print('Thank you for shopping with us')