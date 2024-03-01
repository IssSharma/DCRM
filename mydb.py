import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Sidd@9962'
    )

#prepare a cursor object                                                                                                                                      
cursorObject =database.cursor()

# create a databse
cursorObject.execute("CREATE DATABASE siddco")

print("All Done !")