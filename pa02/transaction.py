'''
docstring?
'''
import sqlite3

def to_cat_dict(cat_tuple):
    '''
    put a docstring here
    '''
    cat = {'rowid':cat_tuple[0], 'itemnum':cat_tuple[1], 'amount':cat_tuple[2],
    'category':cat_tuple[3], 'date':cat_tuple[4], 'description':cat_tuple[5]}
    return cat

def to_cat_dict_list(cat_tuples):
    '''
    put a docstring here
    '''
    return [to_cat_dict(cat) for cat in cat_tuples]

class Transaction():
    '''
    put a docstring here
    '''

    def __init__(self,dbfile):
        '''
    put a docstring here
    '''
        con= sqlite3.connect(dbfile)
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS transactions
                    (itemnum int,amount float,category text,
                    date text,day text, month text, year text,
                    description text)''')
        con.commit()
        con.close()
        self.dbfile = dbfile

    def show(self):
        '''
    put a docstring here
    '''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("SELECT rowid,itemnum,amount,category,date,description from transactions")
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_cat_dict_list(tuples)

    def add(self,item):
        '''
    put a docstring here
    '''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("INSERT INTO transactions VALUES(?,?,?,?,?,?,?,?)",
        (item['itemnum'],item['amount'],item['category'], item['date'],item['day'],item['month'],item['year'],item['description']))
        con.commit()
        cur.execute("SELECT last_insert_rowid()")
        last_rowid = cur.fetchone()
        con.commit()
        con.close()
        return last_rowid[0]

    def delete(self,rowid):
        '''
    put a docstring here
    '''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('''DELETE FROM transactions
                       WHERE rowid=(?);
        ''',(rowid,))
        con.commit()
        con.close()

    def date(self):
        '''
    put a docstring here
    '''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('''SELECT rowid,itemnum,amount,category,
        date,description from transactions order by year''')
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_cat_dict_list(tuples)

    def month(self):
        '''
    put a docstring here
    '''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('''SELECT rowid,itemnum,amount,category,date,
        description from transactions order by month''')
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_cat_dict_list(tuples)

    def year(self):
        '''
    put a docstring here
    '''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('''SELECT rowid,itemnum,amount,category,date,
        description from transactions order by day''')
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_cat_dict_list(tuples)

    def category(self):
        '''
    put a docstring here
    '''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('''SELECT rowid,itemnum,amount,category,date,
        description from transactions order by category''')
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_cat_dict_list(tuples)
