import requests
import hashlib
import time
import json
import base64
import rsa
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
#"User-Agent": "YJYZERP/2.23.0 (iPhone8Plus; iOS 13.3.0; zh-Hans-CN)"

header = {"Content-Type":"application/json"}
# 获取token流程
def get_pub():
    URL = r"https://ac.dun.163yun.com/v3/d"
    method = "POST"
    data = {
        "d": "/NdlSQ6h0fw8tJkD36e0DTxxBJ//pBeTZ0xbO.pvi4p.LTNZbFYYLfDdVWwRJcbxsKMaqfndXzHejXpKipLS6oa4F6yDX7x.rgHx28qDeyB8vBH.n14qHwenTrYwki9WKW6b1L8eeHZe.69hoC1X8tnllICxQK+FjNjr.AhVWbNvx9B.LKkR1tJr0D3c0wcw0h9lPkFS7Ey4LycCj1zLgZhfDPTotbWmg9..jZfwtxUScsz4aiIlWuQRUsckpI/60nuQpOSFZnBOFTZBGR8c+DkpJniX3sq3Z4YnB1+b7ZBRkdIA8fPMf02zeSscDUvAeI9S0JpeUFqY0XU0l1I/n4pWODqWP0qyfAn/O8JiG4lGCaHVJjidnjyHJBBu2SgO0yqqyY.ViK/dF1vvV4.zpfVAG/34vUK00r1LjHXRCrH4OOgW4OjLay/2n/hv0V8CzHKhya9EhFeRqGoWdaxzNxJSgQ0ZiBZMGFTkr32Ho4aNmdqt93eGMHI9i.1DQ1M9gq00M3vFLnDh3NpNwxtEMj6g2qFQtsHg8mgYE9QWBU6VsfuCFpPaZmE8v7hdGjdRmO+2.xWvUEt1VN21U0AjbV0hUVYKVLjCqzHSHixVDAjkonAibIklsAyiUowcHQRq94DMJGYPax4oLZ7jLBZZ9oOdAkFcRFJIXtI4qpJX1QL6Jgp7H7DWaQNy4kkQbJDdKrmXDKY.0PaLZYWapmn7dlgCtSdzxTnpAxC8UDrUUK2LJNAGF/XZz1x0MOTJ0TnFKzHdPTqKc9lt/Wg9bbvZLfszDSXhM9MSX6xIDkm1P0V1nRTkstmjAVcJVL+1wddYY4.NmUykAKGUjUHgmYi3r3jZ2rrZGBnERPTP6VbNIMFnCYYPQhnoNzgDbAbIJNotXIjveuneNrDGEGCTFtUglBqHnBEJivPwDXC8F+FWWjP8hXpK"}
    data_json = requests.post(url=URL, data=data).text
    print(data_json, type(data_json))
    # 获取公钥接口
    key_url = r"https://erp-beta.yjyz.com/api/sso/security/k"
    key_data_json = requests.get(url=key_url).json()
    pub = key_data_json["data"]
    print("公钥是：" + pub, type(pub))
    return pub

# 加密后的密码
def rsaEncrypt(passwd3):
    pub1 = get_pub()
    pub1 = pub1.replace('-', '+')
    pub1 = pub1.replace('_', '/')
    pub1 = "-----BEGIN PUBLIC KEY-----\n%s\n-----END PUBLIC KEY-----" % pub1
    rsakey = rsa.PublicKey.load_pkcs1_openssl_pem(pub1.encode())
    crypto = rsa.encrypt(passwd3.encode(), rsakey)
    return base64.b64encode(crypto).decode()


# 需要MD5字段方法
def md5Encode():
    str = '18797908791'
    # 创建md5对象
    m = hashlib.md5()
    m.update(str.encode('utf-8'))  # 传入需要加密的字符串进行MD5加密
    return m.hexdigest()  # 获取到经过MD5加密的字符串并返回
#获取code_key,第一个接口
def get_codekey():
    URL1 = r"https://erp-beta.yjyz.com/api/sso/oidc/authorize"
    authorizeParams = {
        "scope": "openid",
        "response_type": "code",
        "client_id": "585014642717982720",
        "redirect_url": "https://localhost:8443/uac/",
        "auth_type": "BPassword",
        "state":md5Encode()
    }
    # utc_now = time.strftime('%Y-%m-%dT%H:%M:%S.471Z', time.localtime(time.time()))
    # print(utc_now)
    # authorizeParams['date'] = utc_now
    print(authorizeParams,URL1)
    data_json1 = requests.get(url= URL1,params=authorizeParams,headers = header).json()
    print("第一个接口响应"+str(data_json1))
    code_key=data_json1['data']['code_key']
    print(code_key)
    return code_key

#获取code，userId，第二个接口
URL2 = r"https://erp-beta.yjyz.com/api/sso/oidc/execute"
exe_data = {
    "c_name": "BPasswordLogin",
    "code_key": get_codekey(),
    "input_param": {
        "username": "18797908791",
        "password": rsaEncrypt("c12345678"),
        "regionCode": "86"}
}
exe_data_json = json.dumps(exe_data)
exe_json = requests.post(headers=header, data=exe_data_json, url=URL2).json()
print("第二个接口响应" + str(exe_data), str(exe_json))
code = exe_json['data']['code']
userId = exe_json['data']['userIdStr']
state = exe_json['data']['state']


#第三个接口
def get_token():
    URL3 = r"https://erp-beta.yjyz.com/api/sso/oidc/accessToken"
    accessToken_data = {
        "client_id": "585014642717982720",
        "client_secret": "b9c7398eebe909a01603d5fba2c55086"}
    accessToken_data['code'] = code
    accessToken_data['userId'] = userId
    accessToken_data['state'] = state
    accessToken_data_json = json.dumps(accessToken_data)
    accessToken_data_res = requests.post(headers=header, data=accessToken_data_json, url=URL3).json()
    print(accessToken_data_res)
    access_token = accessToken_data_res['data']['access_token']
    print("返回的token为：" + access_token)


access_token = get_token()
