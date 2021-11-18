import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    port = "3306",
    password = "",
    database ="store_cms_plusplus"
)
#Expect Output:
#Tên hàm: getStatisticByMaker()
#Trả về: List<Statistic> statistic;

#Lớp: Statistic(maker, sold, totalMoney)

mycursor = mydb.cursor()
class Statistic :
    def __init__(self, maker, sold, totalmoney):
        self.maker = maker
        self.sold = sold
        self.totalmoney = totalmoney
    def __str__(self):
        return "maker = %s, sold = %s, totalmoney = %s" % (self.maker, self.sold,self.totalmoney)
def getStatisticByMaker():
    str = "select maker, sum(sold), sum(sold*price) 'totalMoney' from laptop group by maker ;"
    mycursor.execute(str)
    myresult = mycursor.fetchall()
    list = []
    for x in myresult:
        statistic = Statistic(x[0], x[1], x[2])
        list.append(x)
    print(list)
    for x in list:
        print(x)

getStatisticByMaker()
