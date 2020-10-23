"""
Author: Arnab Mukherjee
Capabilities:
    1. Assuming data as json objects.
    2. Parsing data for insert/Update/Delete operation.
    3. Using sqlhelper for the activities.
    4. Returning Success/Failure message as json object.
"""

from typing import Tuple, Optional, Union
from Application.SqLiteHelper import SqLiteHelper
from Application.StaticCodes import StatusCodes, ResponseStatus, ProcessingType


def generate_response(status: ResponseStatus, payload: Union[str, dict]):
    return {
        "status": status.value,
        "payload": {
            "message": payload
        }
    }


class DbManager:
    """Class to manage DB calls"""

    def __init__(self, db_helper: SqLiteHelper, db_options: dict):
        self.db_helper = db_helper
        self.db_options = db_options
        self.db_path = self.db_options.get("db_path")
        self.master_table = self.db_options.get("master_table")

    def test_connection(self) -> Optional[str]:
        """Method for database test connection"""
        test_string = self.db_helper(self.db_path)\
            .create_connection()\
            .create_cursor()\
            .test_connection()
        return test_string

    def insert_data(self, inp_message: dict) -> StatusCodes:
        """Method for insert into database"""
        columns = []
        values = []
        for i in inp_message.keys():
            columns.append(i)
            values.append("'"+inp_message.get(i)+"'")

        columns_str = ",".join(columns)
        values_str = ",".join(values)
        insert_response = self.db_helper(self.db_path) \
            .create_connection() \
            .create_cursor() \
            .insert_data(columns_str, values_str, self.master_table)
        return insert_response

    def delete_data(self, inp_message: dict) -> StatusCodes:
        """Method for delete data from database, assumption is search by single column"""
        columns = []
        values = []
        for i in inp_message.keys():
            columns.append(i)
            values.append("'" + inp_message.get(i) + "'")

        columns_str = ",".join(columns)
        values_str = ",".join(values)

        delete_response = self.db_helper(self.db_path)\
            .create_connection()\
            .create_cursor()\
            .delete_data(columns_str, values_str, self.master_table)
        return delete_response

    def processor(self, inp_message):
        """Method for orchest.rating db traffic"""
        if inp_message.get("type") == ProcessingType.INSERT.value:
            response = self.insert_data(inp_message.get("payload"))
            if response == StatusCodes.DATA_INSERT_SUCCESS:
                return generate_response(ResponseStatus.SUCCESS, response.value)
            elif response == StatusCodes.DATA_INSERT_FAILURE:
                return generate_response(ResponseStatus.ERROR, response.value)

        elif inp_message.get("type") == ProcessingType.DELETE.value:
            response = self.delete_data(inp_message.get("payload"))
            if response == StatusCodes.DATA_DELETE_SUCCESS:
                return generate_response(ResponseStatus.SUCCESS, response.value)
            elif response == StatusCodes.DATA_DELETE_FAILURE:
                return generate_response(ResponseStatus.ERROR, response.value)


