import sqlite3
from sqlite3 import Error

class Database:
    def __init__(self):
        self.sql_create_commands_table = """CREATE TABLE IF NOT EXISTS commands(
                                         id integer PRIMARY KEY,
                                         name text NOT NULL,
                                         action text NOT NULL
                                         );"""
        self.sql_quotes = """CREATE TABLE IF NOT EXISTS quotes(
                          id integer PRIMARY KEY,
                          quote text NOT NULL,
                          made_by text NOT NULL
                          );"""
        self.sql_create_tables = [self.sql_quotes, self.sql_create_commands_table]

    def create_connection(self, db_file):
        """
        creates the database.db file.
        :param db_file: file path to the database.
        :return: conn: this is the database connection that is created when the function runs.
        """
        # print("creating db connection")
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            # print("connected to db")
            # print(conn)
            # return conn
        except Error as e:
            print(e)

        return conn

    def create_table(self, conn, create_table_sql):
        """
        Creates database tables if they do not exist.
        :param conn: sql connection
        :param create_table_sql: tables to create with sqlite.
        :return: None
        """
        try:
            c = conn.cursor()
            c.execute(create_table_sql)
            conn.close()
        except Error as e:
            print(e)

    def add_quote(self, conn, command_info):
        sql = ''' INSERT INTO quotes(quote, made_by)
                      VALUES(?, ?) '''
        cur = conn.cursor()
        cur.execute(sql, command_info)
        conn.commit()
        conn.close()

    def get_quote(self, conn):
        sql = "SELECT * from quotes"
        cur = conn.cursor()
        cur.execute(sql)
        quotes = cur.fetchall()
        conn.close()
        return quotes