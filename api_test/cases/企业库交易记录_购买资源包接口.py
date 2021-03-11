import unittest
from core.modules.request_methods import *
from core.modules.get_Opsheaders import *
headers = get_header()
class BlogTest(unittest.TestCase):

    def setUp(self):
        self.url = r"https://api-beta.yjyz.com/mall.core.srv/organOrder/saveOrganPayOrders"

    def tearDown(self):
        pass

    # def test_username_null(self):
    #     """默认参数"""
    #     data = {
    #         "customerInfo": {
    #             "brandId": 670009459898460224,
    #             "brandName": "测试专用品牌",
    #             "organId": 670010683867799680,
    #             "organName": "广州分公司666",
    #             "sysUserId": 644428902057082880,
    #             "sysUserName": "陈一一",
    #             "sysUserPhone": "18797908791"
    #         },
    #         "productCount": 2,
    #         "productId": 811878065972973568,
    #         "productPrice": 100,
    #         "totalPrice": 120
    #     }
    #     exe_data_json = json.dumps(data)
    #     self.result = post_method(self.url,data =exe_data_json,header = headers)
    #     print(self.result,type(self.result ))
    #     print(self.result['msg'])
    #     # self.assertEqual(self.result['status'], 0)
    #     self.assertEqual(self.result['msg'], 'success')
    #
    #
    def test_brandid_null(self):
        """brandid为空"""
        data =     {
        "customerInfo": {
            "brandId": 0,
            "brandName": "",
            "createTm": 0,
            "id": 0,
            "organId": 0,
            "organName": "",
            "organType": 1,
            "sysUserId": 0,
            "sysUserName": "666911217337204736",
            "sysUserPhone": "18797908701"
        },
        "productCount": 44,
        "productId": 811878065972973568,
        "productPrice": 11,
        "totalPrice": 22
    }
        exe_data_json = json.dumps(data)
        self.result = post_method(self.url,data =exe_data_json,header = headers)
        print(self.result)
        # self.assertEqual(self.result['status'], 0)
        self.assertEqual(self.result['msg'], 'success')

if __name__ == '__main__':
    unittest.main()