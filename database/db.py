import sqlite3


class Database:
    def __init__(self, db_name:str = 'main.db'):
        self.database = db_name


    def execute(self, sql, *args, commit: bool = False, fetchone: bool = False, fetchall: bool = False):
        with sqlite3.connect(self.database) as db:
            cursor = db.cursor()
            cursor.execute(sql, args)

            result = None
            if commit:
                db.commit()
            elif fetchone:
                result = cursor.fetchone()
            elif fetchall:
                result = cursor.fetchall()

        return result

    # === USERS
    def create_table_users(self):
        sql = '''CREATE TABLE IF NOT EXISTS users(
            telegram_id INTEGER NOT NULL UNIQUE,
            full_name TEXT,
            phone_number VARCHAR(13)
        )'''
        self.execute(sql, commit=True)

    def insert_telegram_id(self, telegram_id):
        sql = '''INSERT INTO users(telegram_id) VALUES(?)'''
        self.execute(sql, telegram_id, commit=True)

    def update_user_info(self, full_name, phone_number, telegram_id):
        sql = '''UPDATE users SET full_name = ?, phone_number = ? WHERE telegram_id = ?'''
        self.execute(sql, full_name, phone_number, telegram_id, commit=True)

    def get_user(self, telegram_id):
        sql = '''SELECT * FROM users WHERE telegram_id = ?'''
        return self.execute(sql, telegram_id, fetchone=True)



    # === BOOKS

    def create_table_books(self):
        sql = '''
        CREATE TABLE IF NOT EXISTS books(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT,
            price REAL,
            description TEXT,
            category TEXT
            )'''

        self.execute(sql, commit=True)

    def insert_books(self, title, author, price, description, category):
        sql = '''INSERT INTO books(title, author, price, description, category)VALUES (?, ?, ?, ?)'''
        self.execute(sql, title, author, price, description, category, commit=True)


    def get_all_books(self):
        sql = '''SELECT * FROM books'''
        return self.execute(sql, fetchall=True)

    def get_book_by_id(self, book_id):
        sql = 'SELECT * FROM books WHERE book_id = ?'
        self.execute(sql, book_id, fetchone=True)

    def get_books_by_category(self, category):
        sql = "SELECT * FROM books WHERE category = ?"
        return self.execute(sql, category, fetchall=True)
