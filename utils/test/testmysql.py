from utils.mysqlHelper import *
mysqlconfig = {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'root',
        'passwd': '123456',
        'charset':'utf8',
        'database':'smsdb',
        'cursorclass':pymysql.cursors.DictCursor
        }
conn= MysqldbHelper(mysqlconfig)
print(conn.getVersion())
db_name="testdb"
conn.createDataBase(db_name)
conn.selectDataBase(db_name)
TABLE_NAME="testtable"
"""attrdict = {
        'name':'varchar(30) NOT NULL'
    }
constraint = "PRIMARY KEY(`id`)"
conn.creatTable(TABLE_NAME,attrdict,constraint)
"""
print("========= 单条数据插入 ===========")
params = {}
for i in range(5):
    params.update({"name":"testuser"+str(i)}) # 生成字典数据，循环插入
    print(params)
    conn.insert(TABLE_NAME, params)

