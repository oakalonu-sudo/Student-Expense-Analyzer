def read_file(filename):
    '''Reads expense file and returns a list of lists with date,category,
    description and amount in single list'''
    expenses = []
    with open(filename, 'r') as file:
        content = file.readlines()

        content.pop(0)

        
        for line in content:
            line = line.strip()

            if line:
                line = line.split(',')
                line[3] = float(line[3])
                expenses.append(line)
        
    return expenses

def count_expenses(expenses):
    count = 0
    for line in expenses:
        count += 1
    return count 

def total_calc(expenses):

    total = 0
    for line in expenses:
        total += line[3]
    return total

def average_calc(total, count):

    average = total/count

    return average

def find_smallest(expenses):

    smallest = expenses[0][3]
    for i in range(1,len(expenses)):
        amount = expenses[i][3]
        if amount < smallest:
            smallest = amount
            details = expenses[i][:3]
    return f'${smallest} -> {' - '.join(details)}'


def find_largest(expenses):

    largest = expenses[0][3]
    for i in range(1,len(expenses)):
        amount = expenses[i][3]
        if amount > largest:
            largest = amount
            details = expenses[i][:3]
    return f'${largest} -> {' - '.join(details)}'

def category_sort(expenses):
    '''Returns a dictionary of category as key and other
      details as a list of values'''

    category_dic = {}
    for line in expenses:
        category = line[1]
        new_line = []
        if category in category_dic:
            new_line.extend([line[0],line[2],line[3]])
            category_dic[category].append(new_line)
        else:
            new_line.extend([line[0],line[2],line[3]])
            category_dic[category] = [new_line]

    return category_dic

def category_expenses(all_categories):
    '''Returns a dictionary of category as key and amount as value'''

    analysis_dic = {}
    

    for category,detail in all_categories.items():
        category_amount = 0
        for i in detail:
            category_amount += i[2]

        analysis_dic[category] = category_amount
    return analysis_dic

def count_per_category(all_categories):

    count_dic = {}

    for category, details in all_categories.items():
        count_dic[category] = len(details)

    return count_dic

def highest_category(analysis_dic):

    highest = max(analysis_dic.values())
    largest_cat = []

    for category,amount in analysis_dic.items():
        if amount == highest:
            largest_cat.append(category)
    return f'{','.join(largest_cat)}: {highest: .2f}'

def lowest_category(analysis_dic):

    smallest = min(analysis_dic.values())
    smallest_cat = []

    for category,amount in analysis_dic.items():
        if amount == smallest:
            smallest_cat.append(category)
    return f'{','.join(smallest_cat)}: {smallest: .2f}'


def average_expense_cat(analysis_dic,all_categories):
    '''Calculates the average expense for the categories'''

    total = 0
    average = 0

    for amount in analysis_dic.values():
        total += amount
    average = total/len(all_categories)

    return average

def month_sort(expenses):
    '''Returns a dictionary of month as key and details as values'''

    month_dic = {}

    for line in expenses:
        date = line[0]
        month = date[:2]
        if month in month_dic:
            month_dic[month].append(line)
        else:
            month_dic[month] = [line]

    return month_dic

def month_total(month_dic):

    month_total_dic = {}

    for month,details in month_dic.items():
        for i in details:
            if month in month_total_dic:
                month_total_dic[month] += i[3]
            else:
                month_total_dic[month] = i[3]
    return month_total_dic

def highest_month(month_total_dic):

    highest = max(month_total_dic.values())
    
    for month,amount in month_total_dic.items():
        if highest == amount:
            highest_month = month
    return f'{highest_month} - ${highest}'

def lowest_month(month_total_dic):

    lowest = min(month_total_dic.values())

    for month,amount in month_total_dic.items():
        if lowest == amount:
            lowest_month = month
    return f'{lowest_month} - ${lowest}'

def avg_expense_month(month_dic,month_total_dic):
    '''Returns a dic of key as month and values as average expense'''

    avg_dic = {}

    for month,details in month_dic.items():
        avg_dic[month] = month_total_dic[month]/len(details)
    return avg_dic            

def main():
    expenses = read_file('expense.csv')
    #print(expenses)

    total = total_calc(expenses)
    count = count_expenses(expenses)
    average = average_calc(total,count)
    smallest = find_smallest(expenses)
    largest = find_largest(expenses)
    all_categories = category_sort(expenses)
    analysis_dic = category_expenses(all_categories)
    month_dic = month_sort(expenses)
    month_total_dic = month_total(month_dic)

    #print(all_categories)

    view_menu = True
    
    menu ="1.Total number of expenses\n2.Find out total amount spent on expenses\n3.Find out average amount spent on expenses\n4.Smallest expense\n5.Largest expense\n6.Category analysis\n7.Month analysis\n8.Exit \n"

    category_menu = "1.Total expenses per category\n2.Expenses count per category\n3.Highest category expense\n4.Lowest category expense\n5.Average expense of categories\n6.Return to main menu\n"

    month_menu = "1.All expenses for each month\n2.Total amount of expenses for each month\n3.Highest spending month\n4.Lowest spending month\n5.Average expense per month\n6.Return to main menu\n"

    while view_menu:
        print(menu)
        
        request = input("Choose an option from the menu: ")

        if request == "1":
            print(f"Total number of expenses: {count}\n")
        elif request == "2":
            print(f"Total amount spent on expenses: {total: .2f}\n")
        elif request == "3":
            print(f"Average expense amount: {average: .2f}\n")
        elif request == "4":
            print(f"Smallest expense: {smallest}\n")
        elif request == "5":
            print(f"Largest expense: {largest}\n")
        elif request == "6":

            category_view = True

            while category_view:
                print(category_menu)
                
                category_opt = input("Choose an option from the category menu: ")

                if category_opt == "1":
                    print(f"Total expenses for each category: {analysis_dic}\n")
                elif category_opt == "2":
                    print(f"{count_per_category(all_categories)}\n")
                elif category_opt == "3":
                    print(f'{highest_category(analysis_dic)}\n')
                elif category_opt == "4":
                    print(f'{lowest_category(analysis_dic)}\n')
                elif category_opt == '5':
                    print(f'Average expense of categories: {average_expense_cat(analysis_dic,all_categories): .2f}\n')
                elif category_opt == "6":
                    category_view = False
                else:
                    print("Invalid input\n")

        elif request == "7":
            month_view = True

            while month_view:
                print(month_menu)

                month_opt = input("Choose an option from the month menu: ")

                if month_opt == "1":
                    print(f"\nExpenses for each month: {month_sort(expenses)}\n")
                elif month_opt == "2":
                    print(f"Total amount of expenses for each month: {month_total(month_dic)}\n")
                elif month_opt == "3":
                    print(f'Month with highest total spending: {highest_month(month_total_dic)}\n')
                elif month_opt == "4":
                    print(f'Month with lowest total spending: {lowest_month(month_total_dic)}\n')
                elif month_opt == "5":
                    print(f"Average expense per month: {avg_expense_month(month_dic,month_total_dic)}\n")
                elif month_opt == "6":
                    month_view = False
                else:
                    print("Invalid input")


        elif request == "8":
            view_menu = False
        else:
            print("Invalid input")

    
if __name__ == '__main__':
    main()