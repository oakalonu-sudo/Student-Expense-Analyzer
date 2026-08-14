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
    return f'{','.join(largest_cat)}: {highest}'

def lowest_category(analysis_dic):

    smallest = min(analysis_dic.values())
    smallest_cat = []

    for category,amount in analysis_dic.items():
        if amount == smallest:
            smallest_cat.append(category)
    return f'{','.join(smallest_cat)}: {smallest}'


def average_expense_cat(analysis_dic,all_categories):
    pass


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
    #print(all_categories)

    view_menu = True
    
    menu ="1.Total number of expenses\n2.Find out total amount spent on expenses\n3.Find out average amount spent on expenses\n4.Smallest expense\n5.Largest expense\n6.Category analysis\n7.Exit \n"

    category_menu = "1.Total expenses per category\n2.Expenses count per category\n3.Highest category expens\n4.Lowest category expense\n5.Return to main menu\n"

    while view_menu:
        print(menu)
        
        request = input("Choose an option from the menu: ")

        if request == "1":
            print(f"Total number of expenses: {count}\n")
        elif request == "2":
            print(f"Total amount spent on expenses: {total}\n")
        elif request == "3":
            print(f"Average expense amount: {average}\n")
        elif request == "4":
            print(f"Smallest expense: {smallest}\n")
        elif request == "5":
            print(f"Largest expense: {largest}\n")
        elif request == "6":

            category_view = True

            while category_view:
                print(category_menu)
                
                category_opt = input("Choose an option from the category menu: \n")

                if category_opt == "1":
                    print(f"Total expenses for each category: {analysis_dic}\n")
                elif category_opt == "2":
                    print(f"{count_per_category(all_categories)}\n")
                elif category_opt == "3":
                    print(f'{highest_category(analysis_dic)}\n')
                elif category_opt == "4":
                    print(f'{lowest_category(analysis_dic)}\n')
                elif category_opt == "5":
                    category_view = False
                else:
                    print("Invalid input\n")


        elif request == "7":
            view_menu = False
        else:
            print("Invalid input")

    
if __name__ == '__main__':
    main()