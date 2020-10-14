from typing import Tuple

from Application.SqLiteHelper import SqLiteHelper
import os


class DbManager:
    """Class to manage DB calls"""

    def __init__(self, db_helper: SqLiteHelper, db_options: dict):
        self.db_helper = db_helper
        self.db_options = db_options

    def read_data(self, query):
        pass

    def insert_data(self, columns: Tuple[str, str], values: Tuple[str, str], table: str):
        pass

    def delete_data(self, columns, values, table):
        pass

    def update_data(self, column, old_value, new_value, table):
        pass


if __name__ == "__main__":
    db_path = os.environ["SQLITE_DB"]
    db = DbManager(SqLiteHelper, {"db_path": db_path})
    print(db.read_data("SELECT DATE('now')"))
    print(db.insert_data(("name", "birthdate"), ("gupeh", "02-10"), "birthday_data"))
