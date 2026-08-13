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


def main():
    expenses = read_file('expense.csv')
    print(expenses)

    total = total_calc(expenses)
    count = count_expenses(expenses)
    average = average_calc(total,count)
    smallest = find_smallest(expenses)
    largest = find_largest(expenses)
    print(count)
    print(total)
    print(average)
    print(smallest)
    print(largest)
    

if __name__ == '__main__':
    main()