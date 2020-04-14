from pyquery import PyQuery as pq
from proxypool.schemas.proxy import Proxy
from proxypool.crawlers.base import BaseCrawler

BASE_URL = 'http://www.data5u.com/'


class Data5Crawler(BaseCrawler):
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
        trs = doc('ul[class="l2"]').items()
        for tr in trs:
            if tr.find('span:nth-child(4)').text() == 'http':
                # print(tr.text())
                host = tr.find('span:nth-child(1)').text()
                port = int(tr.find('span:nth-child(2)').text())
                yield Proxy(host=host, port=port)


if __name__ == '__main__':
    crawler = Data5Crawler()
    for proxy in crawler.crawl():
        print(proxy)
