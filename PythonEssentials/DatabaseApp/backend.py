import sqlite3
class Database:
    
    def __init__(self):
        self.con = sqlite3.connect("book.db")
        self.cursor = self.con.cursor()
        query = self.cursor.execute("CREATE TABLE IF NOT EXISTS book (ID INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn      TEXT)")
        self.con.commit()
    
    def insert(self,title, author, year, isbn):
        query = self.cursor.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",(title,author,year,isbn))
        self.con.commit()
    def view(self):
        query = self.cursor.execute("SELECT * FROM book")
        results = self.cursor.fetchall()
        return results
    def search(self,title="", author="", year="", isbn=""):
        query = self.cursor.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
        result = self.cursor.fetchall()
        return result
    def delete(self,ID):
        query = self.cursor.execute("DELETE FROM book WHERE id=?",(ID,))
        self.con.commit()
    def update(self,ID, title, author, year, isbn):
        query = self.cursor.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",(title,author,year,isbn,ID))
        self.con.commit()
    
    def __del__(self):
        self.con.close()