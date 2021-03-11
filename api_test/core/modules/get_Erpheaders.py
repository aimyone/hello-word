from bin.module.get_token_b import *

authorization = get_token('c12345678', '18797908791', 'BPassword')


def get_header():
    headers = {
        "X-Organ-Id": "670010683867799680",
        "authorization": authorization,
        "x-city-code": "440100",
        "content-type": "application/x-www-form-urlencoded",
        "access-control-expose-headers":"Authorization",
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'

    }
    return headers


get_header()
