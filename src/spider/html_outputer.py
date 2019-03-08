
class HtmlOutputer:

    def __init__(self):
        self.data_list = []

    def collect_data(self, data):
        if data is None:
            return
        for item in data:
            self.data_list.append(item)

    def output(self):
        file = open(r'output.txt', 'w')
        for data in self.data_list:
            file.write(str(data))
            file.write('\n')
        file.close()
