import requests
import hashlib
import json
import base64
import rsa
header = {"Content-Type":"application/json"}
#"User-Agent": "YJYZERP/2.23.0 (iPhone8Plus; iOS 13.3.0; zh-Hans-CN)"
#


# 需要MD5字段方法,针对的是手机号码hash
def md5Encode(str):
    # 创建md5对象
    m = hashlib.md5()
    m.update(str.encode('utf-8'))  # 传入需要加密的字符串进行MD5加密
    return m.hexdigest()  # 获取到经过MD5加密的字符串并返回



#获取code_key
def get_codekey(auth_type,phone):
    URL1 = r"https://nn-beta.yjyz.com/api/sso/oidc/authorize"
    authorizeParams = {
        "scope": "openid",
        "response_type": "code",
        "client_id": "585014642717982720",
        "redirect_url": "/login",
        "auth_type": auth_type,
        "state":md5Encode(phone)
    }
    print(authorizeParams,URL1)
    data_json1 = requests.get(url= URL1,params=authorizeParams,headers = header).json()
    print("第一个接口响应"+str(data_json1))
    code_key=data_json1['data']['code_key']
    print(code_key)
    return code_key


#获取code
def get_passwd(passwd,auth_type,phone):
    URL2 = r"https://nn-beta.yjyz.com/api/sso/oidc/execute"
    exe_data = {
        "c_name":auth_type,
        "code_key": get_codekey(auth_type,phone),
        "input_param": {
            "decrypt": "RSA",
            "username": "18797908791",
            "password": passwd,
            "regionCode": "86"}
    }
    exe_data_json = json.dumps(exe_data)
    exe_json = requests.post(headers=header, data=exe_data_json, url=URL2).json()
    print("第二个接口响应" + str(exe_data), str(exe_json))
    code = exe_json['data']['code']
    userId = exe_json['data']['userIdStr']
    state = exe_json['data']['state']
    print(code)
    return code,userId,state


def get_token(passwd,phone,auth_type):
    URL3 = r"https://nn-beta.yjyz.com/api/sso/oidc/accessToken"
    accessToken_data = {
        "client_id": "585014642717982720",
        "client_secret": "b9c7398eebe909a01603d5fba2c55086"}
    list =  get_passwd(passwd,auth_type,phone)
    accessToken_data['code'] = list[0]
    accessToken_data['userId'] = list[1]
    accessToken_data['state'] = list[2]
    accessToken_data_json = json.dumps(accessToken_data)
    accessToken_data_res = requests.post(headers=header, data=accessToken_data_json, url=URL3).json()
    print(accessToken_data_res)
    access_token = accessToken_data_res['data']['access_token']
    print("返回的token为：" + access_token)
    return access_token


get_token('c12345678','18797908791','CPassword')