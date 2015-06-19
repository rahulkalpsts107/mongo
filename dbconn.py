import pymongo
from pymongo import MongoClient

fruit = ['mango','apple','banana','mango','apple','grape']


def establish_conn_to_db():
    connection = MongoClient('localhost',27017)
    db=connection.test
    names = db.names
    items = names.find_one()
    print ('Table value is '+ items['name'])
    print_count()

def print_count():
    counts={}#initialze a dictionary
    for item in fruit:
        if item in counts:
            counts[item]=counts[item]+1
        else:
            counts[item]=1
    print(counts);
    #Exception Handling
    try:
        print (5/0)
    except Exception as e:
        print ("exception :")
        print (type(e))
        print(e)
    print("Life Goes on")

def insert_email():
    print()