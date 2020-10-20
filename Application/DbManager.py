"""
Author: Arnab Mukherjee
Capabilities:
    1. Assuming data as json objects.
    2. Parsing data for insert/Update/Delete operation.
    3. Using sqlhelper for the activities.
    4. Returning Success/Failure message as json object.
"""

from typing import Tuple, Optional
from Application.SqLiteHelper import SqLiteHelper
from Application.StatusCodes import StatusCodes


class DbManager:
    """Class to manage DB calls"""

    def __init__(self, db_helper: SqLiteHelper, db_options: dict):
        self.db_helper = db_helper
        self.db_options = db_options
        self.db_path = self.db_options.get("db_path")

    def test_connection(self):
        test_string = self.db_helper(self.db_path)\
            .create_connection()\
            .create_cursor()\
            .test_connection()
        return test_string
