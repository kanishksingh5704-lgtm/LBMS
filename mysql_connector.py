# pyrefly: ignore [missing-import]
import mysql.connector as ms;

con = ms.connect(
    host="localhost",
    user="root",
    database="lbms",  # name your database here
    passwd=""  # enter your mysql passwd here
)


if con.is_connected():
    print("database connected")
else:
    print("connection unsuccessful")
