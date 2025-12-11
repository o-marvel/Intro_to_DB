import mysql.connector


try:
# Replace with your connection details
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Ossy#12?",
        database = 'alx_book_store'
    )
    mycursor = mydb.cursor()
     # Create the database (safe even if it already exists)
    mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print(" Database 'alx_book_store' created successfully! ")

except mysql.connector.Error as e:
    print(f"Error: {e}")

finally:
    if mydb.is_connected():
        mycursor.close()
        mydb.close()
