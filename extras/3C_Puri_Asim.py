##--------------------------------------------------------------
## Budget over or under
## Name: Asim Puri
## Date: 9/29/2023
##--------------------------------------------------------------

def main():
    flag = 'y'
    while flag == 'y':
        budget = tBudgetCall() 
        cost = expenseCall()
        tBudget = budget - cost
        answer(tBudget,cost,budget)
        flag = input('\nWant to enter another budget? (y/n)')

def tBudgetCall():
    budget = float(input("Enter your budget for the month: $"))
    return(budget)

def expenseCall():
    cost = 0
    flag = 'y'
    while flag == 'y':
        expense = float(input('Enter you expense: '))
        cost += expense
        flag = input('Would you like to enter another expense? (y/n)')
    return(cost)

def answer(tBudget,cost,budget):
    if tBudget == 0:
        print('You are at equilibrium. \n\nHere is your remaining budget for the month: $',format(tBudget,',.2f'),
            '\nHere is your total cost for the month $',format(cost,',.2f'), sep='')
    elif tBudget < 0 :
        print('You went over the budget.\n\nHere is your remaining budget for the month: $',format(tBudget,',.2f'),
            '\nHere is your total cost for the month $',format(cost,',.2f'), sep='')
    elif tBudget < budget:
        print('You are under the budget.\n\nHere is your remaining budget for the month: $',format(tBudget,',.2f'),
            '\nHere is your total cost for the month $',format(cost,',.2f'), sep='')

main()
print('\n~~~~ Good By ~~~~\n')