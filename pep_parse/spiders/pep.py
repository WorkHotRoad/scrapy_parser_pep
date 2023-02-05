import scrapy
import re
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        all_href = set(
            response.xpath(
                '//section[@id="numerical-index"]//'
                'a[@class="pep reference internal"]/@href'
            ).getall()
        )
        for link in list(all_href):
            yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response):
        data = {}
        xpath = r'//h1[@class="page-title"]/descendant-or-self::*/text()'
        page_title = "".join(response.xpath(xpath).getall())
        pattern = r'PEP (?P<version>\d+).{0,3}(?P<name>.+)'
        text_match = re.search(pattern, page_title)
        data["number"] = text_match.group("version")
        data["name"] = text_match.group("name")
        data["status"] = response.xpath(
            '//dt[text()="Status"]/following-sibling::dd[1]/abbr/text()'
        ).get()
        yield PepParseItem(data)
