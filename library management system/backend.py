import sqlite3
def connect():
    conn_obj=sqlite3.connect("books.db")
    cur_obj=conn_obj.cursor()
    cur_obj.execute("CREATE TABLE IF NOT EXISTS "
                    "books(id integer PRIMARY KEY,"
                    "title text"
                    "author text"
                    "year integer"
                    "isbn integer)")
    conn_obj.commit()
    conn_obj.close()
def insert(title,author,year,isbn):
    conn_obj=sqlite3.connect("books.db")
    cur_obj=conn_obj.cursor()
    cur_obj.execute("INSERT into books"
                    "SET title=?,"
                    "year=?,"
                    "isbn=?"
                    "where id=?",(title,author,year,isbn))
    conn_obj.commit()
    conn_obj.close()
def view():
    conn_obj=sqlite3.connect("books.db")
    cur_obj=conn_obj.cursor()
    cur_obj.execute("SELECT * FROM books")
    rows=cur_obj.fetchall()
    conn_obj.close()
    return rows
def update(id,title,author,year,isbn):
    conn_obj=sqlite3.connect("books.db")
    cur_obj=conn_obj.cursor()
    cur_obj.execute("UPDATE books"
                    "SET title=?,"
                    "year=?,"
                    "isbn=?"
                    "where id=?",(title,author,year,isbn))
    conn_obj.commit()
    conn_obj.close()
def delete(d):
    conn_obj=sqlite3.connect("books.db")
    cur_obj=conn_obj.cursor()
    cur_obj.execute("DELETE FROM books WHERE id=?",(d,))
    conn_obj.commit()
    conn_obj.close()
def search(title=" ",author=" ",year=" ",isbn=" "):
    conn_obj=sqlite3.connect("books.db")
    cur_obj=conn_obj.cursor()
    cur_obj.execute("SELECT *"
                    "FROM books"
                    "where title=? OR author=?"
                    "OR year=? OR isbn=?",(title,author,year,isbn))
    rows=cur_obj.fetchall()
    conn_obj.close()
    return rows
connect()
                    
    
    
    
    
    

                    
   
    
    
