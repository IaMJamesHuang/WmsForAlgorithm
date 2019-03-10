from src.db.db_main import DBMain


class SaleRecommend:

    def __init__(self):
        self.db = DBMain()

    # 获取推荐价格
    # 销量/总销量 作为权重r 推荐结果=sum(r * price)
    def get_recommend_price(self, item):
        list = self.db.query_jd_item(item)
        if len(list) == 0:
            return 0
        total = 0
        for recode in list:
            total += recode[2]
        return total/len(list)

    def insert_recommend_info(self, info):
        self.db.insert_item_recommend_info(info)


if __name__ == "__main__":
    item = {"name": "宠物成猫猫粮", "spec": "10kg", "brand": "京东超市伟嘉", "item_id": "5"}
    sale_recommend = SaleRecommend()
    price = sale_recommend.get_recommend_price(item)
    data = [item['item_id'], price]
    sale_recommend.insert_recommend_info(data)
