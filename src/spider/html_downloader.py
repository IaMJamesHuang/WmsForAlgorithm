import urllib.request


class HtmlDownloader:

    def download(self, url):
        if url is None:
            return None

        request = urllib.request.Request(url)
        request.add_header("user-agent", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36")
        response = urllib.request.urlopen(request)

        if response.code != 200:
            return None

        return response.read().decode('utf-8')
