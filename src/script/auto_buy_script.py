import urllib.request
import urllib.parse

from src.script import script_main


class AutoBuy:

    def auto_buy_item(self, company_id, user_id, barcode, amount, loc):
        url = script_main.base_url + r"buyItem"
        data = {
            "barcode": barcode,
            "amount": amount,
            "loc": loc
        }
        post_data = urllib.parse.urlencode(data).encode('utf-8')
        headers = {
            "company_id": company_id,
            "user_id": user_id
        }
        request = urllib.request.Request(url=url, headers=headers, data=post_data, method='POST')
        response = urllib.request.urlopen(request)
        print(response.read())
