''' 
Module      : MySQL_Interface
Author      : Ruthrapathy
Objective   : To connect to MySQL database and execute a SQL
Functions   : 1) Execute select statemnt
              2) Execute Insert/Update/Delete statement
'''

import mysql.connector as sql

HOST = 'localhost'
USER = 'root'
PASSWORD = 'sankaram'
DATABASE = "inventory"
PORT = 3306 # default is 3306. Port must be specified if it is not 3306

def Execute_Select(select_sql):
    '''
Function    : Execute_Select
Author      : Ruthrapathy
Objective   : To execute a select statment after connecting to MySQL
Inputs      : Properly formed select SQL statement
Returns     : a 3 variables containing 
              a) first element as status. True means success, False means fail
              b) second element as error message. Will have value only if status True is returned
              c) third element as list of data returned by select statement
Examples    : Here are some example on how to call the function
              import MySQL_Interface
              status, error_msg, data = MySQL_Interface.Execute_Select("select * from city")
                  
                  '''
    con = None
    cur = None
    status = True
    error_msg = ""
    data = []
    
    try:
        # 1) create a connector object by giving server/host, user-id, pwd and database
        msg = "Error trying to connect to database: "
        con = sql.connect (host=HOST, user=USER, passwd=PASSWORD, 
                       database=DATABASE, port=PORT)
        # 2) create a cursor
        msg = "Error creating cursor: "
        cur = con.cursor()
        # 3) Execute
        msg = "Error executing select statement: " + select_sql
        cur.execute(select_sql)
        # 4) Fetch data
        msg = "Error fetching data: "
        data = cur.fetchall()
        status = True
    except sql.Error as err:
        error_msg = msg + err.msg
        status = False
    finally:
        # 5) Now close open cur & con
        if cur is not None :
            cur.close()
        if con is not None:
            con.close()
    data_lst = Convert_Tuple_To_List (data)
    return status, error_msg, data_lst


def Execute_IUD(iud_sql):
    '''
Function    : Execute_IUD
Author      : Ruthrapathy
Objective   : To execute a insert/update/delete statment after connecting to MySQL in a Transaction
Inputs      : Properly formed insert/update/delete SQL string statement in a list
              iud_sql is a list containing 1 or more Insert/Update/Delete statements
Returns     : a 2 values containing 
              a) first element as status. True means success, False means fail
              b) second element as error message. Will have value only if status False is returned
Examples    : Here are some example on how to call the function
              import MySQL_Interface
              status, error_msg = MySQL_Interface.Execute_Select("insert into city (id, name, countrycode, district, population) values ({}, '{}', '{}', '{}', {})".format(5001, 'Afghanistan', 'AFG', 'test2', 7002))
                  
                  '''
    con = None
    cur = None
    status = True
    error_msg = ""
    
    try:
        # 1) create a connector object by giving server/host, user-id, pwd and database
        msg = "Error trying to connect to database: "
        con = sql.connect (host=HOST, user=USER, passwd=PASSWORD, 
                       database=DATABASE, port=PORT)
        # 2) create a cursor
        msg = "Error creating cursor: "
        cur = con.cursor()
        # start transaction
        con.start_transaction()
        # 3) Execute
        for sqls in iud_sql:
            msg = "Error executing select statement: " + sqls
            cur.execute(sqls)
        # 4) if it comes here, ==> status ==> commit data
        msg = "Error while committing data: "
        con.commit()
        status = True
    except sql.Error as err:
        error_msg = msg + err.msg
        status = False
        if con is not None:
            con.rollback()
    finally:
        # 5) Now close open cur & con
        if cur is not None :
            cur.close()
        if con is not None:
            con.close()
    return status, error_msg
def Execute_IUD(iud_sql):
    '''
Function    : Execute_IUD
Author      : Ruthrapathy
Objective   : To execute a insert/update/delete statment after connecting to MySQL in a Transaction
Inputs      : Properly formed insert/update/delete SQL string statement in a list
              iud_sql is a list containing 1 or more Insert/Update/Delete statements
Returns     : a 2 values containing 
              a) first element as status. True means success, False means fail
              b) second element as error message. Will have value only if status False is returned
Examples    : Here are some example on how to call the function
              import MySQL_Interface
              status, error_msg = MySQL_Interface.Execute_Select("insert into city (id, name, countrycode, district, population) values ({}, '{}', '{}', '{}', {})".format(5001, 'Afghanistan', 'AFG', 'test2', 7002))
                  
                  '''
    con = None
    cur = None
    status = True
    error_msg = ""
    
    try:
        # 1) create a connector object by giving server/host, user-id, pwd and database
        msg = "Error trying to connect to database: "
        con = sql.connect (host=HOST, user=USER, passwd=PASSWORD, 
                       database=DATABASE, port=PORT)
        # 2) create a cursor
        msg = "Error creating cursor: "
        cur = con.cursor()
        # start transaction
        con.start_transaction()
        # 3) Execute
        for sqls in iud_sql:
            msg = "Error executing select statement: " + sqls
            cur.execute(sqls)
        # 4) if it comes here, ==> status ==> commit data
        msg = "Error while committing data: "
        con.commit()
        status = True
    except sql.Error as err:
        error_msg = msg + err.msg
        status = False
        if con is not None:
            con.rollback()
    finally:
        # 5) Now close open cur & con
        if cur is not None :
            cur.close()
        if con is not None:
            con.close()
    return status, error_msg

def Convert_Tuple_To_List(data):
    lst = []
    for item in data:
        l = []
        for c in item:
            l.append(c)
        lst.append(l)
    return lst
