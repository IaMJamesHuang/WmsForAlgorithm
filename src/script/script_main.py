from src.script import auto_buy_script
# 项目地址
base_url = r'http://localhost:8080/wms/'
# 自动购买测试商品
auto_buy_items = [
    {"company_id": "1", "user_id": "1", "barcode": "6903653028657", "amount": "2", "loc": "LC001"}
]


class ScriptMain:

    def run_auto_buy(self):
        auto_buy = auto_buy_script.AutoBuy()
        for item in auto_buy_items:
            auto_buy.auto_buy_item(item['company_id'], item['user_id'], item['barcode'], item['amount'], item['loc'])

    def main(self):
        self.run_auto_buy()


if __name__ == "__main__":
    ScriptMain().main()
