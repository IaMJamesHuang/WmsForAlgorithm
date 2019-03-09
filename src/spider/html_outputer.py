from src.db import db_main


class HtmlOutputer:

    def __init__(self):
        self.data_list = []
        self.db_outputer = db_main.DBMain()

    def collect_data(self, data):
        if data is None:
            return
        for item in data:
            self.data_list.append(item)

    def output(self):
        self.db_outputer.main(self.data_list)
