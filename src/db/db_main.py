import pymysql


class DBMain:
    def insert_jd_item_info(self, data):
        db = pymysql.connect("localhost", "root", "8108320", "wms_db")
        cursor = db.cursor()
        for item in data:
            sql = "insert into jd_item(item_name, price) values(\'%s\', %s)" % (item[0], item[1])
            print(sql)
            try:
                cursor.execute(sql)
                db.commit()
            except Exception as e:
                print(str(e))
                db.rollback()
        db.close()

    def insert_item_recommend_info(self, data):
        db = pymysql.connect("localhost", "root", "8108320", "wms_db")
        cursor = db.cursor()
        sql = "insert into item_recommend(item_id, price) values(%s, %s)" % (data[0], data[1])
        try:
            cursor.execute(sql)
            db.commit()
        except Exception as e:
            print(str(e))
            db.rollback()
        finally:
            db.close()

    # item = {"name": "宠物成猫猫粮", "spec": "10kg", "brand": "京东超市伟嘉", "item_id": "5"}
    def query_jd_item(self, item):
        db = pymysql.connect("localhost", "root", "8108320", "wms_db")
        cursor = db.cursor()
        name = '%' + item['name'] + '%'
        brand = '%' + item['brand'] + '%'
        spec = '%' + item['spec'] + '%'
        sql = "select * from jd_item where item_name like '%s%s%s';" % (brand, name, spec)
        cursor.execute(sql)
        return cursor.fetchall()


if __name__ == "__main__":
    pass
