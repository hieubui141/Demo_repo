import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    port = "3306",
    password = "Fizz4321",
    database ="store_cms_plusplus"
)
mycursor = mydb.cursor()
mycursor.execute(" SELECT * FROM store_cms_plusplus.laptop WHERE ram BETWEEN 4 AND 8;")
myresult = mycursor.fetchall()
print(myresult)
mycursor.execute("select * from laptop where ram = 8 and ssd = 256;")
myresult = mycursor.fetchall()
print(myresult)
mycursor.execute("select * from store_cms_plusplus.laptop where sold > 30 order by sold desc;")
myresult = mycursor.fetchall()
print(myresult)

