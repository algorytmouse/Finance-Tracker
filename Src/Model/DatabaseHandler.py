import sqlite3


class DatabaseHandler:

    def __init__(self):
        self.__conn = None
        self.__cursor = None

    def connect_to_db(self):
        """
        Establishes connection to the Database

        :return: None
        :rtype: None
        """
        self.__conn = sqlite3.connect("Database.db")
        self.__cursor = self.__conn.cursor()

    def close_db_connection(self):
        """
        Closes the Database connection

        :return: None
        :rtype: None
        """
        try:
            self.__conn.close()
        except AttributeError:
            print("You must connect to the Database first, before attempting to close it.")

    def insert_data(self):
        pass

    def get_data(self):
        pass

    def update_data(self):
        pass

    def delete_data(self):
        pass


"""
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       name TEXT NOT NULL,
                       age INTEGER
                       )''')
        conn.commit()

        users = [("Bob", 30), ("Charlie", 22), ("David", 28)]
        cursor.executemany("INSERT INTO users (name, age) VALUES (?, ?)", users)
        conn.commit()

        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()  # Fetch all records
        for row in rows:
            print(row)

        print("_______________________")

        cursor.execute("SELECT * FROM users WHERE name=?", ("Charlie",))
        print(cursor.fetchone())  # Fetch one result

        cursor.execute("UPDATE users SET age = ? WHERE name = ?", (26, "Alice"))
        conn.commit()

        conn.close()
        #conn.close() -> close database connection"""

DatabaseHandler().close_db_connection()
