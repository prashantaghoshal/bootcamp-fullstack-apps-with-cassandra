#!/usr/bin/env python3
import uuid
from connection import session

print('========================================')
print('Start exercise')
todo_items = []
try:
    output = session.execute("SELECT * FROM todoitems WHERE user_id = 'john';")
    for row in output:
        #print(str(row))
        print(row)
        session.execute(
        "INSERT INTO todoitems (user_id, item_id, completed, title) VALUES ('jack', row.item_id, row.completed, row.title);")
        #print(row.title)
        todo = ['jack', str(row.item_id), row.completed, row.title]
        todo_items.append(todo)
    """    
    for row in todo_items:
        print(row)
        print (",".join(row))
    """


except Exception as e:
    print(e)
    print('Failure')
else:
    print('Success')
print('========================================')


"""
print('========================================')
print('Start import')
try:
    session.execute(
        "INSERT INTO todoitems (user_id, item_id, completed, title) VALUES ( 'john', 11111111-5cff-11ec-be16-1fedb0dfd057, true, 'Walk the dog');")
    session.execute(
        "INSERT INTO todoitems (user_id, item_id, completed, title) VALUES ( 'john', 22222222-5cff-11ec-be16-1fedb0dfd057, false, 'Have lunch tomorrow');")
    session.execute(
        "INSERT INTO todoitems (user_id, item_id, completed, title) VALUES ( 'mary', 33333333-5cff-11ec-be16-1fedb0dfd057, true, 'Attend the workshop');")
except Exception as e:
    print(e)
    print('Failure')
else:
    print('Success')
print('========================================')

"""