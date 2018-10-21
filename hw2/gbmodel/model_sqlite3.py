"""
A recipes flask webapp that derive from guestbook.
ata is stored in a SQLite database that looks something like the following:

+-------+----------+---------------------------+---------+--------------+-----------------------------------------------------------+
| Title | Author   | Ingredient                | Time    | Skill Level  | Description                                               |
+=======+==========+===========================+=========+==============+===========================================================+
| Steak | John Doe | Round Steak, Salt, Pepper | 10 mins | Intermediate | Cook for 1 minute each side in a large cast iron skullet. |
+-------+----------+---------------------------+---------+--------------+-----------------------------------------------------------+

This can be created with the following SQL (see bottom of this file):

    create table recipes (name text, email text, signed_on date, message);

"""
from datetime import date
from .Model import Model
import sqlite3
DB_FILE = 'entries.db'    # file for our Database

class model(Model):
    def __init__(self):
        # Make sure our database exists
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        try:
            cursor.execute("select count(rowid) from guestbook")
        except sqlite3.OperationalError:
            cursor.execute("create table guestbook (name text, email text, signed_on date, message)")
        cursor.close()

    def select(self):
        """
        Gets all rows from the database
        Each row contains: name, email, date, message
        :return: List of lists containing all rows of database
        """
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM guestbook")
        return cursor.fetchall()

    def insert(self, name, email, message):
        """
        Inserts entry into database
        :param name: String
        :param email: String
        :param message: String
        :return: True
        :raises: Database errors on connection and insertion
        """
        params = {'name':name, 'email':email, 'date':date.today(), 'message':message}
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("insert into guestbook (name, email, signed_on, message) VALUES (:name, :email, :date, :message)", params)

        connection.commit()
        cursor.close()
        return True
