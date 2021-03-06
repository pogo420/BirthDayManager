"""
Author: Arnab Mukherjee
Future Plans:
1. Dynamic datatype capability
2. Multi column query capability for insert and delete.
"""

import sqlite3
from typing import Optional, List, Tuple, Union

from Application.StaticCodes import StatusCodes
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
        """Method for creating connection object"""
        try:
            if is_null(self.db_path):
                raise Exception("Null data")
            self.connection = sqlite3.connect(self.db_path)
        except Exception as e:
            print_error(e)
        return self

    def create_cursor(self) -> Optional['SqLiteHelper']:
        """Method for creating cursor object"""
        try:
            self.cursor = self.connection.cursor()
        except Exception as e:
            print_error(e)
        return self

    def test_connection(self) -> Optional[List[Tuple]]:
        """Method for connection testing"""
        try:
            return self.cursor.execute("SELECT DATE('now')").fetchall()
        except Exception as e:
            print_error(e)

    def read_data(self, query) -> Union[List[Tuple], StatusCodes]:
        """Method to read data based on the query
            read_data("SELECT * FROM birthday_data")
        """
        try:
            return self.cursor.execute(query).fetchall()
        except Exception as e:
            print_error(e)
            return StatusCodes.DATA_READ_FAILURE

    def insert_data(self, column_str: str, values_str: str, table: str) -> Optional[StatusCodes]:
        """Method to insert row
            insert_data("name, birthdate", "'gupeh', '02-10'", "birthday_data") -->
            insert into birthday_data(name, birthdate) values('gupeh', '02-10');
        """
        try:
            insert_query = f"INSERT INTO {table}({column_str}) VALUES({values_str})"
            print(insert_query)
            self.cursor.execute(insert_query)
            self.connection.commit()
            return StatusCodes.DATA_INSERT_SUCCESS
        except Exception as e:
            print_error(e)
            return StatusCodes.DATA_INSERT_FAILURE

    def delete_data(self, column_str: str, values_str: str, table: str, isEqual = 1) -> Optional[StatusCodes]:
        """Method to delete row/rows based on single column
            delete_data("emp_id", "45", "emp_table", 1) -->
            select * from emp_table where emp_id = "45
        """
        try:
            if isEqual == 1:
                delete_query = f"DELETE FROM {table} WHERE {column_str}={values_str}"
            else:
                delete_query = f"DELETE FROM {table} WHERE {column_str}!={values_str}"
            print(delete_query)
            self.cursor.execute(delete_query)
            self.connection.commit()
            return StatusCodes.DATA_DELETE_SUCCESS
        except Exception as e:
            print_error(e)
            return StatusCodes.DATA_DELETE_FAILURE
