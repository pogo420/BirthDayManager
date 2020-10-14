import sqlite3
import os
from typing import Optional, List, Tuple

from Application.StatusCodes import StatusCodes
from Application.Utilities import is_null, print_error


class SqLiteHelper:
    """Class for sqlite operations"""

    def __init__(self, db_path: str):
        self.db_path = db_path
        self.connection = None
        self.cursor = None
        self.result = None
        self.query = ""

    def create_connection(self) -> Optional['SqLiteHelper']:
        try:
            if is_null(self.db_path):
                raise Exception("Null data")
            self.connection = sqlite3.connect(self.db_path)
        except Exception as e:
            print_error(e)
        return self

    def create_cursor(self) -> Optional['SqLiteHelper']:
        try:
            self.cursor = self.connection.cursor()
        except Exception as e:
            print_error(e)
        return self

    def test_connection(self) -> Optional[List[Tuple]]:
        try:
            return self.cursor.execute("SELECT DATE('now')").fetchall()
        except Exception as e:
            print_error(e)

    def read_data(self, query) -> Optional[List[Tuple]]:
        try:
            return self.cursor.execute(query).fetchall()
        except Exception as e:
            print_error(e)

    def insert_data(self, column_str: str, values_str: str, table: str):
        try:
            insert_query = f"INSERT INTO {table}({column_str}) VALUES({values_str})"
            print(insert_query)
            self.cursor.execute(insert_query)
            self.connection.commit()
            return StatusCodes.DATA_INSERT_SUCCESS
        except Exception as e:
            print_error(e)


if __name__ == "__main__":
    db_path = os.environ["SQLITE_DB"]
    print(SqLiteHelper(db_path).create_connection().create_cursor().test_connection())
    print(SqLiteHelper(db_path).create_connection().create_cursor().read_data("SELECT DATE('now')"))
    print(SqLiteHelper(db_path).create_connection().create_cursor().insert_data("name, birthdate", "'gupeh', '02-10'", "birthday_data"))
    print(SqLiteHelper(db_path).create_connection().create_cursor().read_data("SELECT * FROM birthday_data"))
