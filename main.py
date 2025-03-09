from colorama import Fore, Style
import datetime
import statistics
import os

expenses = []
grouped_expenses = {}
names = []
overall_prices = []

os.system('cls')

print("Write an expense in the format" + Fore.CYAN + " name:price:category" + Fore.RESET, end='. ')
print("If you want to stop writing expenses, type '" + Fore.CYAN + "stop" + Fore.RESET + "'.")


# Main input
while True:
    user_input = input("— ").lower()
    splited_input = user_input.split(":")  # ['name', 'price', 'category']

    if user_input == "stop":
        if not expenses:  # If expenses list is empty
            print(Fore.RED + "You have not written any expense yet" + Fore.RESET)
            continue
        else:
            break

    if len(splited_input) == 3 and all(splited_input):
        try:
            splited_input[1] = float(splited_input[1])  # Convert price to number
            print(Fore.GREEN + f"Expense submitted ({splited_input[0]})" + Fore.RESET)
            expenses.append(splited_input)
        except ValueError:  # If price is not a number
            print(Fore.RED + "Your price is not a number. Your expense will not be submitted" + Fore.RESET)
    else:  # If the format is wrong
        print(Fore.RED + "Invalid format. Your expense will not be submitted" + Fore.RESET)

# Group all expoenses by categories
for expense in expenses:
    name = expense[0];
    price = expense[1];
    category = expense[2];
    if category not in grouped_expenses:
        grouped_expenses[category] = [(name, price)]  # Add new category and it's value
    else:
        grouped_expenses[category].append((name, price))  # Add new expense to existing category

# Overall expenses
for category in grouped_expenses:
    for expense in grouped_expenses[category]:
        names.append(expense[0])
        overall_prices.append(float(expense[1]))


print(Style.BRIGHT + Fore.MAGENTA + f"\nOVERALL EXPENSES" + Style.RESET_ALL, end="")
print(f"""
    ● Products: {', '.join(names)}
    ● Overall price: {sum(overall_prices)}
    ● Average price: {statistics.mean(overall_prices)}""" + Style.RESET_ALL)

print(Style.BRIGHT + Fore.MAGENTA + "\nEXPENSES BY CATEGORIES" + Style.RESET_ALL)


# Expenses by categories
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


raw_time = datetime.datetime.now()
print(Style.DIM + Fore.CYAN + "\nReport generated at " + raw_time.strftime("%d.%m.%Y %H:%M:%S") + Style.RESET_ALL)
