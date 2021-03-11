from core.modules.request_methods import  *
from core.modules.get_Opsheaders import *
def get_res():
    url = r"https://ops-beta.yjyz.com/api/mall.web.api/organAccount/resource/list"
    data = {"condition":{},"pageNo":1,"rowCntPerPage":10,"pageSize":10}
    re_data = json.dumps(data)
    headers = get_header()
    res_data = post_method(url, data=re_data, header=headers)
    print(res_data)
    return res_data

get_res()