from core.modules.request_methods import  *
from core.modules.get_Opsheaders import *
def get_res():
    url = r"https://ops-beta.yjyz.com/api/mall.web.api/organAccount/order/list"
    data = {"createEndTm": 1613750399000, "createStartTm": 1611072000000, "pageNo": 1, "rowCntPerPage": 10,
            "pageSize": 10}
    headers = get_header()
    res_data = post_method(url, data=data, header=headers)
    return res_data

a = get_res()
print(a)