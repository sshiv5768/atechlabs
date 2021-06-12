import mysql.connector

# Setup the database connection
db_connection = mysql.connector.connect(
host='localhost',
user='root',
passwd='',
database='books'
)

db = db_connection.cursor()

# Create operation
db.execute("CREATE TABLE books(name varchar(200), author varchar(100))")

# INSERT operation
sql_code = "INSERT into books(name, author) values(%s, %s)"
books = [("JK", "Jk Simons"), ("Army of Dead", "Zack snyder"),]
db.executemany(sql_code, books)
db_connection.commit()

# READ operation
db.execute("SELECT name FROM books")
result = db.fetchone()
for i in result:
    print(i)
