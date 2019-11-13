import MySQLdb as mdb
import sys

con = mdb.connect('localhost', 'root', 'invalid', 'testDB');
cur = con.cursor()

try:
    sql = "SELECT * FROM `user`"
    cur.execute(sql)
    user = cur.fetchall()

    for val in user:
        print ("Nama : %s" %val[1])

except:
    print ("Select Data Gagal")

if con:    
    con.close()