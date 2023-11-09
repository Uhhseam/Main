##--------------------------------------------------------------
## Budget over or under
## Name: Asim Puri
## Date: 9/29/2023
##--------------------------------------------------------------

flag1 = 'y'
while flag1 == 'y': 
    cost = 0
    budget = float(input("Enter your budget for the month: $"))
    flag2 = 'y'
    while flag2 == 'y':
        expense = float(input('Enter you expense: '))
        cost += expense
        flag2 = input('Would you like to enter another expense? (y/n)')
    print(cost)
    tBudget = budget - cost
    if tBudget == 0:
        print('You are at equilibrium. \n\nHere is your remaining budget for the month: $',format(tBudget,',.2f'),
              '\nHere is your total cost for the month $',format(cost,',.2f'), sep='')
    elif tBudget < 0 :
        print('You went over the budget.\n\nHere is your remaining budget for the month: $',format(tBudget,',.2f'),
              '\nHere is your total cost for the month $',format(cost,',.2f'), sep='')
    elif tBudget < budget:
        print('You are under the budget.\n\nHere is your remaining budget for the month: $',format(tBudget,',.2f'),
              '\nHere is your total cost for the month $',format(cost,',.2f'), sep='')
    flag1 = input('\nWant to enter another budget? (y/n)')
print('\n~~~~ Good By ~~~~\n')