import requests
import hashlib
import time
import json
# 登录注册页面请求的接口
URL = r"https://ac.dun.163yun.com/v3/d"
method = "POST"
data = {"d":"/NdlSQ6h0fw8tJkD36e0DTxxBJ//pBeTZ0xbO.pvi4p.LTNZbFYYLfDdVWwRJcbxsKMaqfndXzHejXpKipLS6oa4F6yDX7x.rgHx28qDeyB8vBH.n14qHwenTrYwki9WKW6b1L8eeHZe.69hoC1X8tnllICxQK+FjNjr.AhVWbNvx9B.LKkR1tJr0D3c0wcw0h9lPkFS7Ey4LycCj1zLgZhfDPTotbWmg9..jZfwtxUScsz4aiIlWuQRUsckpI/60nuQpOSFZnBOFTZBGR8c+DkpJniX3sq3Z4YnB1+b7ZBRkdIA8fPMf02zeSscDUvAeI9S0JpeUFqY0XU0l1I/n4pWODqWP0qyfAn/O8JiG4lGCaHVJjidnjyHJBBu2SgO0yqqyY.ViK/dF1vvV4.zpfVAG/34vUK00r1LjHXRCrH4OOgW4OjLay/2n/hv0V8CzHKhya9EhFeRqGoWdaxzNxJSgQ0ZiBZMGFTkr32Ho4aNmdqt93eGMHI9i.1DQ1M9gq00M3vFLnDh3NpNwxtEMj6g2qFQtsHg8mgYE9QWBU6VsfuCFpPaZmE8v7hdGjdRmO+2.xWvUEt1VN21U0AjbV0hUVYKVLjCqzHSHixVDAjkonAibIklsAyiUowcHQRq94DMJGYPax4oLZ7jLBZZ9oOdAkFcRFJIXtI4qpJX1QL6Jgp7H7DWaQNy4kkQbJDdKrmXDKY.0PaLZYWapmn7dlgCtSdzxTnpAxC8UDrUUK2LJNAGF/XZz1x0MOTJ0TnFKzHdPTqKc9lt/Wg9bbvZLfszDSXhM9MSX6xIDkm1P0V1nRTkstmjAVcJVL+1wddYY4.NmUykAKGUjUHgmYi3r3jZ2rrZGBnERPTP6VbNIMFnCYYPQhnoNzgDbAbIJNotXIjveuneNrDGEGCTFtUglBqHnBEJivPwDXC8F+FWWjP8hXpK"}
data_json = requests.post(url= URL,data=data).text
print(data_json,type(data_json))
# 获取密钥接口
key_url = r"https://erp-beta.yjyz.com/api/sso/security/k"
key_data_json = requests.get(url= key_url).text
print(key_data_json,type(key_data_json))
#需要加密字段方法
phone = '18797908791'
utc_now = time.strftime('%Y-%m-%dT%H:%M:%S.471Z',time.localtime(time.time()))
print(utc_now)
def md5Encode(str):
    #创建md5对象
    m = hashlib.md5()
    m.update(str)  # 传入需要加密的字符串进行MD5加密
    return m.hexdigest()  # 获取到经过MD5加密的字符串并返回
state = md5Encode(phone.encode('utf-8'))
print(state)
URL1 = r"https://erp-beta.yjyz.com/api/sso/oidc/authorize"
authorizeParams = {
    "scope": "openid",
    "response_type": "code",
    "client_id": "123456789",
    "redirect_url": "https://localhost:8443/uac/",
    "auth_type": "BPassword"
}
authorizeParams['state'] = state
authorizeParams['date'] = utc_now
print(authorizeParams,URL1)

data_json1 = requests.get(url= URL1,params=authorizeParams).json()
print(data_json1,type(data_json1))
code_key=data_json1['data']['code_key']
print(code_key,type(code_key))

URL2 = r"https://erp-beta.yjyz.com/api/sso/oidc/execute"
header = {"Content-Type":"application/json",
          "User-Agent": "YJYZERP/2.23.0 (iPhone8Plus; iOS 13.3.0; zh-Hans-CN)"
          }
exe_data={
    "c_name": "BPasswordLogin",
    "code_key":code_key,
    "input_param": {
        "username": "18797908791",
        "password": "c12345678",
        "regionCode": "86"}
    }
a = json.dumps(exe_data)

exe_json = requests.post(headers =header,data = a, url=URL2).json()
print(exe_data,exe_json,type(exe_data))
code = exe_json['data']['code']
userIdStr = exe_json['data']['userIdStr']
print(code+"12121")

URL3 = r"https://erp-beta.yjyz.com/api/sso/oidc/accessToken"
accessToken_data={
    "client_id":"585014642717982720",
    "client_secret":"b9c7398eebe909a01603d5fba2c55086",
    "state-login": "mobile-login"}
accessToken_data['code'] = code
accessToken_data['userIdStr'] = userIdStr

accessToken_data_json = json.dumps(accessToken_data)
accessToken_data_res = requests.post(headers =header,data = accessToken_data_json, url=URL2).text
print(accessToken_data,accessToken_data_res,type(accessToken_data_res))


