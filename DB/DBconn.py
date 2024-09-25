import sqlite3
import psycopg2 as pg2
import config


mDB = ''
mTable = ''

class DW:
    def __init__(self,mDB_URL, mDB, mTable, mUser, mPW, mPort, engine='sqlite') -> None:
        self.DB_URL = mDB_URL
        self.DB = mDB
        self.Table = mTable
        self.User = mUser
        self.PW = mPW
        self.Port = mPort
        self.engine = engine

        self.conn = self._connect(self.DB)
        self.curr = self._cursor(self.conn)

    def _connect(self, mDB):
        if self.engine == 'sqlite':
            conn = sqlite3.connect('./DataBase/test.db')
            return conn
        elif self.engine == 'postgres':
            #postgres : config < dotenv
            pg_conn = pg2.connect(f"host={self.DB_URL} dbname={self.DB} user={self.User} password={self.PW} port={self.Port}")
            return pg_conn 
    
    def _cursor(self, conn):
        curr = conn.cursor()
        return curr


class Databases():
    def __init__(self):
        self.db = pg2.connect(host='localhost', dbname='test',user='postgres',password='password',port=5432)
        self.cursor = self.db.cursor()

    def __del__(self):
        self.db.close()
        self.cursor.close()

    def execute(self,query,args={}):
        self.cursor.execute(query,args)
        row = self.cursor.fetchall()
        return row

    def commit(self):
        self.cursor.commit()