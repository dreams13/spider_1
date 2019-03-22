# -*- coding: utf-8 -*-
import requests
import json
import sys


class King(object):
    def __init__(self, word):
        self.url = 'http://fy.iciba.com/ajax.php?a=fy'
        self.form_data = {
            'f': 'auto',
            't': 'auto',
            'w': word
        }
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
        }

    def get_response(self):
        response = requests.post(headers=self.headers, url=self.url, data=self.form_data)
        result = response.content.decode()
        return result

    def parse_data(self, data):
        result_dict = json.loads(data)
        try:
            out = result_dict['content']['out']
        except:
            out = result_dict['content']['word_mean']
        return out

    def run(self):
        result = self.get_response()

        print(self.parse_data(result))


if __name__ == '__main__':
    word = sys.argv[1]
    # while True:
    #     word = input('请输入要翻译的内容:\n\t')
    king = King(word)
    king.run()
