from proxypool.crawlers.base import BaseCrawler
from proxypool.schemas.proxy import Proxy
import re
from pyquery import PyQuery as pq


BASE_URL = 'http://www.xicidaili.com/wt/{page}'

class XicidailiCrawler(BaseCrawler):
    """
    xicidaili crawler, https://www.xicidaili.com/
    """
    urls = [BASE_URL.format(page=page) for page in range(1, 10)]

    def parse(self, html):
        """
        parse html file to get proxies
        :return:
        """
        doc = pq(html)
        for item in doc('tr[class="odd"]').items():
            td_ip = item.find('td:nth-child(2)').text()
            td_port = item.find('td:nth-child(3)').text()
            if td_ip and td_port:
                yield Proxy(host=td_ip, port=td_port)


if __name__ == '__main__':
    crawler = XicidailiCrawler()
    for proxy in crawler.crawl():
        print(proxy)
