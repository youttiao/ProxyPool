from pyquery import PyQuery as pq
from proxypool.schemas.proxy import Proxy
from proxypool.crawlers.base import BaseCrawler

BASE_URL = 'https://www.ipaddress.com/proxy-list/'


class IpaddressCrawler(BaseCrawler):
    """
    https://www.ipaddress.com/proxy-list/
    """
    urls = [BASE_URL]

    def parse(self, html):
        """
        parse html file to get proxies
        :return:
        """
        doc = pq(html)
        trs = doc('tbody tr').items()
        for tr in trs:
            ip_and_port = tr.find('td:nth-child(1)').text().split(':')
            host = ip_and_port[0]
            port = int(str(ip_and_port[1]))
            yield Proxy(host=host, port=port)


if __name__ == '__main__':
    crawler = IpaddressCrawler()
    for proxy in crawler.crawl():
        print(proxy)
