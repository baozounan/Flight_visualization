import pymysql
con =pymysql.connect(

           host = '127.0.0.1',

           port =3306,

           user = 'root',

           password = '123456',

           db = 'flight_visualization',

           charset = 'utf8'
)
cur=con.cursor() #建立游标
row = cur.execute('show tables') #利用游标执行sql语句
print(row)
all = cur.fetchall() # 利用游标进行数据的读取
print(all)
cur.execute("insert test0 value(1,‘小王’)") #插入数据时要提交事务
con.commit()
cur.executemany("INSERT test0 VALUE(%s,%s)",[(2,'小白'),(3,'小五')]) # 插入多条值
con.commit()
cur.close()#先关闭游标
con.close()#再关闭连接