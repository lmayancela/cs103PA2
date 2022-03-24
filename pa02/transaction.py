import sqlite3

def to_cat_dict(cat_tuple):
    cat = {'rowid':cat_tuple[0], 'item#':cat_tuple[1], 'amount':cat_tuple[2], 'category':cat_tuple[3], 'date':cat_tuple[4], 'description':cat_tuple[5]}
    return cat

def to_cat_dict_list(cat_tuples):
    return [to_cat_dict(cat) for cat in cat_tuples]

class Transaction():

    def __init__(self,file_name):
        con= sqlite3.connect(dbfile)
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS categories
                    (item# int,amount int,category text,date text,description text)''')
        con.commit()
        con.close()
        self.dbfile = dbfile

    def show(self):
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("select year,sex,count(*) from names2K where year>2004 and year<2010 group by year, sex order by year")
        toReturn = *cur.fetchall(), sep = "\n"
        con.commit()
        con.close()
        return toReturn

    def add(self,item):
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("INSERT INTO categories VALUES(?,?,?,?,?)",(item['item#'],item['amount'],item['category'],item['date'],item['description']))
        con.commit()
        cur.execute("SELECT last_insert_rowid()")
        last_rowid = cur.fetchone()
        con.commit()
        con.close()
        return last_rowid[0]

    def delete(self,rowid):
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('''DELETE FROM categories
                       WHERE rowid=(?);
        ''',(rowid,))
        con.commit()
        con.close()

    def date(self):

    def month(self):

    def year(self):

    def category(self):
