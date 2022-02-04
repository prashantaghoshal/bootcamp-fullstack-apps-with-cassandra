#!/usr/bin/env python3
import uuid
from connection import session

print('========================================')
print('Start exercise')

try:
    prepared_query = session.prepare("SELECT * FROM todoitems")
    output = session.execute(prepared_query)

    for row in output:
        prepared_insert = session.prepare("INSERT INTO todoitems (user_id, item_id, completed, title) VALUES (?,?,?,?)")
        session.execute(prepared_insert, ("tony", row.item_id, False, row.title))

except Exception as e:
    print(e)
    print('Failure')
else:
    print('Success')
print('========================================')
