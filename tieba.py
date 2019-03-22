import requests
from lxml import etree
import js2py

context = js2py.EvalJs


class TieBa(object):
    def __init__(self, name):
        self.url = 'https://tieba.baidu.com/f?ie=utf-8&kw=%s' % name
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
        }

    def get_response(self, url):
        response = requests.get(url=url, headers=self.headers)
        return response.content

    def get_url(self, url_list):
        url_list = url_list.decode().replace('<!--', '').replace('-->', '')
        html = etree.HTML(url_list)
        hrefs_titles = html.xpath("//a[contains(@class,'j_th_tit')]")
        data_list = []
        for href_title in hrefs_titles:
            temp = {}
            temp['title'] = href_title.xpath('./@title')[0]
            temp['href'] = 'http://tieba.baidu.com' + href_title.xpath('./@href')[0]
            data_list.append(temp)
        try:
            next_page = 'https:' + html.xpath('//a[text()="下一页>"]/@href')[0]
        except:
            next_page = None
        return data_list, next_page

    def parse_detail_page(self,data):
        html = etree.HTML(data)
        imgs_url = html.xpath("//img[contains(@class,'BDE_Image')]/@src")
        for img_url in imgs_url:
            print(img_url)


    def download(self, url):
        pass

    def run(self):
        data = self.get_response(self.url)
        url_list, next_page = self.get_url(data)
        print(url_list, next_page)
        for url in url_list:
            detail_page = self.get_response(url['href'])
            self.parse_detail_page(detail_page)


if __name__ == '__main__':
    tieba = TieBa('李毅')
    tieba.run()
