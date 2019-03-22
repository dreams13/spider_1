import requests
import time
from random import randint
import hashlib
import json
from jsonpath import jsonpath


def youdao(word):
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    headers = {
        'Referer': 'http://fanyi.youdao.com/',
        'Cookie': 'OUTFOX_SEARCH_USER_ID_NCOO=1364273349.7535648; OUTFOX_SEARCH_USER_ID="845451599@10.169.0.83"; JSESSIONID=aaaaOAKhVifPJawXmAKMw; ___rl__test__cookies=1553241779768',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
    ts = str(int(time.time() * 1000))
    salt = ts + '%s' % randint(0, 9)
    sign = hashlib.md5()
    sign.update(("fanyideskweb" +word + salt + "1L5ja}w$puC.v_Kz3@yYn").encode())
    sign = sign.hexdigest()

    data_dict = {
        'i': word,  # 人生苦短，我用python
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': salt,
        'sign': sign,
        'ts': ts,
        'bv': 'c12ad7e50e867b1e60c9bd86cce4f75d',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_CLICKBUTTION',
        'typoResult': 'false'
    }
    print(data_dict)
    response = requests.post(url=url, headers=headers, data=data_dict)
    print(response.text)
    result = json.loads(response.text)
    print(result["translateResult"][0][0]['tgt'])
    print(jsonpath(result, '$..tgt')[0])

if __name__ == '__main__':
    youdao('我爱你')
