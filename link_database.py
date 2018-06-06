import pymysql

db = pymysql.connect("localhost","root","tab15963","RUNOOB")

cursor = db.cursor()

cursor.execute("SELECT VERSION()")

data = cursor.fetchone()

print("Database     %s" % data)


db.close()
