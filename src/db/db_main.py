import pymysql


class DBMain:
    def main(self, data):
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


if __name__ == "__main__":
    test_data = [['狗粮 30g', '10']]
    DBMain().main(test_data)
