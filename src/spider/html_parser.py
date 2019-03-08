import re


class HtmlParser:

    def parse(self, data):
        data_list = []
        link_list = re.findall(r'<li data-sku="\d*" class="gl-item">.*?</li>', data, re.DOTALL)
        for link in link_list:
            single_data = []
            # 名称
            name_match = re.search(r'<div class="p-name p-name-type-2">.*?<em>(.*?)</em>.*?</div>', link, re.DOTALL)
            if name_match:
                name = re.sub(r'<.*?>', '', name_match.group(1))
            else:
                name = "empty"
            single_data.append(name)

            # 价格
            price_match = re.search(r'<div class="p-price">.*?<i>(.*?)</i>.*?</div>', link, re.DOTALL)
            if price_match:
                price = price_match.group(1)
            else:
                price = "empty"
            single_data.append(price)

            data_list.append(single_data)

        return data_list
