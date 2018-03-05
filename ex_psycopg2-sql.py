# SQL in Python using PostGres and the psycopg2 library



import psycopg2
from datetime import datetime

conn = psycopg2.connect(dbname='socialmedia', user='postgres', host='/tmp')
c = conn.cursor()

ts = datetime.strptime(today, '%Y-%m-%d').strftime("%Y%m%d")
today = '2014-08-14'

# This is not strictly necessary but demonstrates how you can convert a date
# to another format
ts = datetime.strptime(today, '%Y-%m-%d').strftime("%Y%m%d")

c.execute(
    '''CREATE TABLE logins_7d AS
    SELECT userid, COUNT(*) AS cnt, timestamp %(ts)s AS date_7d
    FROM logins
    WHERE logins.tmstmp > timestamp %(ts)s - interval '7 days'
    GROUP BY userid;''', {'ts': ts}
)

c.execute(
    '''DROP TABLE IF EXISTS logins_7d_web;CREATE TABLE logins_7d_web AS
    SELECT userid, COUNT(*) AS cnt, timestamp %(ts)s AS date_7d_web
    FROM logins
    WHERE logins.tmstmp > timestamp %(ts)s - interval '7 days' and type ='web'
    GROUP BY userid;''', {'ts': ts}
)


conn.commit()
conn.close()



# In postgres
CREATE USER ender WITH ENCRYPTED PASSWORD 'bugger';
CREATE DATABASE golf WITH OWNER ender;



### Query2
import psycopg2
import getpass

upass = getpass.getpass()
conn = psycopg2.connect(database="golf", user="ender", password=upass, host="localhost", port="5432")
print("connected")

cur = conn.cursor()

cur.fetchone()

#fetchmany(n) to get n rows
cur.fetchmany(10)

cur = conn.cursor()
query = '''
        SELECT *
        FROM golf
        LIMIT 30;
        '''

cur.execute(query)
results = cur.fetchall() # fetchall() grabs all remaining rows
type(results[0])
ur.execute(query)
for record in cur:
    print ("date:{}, outlook:{}, temperature:{}".format(record[0], record[1], record[2]))


query = "SELECT count(*) FROM golf;"
upass = getpass.getpass()

with psycopg2.connect(database="golf", user="ender", password=upass, host="localhost", port="5432") as conn:
    with conn.cursor() as curs:
        print("Cursor inside with block: {}".format(curs))
        curs.execute(query)
    print("Cursor outside with block: {}".format(curs))

print ("Old record count: {}".format(record_count))

cur.execute('SELECT count(*) FROM golf;')
record_count = cur.fetchone()[0]

print("New record count: {}".format(record_count))


date_cut = "2014-08-01; DROP TABLE logins" # The user enters a date in a field on a web form
horribly_risky = "SELECT * FROM logins WHERE tmstmp > {};".format(date_cut)
print (horribly_risky)

### SQL Injection
date_cut = "2014-08-01; DROP TABLE logins" # The user enters a date in a field on a web form
horribly_risky = "SELECT * FROM logins WHERE tmstmp > {};".format(date_cut)
print (horribly_risky)

### Practice safe SQL with Psycopg2

>>> SQL = "INSERT INTO authors (name) VALUES (%s);"
>>> data = ("O'Reilly", )
>>> cur.execute(SQL, data) # Note: no % operator


conn.rollback()

cur.execute('SELECT count(*) FROM golf;')
record_count = cur.fetchone()[0]

print ("After rollback: {}".format(record_count))


conn.commit()
conn.close()
conn.close()
conn

