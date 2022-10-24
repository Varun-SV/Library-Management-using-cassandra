from sqlite3 import Cursor
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from cassandra.query import SimpleStatement

usercreds = PlainTextAuthProvider(username='', password='')
cursor = Cluster(['127.0.0.1'], auth_provider=usercreds)
session = cursor.connect()
# print(type(session))
# print(session)
try:
    session
    # c=session.execute("SELECT * FROM test.test")
    print('Connected to Cassandra')
    # c = session.execute("use experiment")
    cursor2 = session.execute("use experiment;")
    print('Using keyspace experiment')
    cursor2 = session.execute("CREATE TABLE data (id int PRIMARY KEY, firstname text, lastname text);")
    print('Created table data')
    cursor2 = session.execute("INSERT INTO data (id, firstname, lastname) VALUES (1, 'John', 'Doe');")
    print('Inserted data into table data')
    cursor2 = session.execute("SELECT * FROM data;")
    print('Selected data from table data')
    for i in cursor2:
        print(i)
    # # cursor2 = session.execute('use testcse;')
    # cursor2 = session.execute('insert into data (id,firstname,lastname) values (1, "John", "Doe");')
    # cursor2 = session.execute('SELECT * FROM data;')
    # for i in cursor2:
    #     print(i)

except:
    print('Connection failed')
    # print("Creating new keyspace")
    # cursor2 = session.execute("CREATE KEYSPACE experiment WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};")

finally:
    print("Closing connection")
    cursor.shutdown()
