import sqlite3

mDB = ''
mTable = ''

class DW:
    def __init__(self, mDB, mTable) -> None:
        self.mDB = mDB
        self.mTable = mTable
        self.conn = self._connect(self.mDB)
        self.curr = self._cursor(self.conn)

    def _connect(self, mDB):
        conn = sqlite3.connect('./DataBase/test.db')
        return conn
    
    def _cursor(self, conn):
        curr = conn.cursor()
        return curr