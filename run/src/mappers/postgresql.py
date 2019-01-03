#!/usr/bin/env python3

import psycopg2
from psycopg2.extras import RealDictCursor

class Database:
    def __init__(self):
        self.connection = psycopg2.connect('dbname=db')
        self.connection.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
        self.cursor = self.connection.cursor(cursor_factory=RealDictCursor)
    def __enter__(self):
        return self
    def __exit__(self,exception_type,exception_value,exception_traceback):
        if self.connection:
            self.connection.commit()
            if self.cursor:
                self.cursor.close()
            self.connection.close()
