import pymysql
mysqlconfig = {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'root',
        'passwd': '123456',
        'charset':'utf8',
        'database':'smsdb',
        'cursorclass':pymysql.cursors.DictCursor
        }