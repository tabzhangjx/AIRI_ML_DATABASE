import os
import pymysql

#Create the database
#??Make sure to create the database at the server first
#use basename
db = pymysql.connect(host="localhost", port=3306, user="root", passwd="tab123456", db="IAIR_1", charset='utf8')#connect to database
cr=db.crusor()

#create table

sql = "CREAT TABLE DATA(FILE_PATH varchar(100), A varchar(30), B varchar(30), C varchar(30), D varchar(30));"

cr.execute(sql)

#input the data
dir=input('Please input the path')
filename=os.listdir(dir)
for temp in filename:
    labels=temp.split('_') #return four labels as a list
    #Fill in the table
    for temp2 in labels:
        sql="INSERT INTO DATA VALUES (%s,%s,%s,%s,%s)"%(dir+'/'+temp,labels(0),labels(1),labels(2),labels(3))
        print(label(0))
        cr.execute(sql)
#end the connection
db.commit()
db.close()
