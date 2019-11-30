import scrapy
from ..items import Product
# scrapy crawl pandashop


class PandashopSpider(scrapy.Spider):
    name = "pandashop"
    allowed_domains = ["pandashop.md"]

    def start_requests(self):
        urls = [
            "https://www.pandashop.md/ro/catalog/electronics/orgtech/usb_drives/external_hdd/default.aspx?all=1",
            "https://www.pandashop.md/ro/catalog/electronics/orgtech/usb_drives/external_ssd/default.aspx?all=1",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        for element in response.css("div.catalog_item"):
            product = Product()
            product["name"] = element.css(
                "div.details > div.catalog_name > a *::text").get()
            pricestr = element.css(
                "div.brief > .price_light > strong *::text").get()
            product["price"] = int(pricestr.replace(" ", ""))

            productDetails = element.css("div.details > p *::text").get()
            productDetails.replace("<br>", "")

            productDetailsList = productDetails.strip().split(" • ")
            for data in productDetailsList:

                dataSplit = data.strip().split(maxsplit=1)
                if len(dataSplit) == 2:
                    dataSplit[1] = dataSplit[1].replace(
                        "\n", "").replace("\xa0", " ")
                else:
                    dataSplit.append("")
                if dataSplit[0].strip() == "Capacitate:":
                    product["capacity"] = dataSplit[1]
                elif dataSplit[0].strip() == "Interfaţă:":
                    product["interface"] = dataSplit[1]
                elif dataSplit[0].strip() == "Culoare:":
                    product["color"] = dataSplit[1]
                elif dataSplit[0].strip() == "Dimensiuni:":
                    product["size"] = dataSplit[1]
                elif dataSplit[0].strip() == "Greutate:":
                    product["weight"] = dataSplit[1]
            yield product
