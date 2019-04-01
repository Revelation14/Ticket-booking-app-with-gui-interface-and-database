import sqlite3
class Database:
    def __init__(self,db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS ticket (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, email TEXT, number INTEGER, seat TEXT )")
        self.conn.commit()
    def book(self,name,age,email,number,seat):
        self.cur.execute("INSERT INTO ticket VALUES (NULL,?,?,?,?,?)",(name,age,email,number,seat))
        self.conn.commit()
    def view(self):
        self.cur.execute("SELECT * FROM ticket")
        rows=self.cur.fetchall()
        return rows
    def cancel(self,id):
        self.cur.execute("DELETE FROM ticket WHERE id =?",(id,))
        self.conn.commit()
    def __del__(self):
        self.conn.close()
