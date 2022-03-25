'''
test_transaction runs unit and integration tests on the transaction module
'''

import pytest
from transaction import Transaction, to_cat_dict

@pytest.fixture
def dbfile(tmpdir):
    ''' create a database file in a temporary file system '''
    return tmpdir.join('test_tracker.db')

@pytest.fixture
def empty_db(dbfile):
    ''' create an empty database '''
    db = Transaction(dbfile)
    yield db


@pytest.fixture
def small_db(empty_db):
    ''' create a small database, and tear it down later'''
    cat1 = {'itemnum':2, 'amount':0,'category':'dudes', 
            'date':'ur mom', 'day': '01', 'month':'04','year':'2020','description':'sometimes i hate ppl'}
    cat2 = {'itemnum':69, 'amount':638,'category':'ur mom', 
            'date':'1/1/2001', 'day': '01', 'month':'04','year':'2020','description':'Im so tired of this hw'}
    cat3 = {'itemnum':2, 'amount':0,'category':'asians', 
            'date':'a girl', 'day': '01', 'month':'04','year':'2020','description':'git pull? why dont u pull some girls first'}
    id1=empty_db.add(cat1)
    id2=empty_db.add(cat2)
    id3=empty_db.add(cat3)
    yield empty_db
    empty_db.delete(id3)
    empty_db.delete(id2)
    empty_db.delete(id1)

@pytest.fixture
def med_db(small_db):
    ''' create a database with 10 more elements than small_db'''
    rowids=[]
    # add 10 categories
    for i in range(10):
        s = str(i)
        cat ={
               'itemnum':5, 
                'amount':20.0,
                'category':"deez nuts" +s, 
                'date':"2022-04-01", 
                'day':'01',
                'month':'04',
                'year':'2022',
                'description':'describe deez nuts on yo chin'+s
                }
        rowid = small_db.add(cat)
        rowids.append(rowid)

    yield small_db

    # remove those 10 categories
    for j in range(10):
        small_db.delete(rowids[j])



@pytest.mark.simple
def test_to_cat_dict():
    ''' teting the to_cat_dict function '''
    a = to_cat_dict((1, 2, 3, 'testcat', '4/1/2022', 'testdesc'))
    assert a['itemnum']==2
    assert a['amount']==3
    assert a['category']=='testcat'
    assert a['date']=='4/1/2022'
    assert a['description']=='testdesc'
    assert len(a.keys())==6


@pytest.mark.add
def test_add(med_db):
    ''' add a category to db, the select it, then delete it'''

    cat0 = {
            'itemnum':5, 
            'amount':20.0,
            'category':"deez nuts", 
            'date':"2022-04-01", 
            'day':'01',
            'month':'04',
            'year':'2022',
            'description':'describe deez nuts on yo chin'
            }
    cats0 = med_db.show()
    rowid = med_db.add(cat0)
    cats1 = med_db.show()
    assert len(cats1) == len(cats0) + 1



@pytest.mark.delete
def test_delete(med_db):
    ''' add a category to db, delete it, and see that the size changes'''
    # first we get the initial table
    cats0 = med_db.show()

    # then we add this category to the table and get the new list of rows
    cat0 = {'itemnum':5, 
            'amount':20.0,
            'category':"testing add", 
            'date':"2022-04-01", 
            'day':'01',
            'month':'04',
            'year':'2022',
            'description':'testing add'
            }
    rowid = med_db.add(cat0)
    cats1 = med_db.show()

    # now we delete the category and again get the new list of rows
    med_db.delete(rowid)
    cats2 = med_db.show()

    assert len(cats0)==len(cats2)
    assert len(cats2) == len(cats1)-1
