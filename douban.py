import requests
from lxml import etree
import json
import os


class DouBan(object):

    def __init__(self):
        self.url = 'https://www.douban.com/doulist/240962/?start=0&sort=seq&playable=0&sub_type='
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
            'Referer': 'https://www.douban.com/doulist/240962/?start=50&sort=seq&playable=0&sub_type='
        }
        self.num = 1

    def get_response(self, url):
        response = requests.get(url=url, headers = self.headers)
        return response.content

    def video_link(self, data):
        html = etree.HTML(data)
        video_items = html.xpath("//div[contains(@class,'bd doulist')]")
        video_list = []
        for video in video_items:
            video_detail = {}
            try:
                video_detail['name'] = video.xpath("div[@class='title']/a[@target]/text()")[1].strip('\n')
            except:
                video_detail['name'] = video.xpath("div[@class='title']/a[@target]/text()")[0].strip('\n')
            video_detail['score'] = video.xpath("div[@class='rating']/span[@class='rating_nums']/text()")[0]
            video_detail['link'] = video.xpath("div/a[@class='doulist-video-item']/@href")
            video_list.append(video_detail)
        try:
            next_page = html.xpath("//a[text()='后页>']/@href")[0]
        except:
            next_page = None
        return video_list, next_page

    def record(self, file):
        if not os.path.exists('video'):
            os.makedirs('video')
        filename = 'video/'+'%s.txt' % self.num
        for video_detail in file:
            for key,value in video_detail.items():
                print(key,value)
        with open(filename, 'w') as f:
            f.write(json.dumps(file, ensure_ascii=False))
        self.num += 1

    def run(self):
        next_url = self.url
        while True:
            data = self.get_response(url=next_url)
            video_list, next_url = self.video_link(data)
            self.record(video_list)
            print('-------爬取中---------')
            if not next_url:
                print('-------爬取完毕---------')
                break



if __name__ == '__main__':
    douban = DouBan()
    douban.run()