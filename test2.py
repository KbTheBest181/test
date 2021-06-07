import sqlite3

con = sqlite3.connect('DustMiningBot.db')
cur = con.cursor()
#cur.execute("create table test(sno text, name text)")
#cur.execute("insert into test(1, Bhattu)")
#con.commit()
for i in cur.execute("select * from admins"):
  print(i)
