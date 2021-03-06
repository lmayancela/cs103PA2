#! /opt/miniconda3/bin/python3
'''
tracker is an app that maintains a list of personal
financial transactions.

It uses Object Relational Mappings (ORM)
to abstract out the database operations from the
UI/UX code.

The ORM, Category, will map SQL rows with the schema
  (rowid, category, description)
to Python Dictionaries as follows:

(5,'rent','monthly rent payments') <-->

{rowid:5,
 category:'rent',
 description:'monthly rent payments'
 }

Likewise, the ORM, Transaction will mirror the database with
columns:
amount, category, date (yyyymmdd), description

In place of SQL queries, we will have method calls.

This app will store the data in a SQLite database ~/tracker.db

Note the actual implementation of the ORM is hidden and so it
could be replaced with PostgreSQL or Pandas or straight python lists

'''
from category import Category
from transaction import Transaction

transactions = Transaction('tracker.db')
category = Category('tracker.db')


# here is the menu for the tracker app

MENU = '''
0. quit
1. show categories
2. add category
3. modify category
4. show transactions
5. add transaction
6. delete transaction
7. summarize transactions by date
8. summarize transactions by month
9. summarize transactions by year
10. summarize transactions by category
11. print this menu
'''




def process_choice(choice):
    '''
    put a docstring here
    '''

    if choice=='1':
        cats = category.select_all()
        print_categories(cats)
    elif choice=='2':
        name = input("category name: ")
        desc = input("category description: ")
        cat = {'name':name, 'desc':desc}
        category.add(cat)
    elif choice=='3':
        print("modifying category")
        rowid = int(input("rowid: "))
        name = input("new category name: ")
        desc = input("new category description: ")
        cat = {'name':name, 'desc':desc}
        category.update(rowid,cat)
    elif choice == '4':
        trans = transactions.show()
        print_transactions(trans)
    elif choice == '5':
        itemnum = input("new transaction item#: ")
        amount = input("new transaction amount: ")
        category_type = input("new transaction category: ")
        description = input("new transaction description: ")
        year = input("what year was this transaction made: ")
        month = input("which month (numerical like 03 for March): ")
        day = input("which day (as a two-digit number like 03): ")
        trans = {'itemnum':itemnum,'amount':amount,'category':category_type,'date':
         year+'-' +month+'-'+day,'day':day,'month':month,'year':year,'description':description}
        transactions.add(trans)
    elif choice == '6':
        row_id = int(input("Provide ID of transaction to be deleted: "))
        print("Deleting Element with ID: "+ str(row_id))
        transactions.delete(row_id)
    elif choice == '7':
        print_transactions(transactions.date())
    elif choice == '8':
        print_transactions(transactions.month())
    elif choice == '9':
        print_transactions(transactions.year())
    elif choice == '10':
        print_transactions(transactions.category())
    elif choice == '11':
        print(MENU)
    else:
        choice = '0'
        return choice

    choice = input("> ")
    return choice


def toplevel():
    ''' handle the user's choice '''
    print(MENU)
    choice = input("> ")
    while choice !='0' :
        choice = process_choice(choice)
    print('bye')

#
# here are some helper functions
#

def print_transactions(items):
    ''' print the transactions '''
    if len(items)==0:
        print('no items to print')
        return
    print('\n')
    print("%-10s %-10s %-10s %-10s %-10s %-30s"%(
        'row_id','item #','amount','category','date','description'))
    print('-'*100)
    for item in items:
        values = tuple(item.values())
        print("%-10s %-10s %-10d %-10s %-10s %-30s"%
        (values[0], values[1], values[2], values[3], values[4], values[5]))

def print_category(cat):
    '''
    put a docstring here
    '''
    print("%-3d %-10s %-30s"%(cat['rowid'],cat['name'],cat['desc']))

def print_categories(cats):
    '''
    put a docstring here
    '''
    print("%-3s %-10s %-30s"%("id","name","description"))
    print('-'*45)
    for cat in cats:
        print_category(cat)


# here is the main call!

toplevel()
