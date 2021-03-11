import requests
import json


# 请求方式get
def get_method(url, data=None, header=None):
    if header is not None:
        res = requests.get(url, params=data, headers=header)
    else:
        res = requests.get(url=url, params=data)
    return res.json()


# 请求方式post
def post_method(url, data=None, header=None):
    global res
    if header is not None:
        res = requests.post(url, data=data, headers=header)
    else:
        res = requests.post(url=url, data=data)
    # if str(res) == "<Response[200]>":
    return res.json()
    # else:
    #     return res.text


# 请求方式put
def put_method(url, data=None, header=None):
    if header is not None:
        res = requests.put(url, data=data, headers=header)
    else:
        res = requests.put(url=url, data=data)
    return res.json()


# 请求方式delete
def delete_method(url, data=None, header=None):
    if header is not None:
        res = requests.delete(url, data=data, headers=header)
    else:
        res = requests.delete(url=url, data=data)
    return res.json()


# 主方法
# def run_method(self, method, url, data=None, header=None):
#     if method == 'get' or 'GET':
#         res = self.get_method(url, data, header)
#     elif method == 'post' or 'POST':
#         res = self.post_method(url, data, header)
#     elif method == 'put' or 'PUT':
#         res = self.put_method(url, data, header)
#     elif method == 'delete' or 'DELETE':
#         res = self.delete_method(url, data, header)
#     else:
#         res = "你的请求方式不正确"
#     # return res  编码json.dumps() --python对象转换为json   解码   json.loads()  json格式字符转换成python对象
#     return json.dumps(res, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ':'))


# if __name__=='__main__':
#     url = r"https://erp-beta.yjyz.com/api/sso/oidc/authorize"
#     ir = ApiRequest()
#     data = get_data()
#     result = ir.run_method(url=url,method='get',data=data)
#     print(result)