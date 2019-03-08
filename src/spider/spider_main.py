import urllib.request
from src.spider import url_manager, html_downloader, html_parser, html_outputer

# 单个商品爬取的页面数量
page_num = 3


class SpiderMain:

    def __init__(self):
        self.url_manager = url_manager.UrlManager()
        self.html_downloader = html_downloader.HtmlDownloader()
        self.html_parser = html_parser.HtmlParser()
        self.html_outputer = html_outputer.HtmlOutputer()

    def add_urls(self, item):
        item = urllib.request.quote(item)
        for n in range(1, page_num):
            url = 'http://search.jd.com/Search?keyword=%s&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&page=%d&s=%d&click=0' % (item, 2 * n - 1, 1 + 60 * (n - 1))
            self.url_manager.add_new_url(url)

    def main(self, item):
        self.add_urls(item)
        while self.url_manager.has_new_url():
            url = self.url_manager.get_new_url()
            response = self.html_downloader.download(url)
            if response is not None:
                data_list = self.html_parser.parse(response)
                self.html_outputer.collect_data(data_list)

        self.html_outputer.output()


if __name__ == "__main__":
    SpiderMain().main("猫粮")
