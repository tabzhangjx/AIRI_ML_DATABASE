import os
import pymysql

#Create the database
#??Make sure to create the database at the server first
#use basename
db = pymysql.connect("localhost","testuser","testcode","basename" )#connect to database
cr=db.crusor()

nums=input("how much items do you want:")

sql="SELECT 'a', count(*) from  "