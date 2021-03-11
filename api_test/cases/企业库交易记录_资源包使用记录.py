from core.modules.request_methods import  *
from core.modules.get_Opsheaders import *
def get_res():
    url = r"https://ops-beta.yjyz.com/api/mall.web.api/organAccount/order/list"
    data = {"createEndTm": 1613750399000, "createStartTm": 1611072000000, "pageNo": 1, "rowCntPerPage": 10,
            "pageSize": 10}
    exe_data_json = json.dumps(data)
    headers = get_header()
    res_data = post_method(url, data=exe_data_json, header=headers)
    print(res_data)
    return res_data

get_res()