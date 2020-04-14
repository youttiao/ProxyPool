from pyquery import PyQuery as pq
from proxypool.schemas.proxy import Proxy
from proxypool.crawlers.base import BaseCrawler

BASE_URL = 'http://free-proxy-list.net/'


class FreeproxylistCrawler(BaseCrawler):
    """
    data5u
    """
    urls = [BASE_URL]

    def parse(self, html):
        """
        parse html file to get proxies
        :return:
        """
        doc = pq(html)
        trs = doc('tr').items()
        for tr in trs:
            if tr.find('td[class="hx"]').text() == 'no':
                host = tr.find('td:nth-child(1)').text()
                port = int(tr.find('td:nth-child(2)').text())
                yield Proxy(host=host, port=port)


if __name__ == '__main__':
    crawler = FreeproxylistCrawler()
    for proxy in crawler.crawl():
        print(proxy)
