from proxypool.schemas.proxy import Proxy
from proxypool.crawlers.base import BaseCrawler
import json

BASE_URL = 'https://cool-proxy.net/proxies.json'


class CoolproxyCrawler(BaseCrawler):
    """
    https://cool-proxy.net/
    """
    urls = [BASE_URL]

    def parse(self, html):
        r = json.loads(html)
        for item in r:
            host = item['ip']
            port = item['port']
            yield Proxy(host=host, port=port)


if __name__ == '__main__':
    crawler = CoolproxyCrawler()
    for proxy in crawler.crawl():
        print(proxy)
