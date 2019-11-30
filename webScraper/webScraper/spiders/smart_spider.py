# import scrapy
# from ..items import Product
# # scrapy crawl pandashop


# class SmartSpider(scrapy.Spider):
#     name = "smart"
#     allowed_domains = ["smart.md"]

#     def start_requests(self):
#         urls = [
#             "https://www.smart.md/ro/hdd"
#         ]
#         for url in urls:
#             yield scrapy.Request(url=url, callback=self.parse)

#     def parse(self, response):
#         for element in response.css("div.products_container"):
#             product = Product()
#             print(f"xxxxxx::{product}")
#             product["name"] = element.css(
#                 "div.Block_cont_produsC.row_special > a").get()
#             print(f"xxxxxx::{product}")
#             # pricestr = element.css(
#             #     "div.brief > .price_light > strong *::text").get()
#             # product["price"] = int(pricestr.replace(" ", ""))

#             # productDetails = element.css("div.details > p *::text").get()
#             # productDetails.replace("<br>", "")
#             # productDetailsList = productDetails.strip().split(" • ")
#             # for data in productDetailsList:

#             #     dataSplit = data.strip().split(maxsplit=1)
#             #     if len(dataSplit) == 2:
#             #         dataSplit[1] = dataSplit[1].replace(
#             #             "\n", "").replace("\xa0", " ")
#             #     else:
#             #         dataSplit.append("")
#             #     if dataSplit[0].strip() == "Capacitate:":
#             #         product["capacity"] = dataSplit[1]
#             #     elif dataSplit[0].strip() == "Interfaţă:":
#             #         product["interface"] = dataSplit[1]
#             #     elif dataSplit[0].strip() == "Culoare:":
#             #         product["color"] = dataSplit[1]
#             #     elif dataSplit[0].strip() == "Dimensiuni:":
#             #         product["size"] = dataSplit[1]
#             #     elif dataSplit[0].strip() == "Greutate:":
#             #         product["weight"] = dataSplit[1]
#             yield product
