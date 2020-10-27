import os
from Application.DbManager import DbManager
from Application.SqLiteHelper import SqLiteHelper


class UserQueryTranslator:

    def __init__(self, request_data):
        self.request_data = request_data
        self.db_path = os.environ["SQLITE_DB"]
        self.master_table = os.environ["MASTER_TABLE"]

    def process_data(self):
        return DbManager(SqLiteHelper, {"db_path": self.db_path, "master_table": self.master_table}) \
            .processor(self.request_data)
