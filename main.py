from colorama import Fore, Style
import datetime
import statistics

expenses = []
grouped_expenses = {}

print("Write an expense in the format" + Fore.CYAN + " name:price:category" + Fore.RESET, end='. ')
print("If you want to stop writing expenses, type '" + Fore.CYAN + "stop" + Fore.RESET + "'.")

# Main input
while True:
    user_input = input("— ").lower()
    splited_input = user_input.split(":")

    if user_input == "stop":
        if not expenses: print(Fore.RED + "You have not written any expense yet" + Fore.RESET) # If expenses list is empty
        else: break
    elif len(splited_input) == 3 and all(splited_input):
        if splited_input[1].isnumeric() and float(splited_input[1]) > 0:
            print(Fore.GREEN + f"Expense submitted ({splited_input[0]})" + Fore.RESET)
            expenses.append(splited_input)
        else:
            print(Fore.RED + "Your price is not a valid number. Your expense will not be submitted" + Fore.RESET)
    else:
        print(Fore.RED + "Invalid format. Your expense will not be submitted" + Fore.RESET)
        continue

# Group all expoenses by categories
for expense in expenses:
    name, price, category = expense
    if category not in grouped_expenses:
        grouped_expenses[category] = [(name, price)]  # Add new category and it's value
    else:
        grouped_expenses[category].append((name, price))  # Add new expense to existing category


print(Style.BRIGHT + Fore.MAGENTA + f"\nOVERALL EXPENSES" + Style.RESET_ALL, end="")
print(f"""
    ● Products: {', '.join([expense[0] for expense in expenses])}
    ● Overall price: {sum([float(expense[1]) for expense in expenses])}
    ● Average price: {statistics.mean([float(expense[1]) for expense in expenses])}""" + Style.RESET_ALL)

# Expenses by categories
print(Style.BRIGHT + Fore.MAGENTA + "\nEXPENSES BY CATEGORIES" + Style.RESET_ALL)
for category in grouped_expenses:
    names_in_category = []
    prices_in_category = []
    for expense in grouped_expenses[category]:
        names_in_category.append(expense[0])
        prices_in_category.append(float(expense[1]))

    print(f"""Category: {Fore.YELLOW + category.upper() + Fore.RESET}
    ● Products: {', '.join(names_in_category)}
    ● Overall price: {sum(prices_in_category)}
    ● Average price: {statistics.mean(prices_in_category)}""")


date_time = datetime.datetime.now()
print(Style.DIM + Fore.CYAN + "\nReport generated at " + date_time.strftime("%d.%m.%Y %H:%M:%S") + Style.RESET_ALL)
