import sqlite3

con = sqlite3.connect('testing.db')
cur = con.curser()
cur.execute("create table test(sno text, name text)")
for i in cur.execute("select * from test"):
  print(i)
