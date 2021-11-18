import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    port = "3306",
    password = "",
    database ="store_cms_plusplus"
)
mycursor = mydb.cursor()
"""Viết tính năng thống kê số lượng loại máy tính của mỗi hãng, sắp xếp theo số lượng giảm dần
Expect output:
- Tên hàm: getCounterByMaker()
- Trả về: List<Counter> counters

- Lớp Counter (maker, quantity)
"""
class Counter:
    def __init__(self, maker, quantity):
        self.maker = maker
        self.quantity = quantity
    def __str__(self):
        return "Maker: %s, Quantity: %s" % (self.maker, self.quantity)

def getCounterByMaker():
    str = "select maker, count(maker) 'quantity' from laptop group by maker order by quantity desc;"
    mycursor.execute(str)
    myresult = mycursor.fetchall()
    list = []
    for x in myresult:
        counter = Counter(x[0], x[1])
        list.append(counter)
    print(list)
    for x in list:
        print(x)

getCounterByMaker()





