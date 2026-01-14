#BUDGET HANDLING
try:
    with open('budget.txt', 'r') as f:
        monthly_budget = float(f.read())

except FileNotFoundError:
    monthly_budget = float(input('Enter your monthly budget (positive number): '))

    if monthly_budget <= 0:
        print('Monthly budget must be positive')
        exit()
    with open('budget.txt', 'w') as f:
        f.write(str(monthly_budget))


#MENU LOOP
active_date = None  
while True:
    print('\n1: Enter a new date')
    print('2: Add expense in running date')
    print('3: Exit')

    a = int(input('Select your option: '))

    if a == 1:
        active_date = input('Enter date (YYYY-MM-DD): ')
        print(f'Active date set to {active_date}')

    elif a == 2:
        if active_date is None:
            print('Please give date first')

        else:
            category = input('Enter category: ')
            amount_spent = float(input(f'Enter amount spent in {category}: '))

            if amount_spent <= 0:
                print('Amount spent should be a positive number')

            else:
                with open('user1', 'a') as user1:
                    user1.write(f'{active_date}|{category}|{amount_spent}\n')
                print('Expense added successfully')
                total_spent = 0.0

                with open('user1', 'r') as user1:
                    for line in user1:
                        parts = line.strip().split('|')
                        if len(parts) == 3:          
                            total_spent += float(parts[2])

                remaining_balance = monthly_budget - total_spent

                print(f'Total spent: {total_spent}')
                print(f'Remaining balance: {remaining_balance}')

    elif a == 3:
        print('Exiting program')
        break

    else:
        print('Invalid option')

