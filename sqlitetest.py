import sqlite3
conn=sqlite3.connect("pets.db")
cursor=conn.cursor()

#version confirm
print(sqlite3.sqlite_version_info)
version=cursor.execute('SELECT sqlite_version()').fetchone()[0]
print(version)

#delete table
cursor.execute("""DROP TABLE IF EXISTS pets""")
conn.commit()

#create table
cursor.execute('''CREATE TABLE pets(
                  name VARCHAR(20),
                  owner VARCHAR(20),
                  species VARCHAR(20),
                  sex CHAR(1),
                  birth DATE,
                  death DATE)''')
#insert data
cursor.execute("INSERT INTO pets VALUES('Fluffy','Harold','cat','f','1993-02-04',NULL)")
cursor.execute("INSERT INTO pets VALUES('Claws','Gwen','cat','m','1994-03-17',NULL)")
cursor.execute("INSERT INTO pets VALUES('Buffy','Harold','dog','f','1989-05-13',NULL)")
cursor.execute("INSERT INTO pets VALUES('Fang','Benny','dog','m','1990-08-27',NULL)")
cursor.execute("INSERT INTO pets VALUES('Bower','Diane','dog','m','1995-08-31','1998-07-29')")
cursor.execute("INSERT INTO pets VALUES('Chirpy','Gwen','bird','f','1998-09-11',NULL)")
cursor.execute("INSERT INTO pets VALUES('Whistler','Gwen','bird','f','1997-12-09',NULL)")
cursor.execute("INSERT INTO pets VALUES('Slim','Benny','snake','m','1996-04-29',NULL)")
conn.commit()

#data search

print('{:=^50}'.format(''))
cursor.execute('select * from pets')
print(cursor.fetchone())# list형식

print('{:=^50}'.format(''))
print(cursor.fetchmany(3))  #튜플을 리스트로 묶어서

print('{:=^50}'.format(''))
print(cursor.fetchall())

#data search
print('{:=^50}'.format(''))
cursor.execute('select * from pets')
for row in cursor:
      print(row)
print('{:=^50}'.format(''))
for row in cursor.execute('select * from pets'):
      print(row)

#delete table
#cursor.execute('DROP TABLE pets')
cursor.close()
print('{:=^50}'.format(''))
conn = sqlite3.connect('pets.db')
with conn:
      cursor=conn.cursor()
      cursor.execute('select * from pets')
      rows=cursor.fetchall()
      for row in rows:
            print(row)
            
