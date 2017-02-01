import sqlite3

class DBmain:
    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def select_id(self, id_number):
        with self.connection:
            return self.cursor.execute("SELECT Name FROM user WHERE id = ?",(id_number,)).fetchall()
    def add_user(self, id_number, username):
        with self.connection:
             self.cursor.execute("INSERT INTO user(id,Name) VALUES (?,?)", (id_number, username))
             self.connection.commit()
    def close(self):
        self.connection.close()