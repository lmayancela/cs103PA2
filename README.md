# CS103a Spring 22

# PA02: tracker.py and the Transaction class

This app uses an SQL database to store transaction history using a tracker. This is able to add, remove, change, and sort information within the database for easy access and viewing.

This is the music that got us through it
https://www.youtube.com/watch?v=kfVsfOSbJY0

'''bash
Script started on Thu Mar 24 23:15:30 2022
[1m[7m%[27m[1m[0m                                                                               
 
]7;file://chromebookpro16.dyn.brandeis.edu/Users/marco/desktop/COSI103/cs103PA2
[0m[27m[24m[J(base) marco@chromebookpro16 cs103PA2 % [K[?2004hccd c  ppylinbt  t transaction.py[?2004l

************* Module transaction.py
transaction.py:1:0: F0001: No module named transaction.py (fatal)
[1m[7m%[27m[1m[0m                                                                               
 
]7;file://chromebookpro16.dyn.brandeis.edu/Users/marco/desktop/COSI103/cs103PA2
[0m[27m[24m[J(base) marco@chromebookpro16 cs103PA2 % [K[?2004hccd pa02[?2004l

[1m[7m%[27m[1m[0m                                                                               
 
]7;file://chromebookpro16.dyn.brandeis.edu/Users/marco/desktop/COSI103/cs103PA2/pa02
[0m[27m[24m[J(base) marco@chromebookpro16 pa02 % [K[?2004hcd pa02pylint transaction.py[?2004l


-------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 5.86/10, +4.14)

[1m[7m%[27m[1m[0m                                                                               
 
]7;file://chromebookpro16.dyn.brandeis.edu/Users/marco/desktop/COSI103/cs103PA2/pa02
[0m[27m[24m[J(base) marco@chromebookpro16 pa02 % [K[?2004hppylint tracker.py[?2004l

************* Module tracker
tracker.py:134:10: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
tracker.py:139:14: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
tracker.py:146:10: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
tracker.py:152:10: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)

-----------------------------------
Your code has been rated at 9.47/10

[1m[7m%[27m[1m[0m                                                                               
 
]7;file://chromebookpro16.dyn.brandeis.edu/Users/marco/desktop/COSI103/cs103PA2/pa02
[0m[27m[24m[J(base) marco@chromebookpro16 pa02 % [K[?2004hppap  ppytest -q test_transc action.py[?2004l

[32m.[0m[32m.[0m[32m.[0m[32m                                                                      [100%][0m
[32m[32m[1m3 passed[0m[32m in 0.09s[0m[0m
[1m[7m%[27m[1m[0m                                                                               
 
]7;file://chromebookpro16.dyn.brandeis.edu/Users/marco/desktop/COSI103/cs103PA2/pa02
[0m[27m[24m[J(base) marco@chromebookpro16 pa02 % [K[?2004hppytest -q       p  ppython trak cker.py[1m [0m[0m [?2004l


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

> 4
no items to print
> 5
new transaction item#: 20
new transaction amount: 200
new transaction category: Home
new transaction description: Premiunm    m Couch  
what year was this transaction made: 2020
which month (numerical like 03 for March): 12
which day (as a two-digit number like 03): 02
> 4


row_id     item #     amount     category   date       description                   
----------------------------------------------------------------------------------------------------
1          20         200        Home       2020-12-02 Premium Couch                 
> 5
new transaction item#: 30  22
new transaction amount: 400
new transaction category: Pets
new transaction description: Shiba Inu Pup
what year was this transaction made: 2022
which month (numerical like 03 for March): 05
which day (as a two-digit number like 03): 22
> 4


row_id     item #     amount     category   date       description                   
----------------------------------------------------------------------------------------------------
1          20         200        Home       2020-12-02 Premium Couch                 
2          22         400        Pets       2022-05-22 Shiba Inu Pup                 
> 6
Provide ID of transaction to be deleted: 1
Deleting Element with ID: 1
> 4


row_id     item #     amount     category   date       description                   
----------------------------------------------------------------------------------------------------
2          22         400        Pets       2022-05-22 Shiba Inu Pup                 
> 11

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

> 7


row_id     item #     amount     category   date       description                   
----------------------------------------------------------------------------------------------------
2          22         400        Pets       2022-05-22 Shiba Inu Pup                 
> 8 5
new transaction item#: 80
new transaction amount: 100
new transaction category: test
new transaction description: test
what year was this transaction made: 2000
which month (numerical like 03 for March): 10
which day (as a two-digit number like 03): 10
> 5
new transaction item#: 75
new transaction amount: 3000 
new transaction category: test
new transaction description: test
what year was this transaction made: 2018
which month (numerical like 03 for March): 12 1
which day (as a two-digit number like 03): 24
> 11

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

> 7


row_id     item #     amount     category   date       description                   
----------------------------------------------------------------------------------------------------
3          80         100        test       2000-10-10 test                          
4          75         300        test       2018-11-24 test                          
2          22         400        Pets       2022-05-22 Shiba Inu Pup                 
> 8


row_id     item #     amount     category   date       description                   
----------------------------------------------------------------------------------------------------
2          22         400        Pets       2022-05-22 Shiba Inu Pup                 
3          80         100        test       2000-10-10 test                          
4          75         300        test       2018-11-24 test                          
> 9


row_id     item #     amount     category   date       description                   
----------------------------------------------------------------------------------------------------
3          80         100        test       2000-10-10 test                          
4          75         300        test       2018-11-24 test                          
2          22         400        Pets       2022-05-22 Shiba Inu Pup                 
> 10


row_id     item #     amount     category   date       description                   
----------------------------------------------------------------------------------------------------
2          22         400        Pets       2022-05-22 Shiba Inu Pup                 
3          80         100        test       2000-10-10 test                          
4          75         300        test       2018-11-24 test                          
> 0
bye
[1m[7m%[27m[1m[0m                                                                               
 
]7;file://chromebookpro16.dyn.brandeis.edu/Users/marco/desktop/COSI103/cs103PA2/pa02
[0m[27m[24m[J(base) marco@chromebookpro16 pa02 % [K[?2004hqquit[?2004l

zsh: command not found: quit
[1m[7m%[27m[1m[0m                                                                               
 
]7;file://chromebookpro16.dyn.brandeis.edu/Users/marco/desktop/COSI103/cs103PA2/pa02
[0m[27m[24m[J(base) marco@chromebookpro16 pa02 % [K[?2004heexit[?2004l


Saving session...
...copying shared history...
...saving history...truncating history files...
...completed.
Deleting expired sessions...none found.

Script done on Thu Mar 24 23:21:36 2022

'''






