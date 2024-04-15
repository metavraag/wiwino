import sqlite3

class DatabaseManager:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def execute(self, query):
        self.cursor.execute(query)
        self.conn.commit()

    def fetch(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def __del__(self):
        self.conn.close()
    
    def create_table_links(self, table_name):
        query = f"""CREATE TABLE IF NOT EXISTS {table_name} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            link TEXT NOT NULL UNIQUE
            )"""
        self.execute(query)
        self.conn.commit()
    