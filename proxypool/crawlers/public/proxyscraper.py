from proxypool.schemas.proxy import Proxy
from proxypool.crawlers.base import BaseCrawler
import json

BASE_URL = 'https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.json'

class SunnyCrawler(BaseCrawler):
    """
    https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.json
    """
    urls = [BASE_URL]

    def parse(self, html):
        r = json.loads(html)
        keys = [k for k in r if 'proxy' in k]
        for key in keys:
            for item in r[key]:
                host = item['ip']
                port = int(str(item['port']))
                yield Proxy(host=host, port=port)


if __name__ == '__main__':
    crawler = SunnyCrawler()
    for proxy in crawler.crawl():
        print(proxy)
