import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='saro',
                                         user='root',
                                         password='Lti@1234')

    mySql_Create_Table_Query = """ insert into mani values(2,"rice","2000","2022-07-12")
    
    
    """

    curser = connection.cursor()
    result = curser.execute(mySql_Create_Table_Query)
    print("Laptop Table created successfully ")
    connection.commit()
except mysql.connector.Error as error:
    print("Failed to create table in MySQL: {}".format(error))
finally:

    curser.close()
    connection.close()
    print("MySQL connection is closed")


