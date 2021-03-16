import mysql.connector

passwd= input(str("Enter The Database password"))
file = open('libs/dll/temp/do not delete.txt', 'w')
file.write(passwd)
file.close()
con = mysql.connector.connect(host="localhost", user="root", password=passwd)
cur = con.cursor()
cur.execute("CREATE DATABASE shop")
print("Database Created Successfully")
con.commit()