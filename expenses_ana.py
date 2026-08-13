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
    return smallest


def find_largest(expenses):

    largest = expenses[0][3]
    for i in range(1,len(expenses)):
        amount = expenses[i][3]
        if amount > largest:
            largest = amount
    return largest

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
    


def main():
    expenses = read_file('expense.csv')
    print(expenses)

    total = total_calc(expenses)
    count = count_expenses(expenses)
    average = average_calc(total,count)
    smallest = find_smallest(expenses)
    largest = find_largest(expenses)
    all_categories = category_sort(expenses)
    analysis_dic = category_expenses(all_categories)
    print(count)
    print(total)
    print(average)
    print(smallest)
    print(largest)
    print(all_categories)
    print(analysis_dic)
    

if __name__ == '__main__':
    main()