import requests

url = 'http://www.baidu.com'
response1 = requests.get(url)
print(len(response1.text))
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'

}
response2 = requests.get(url, headers=headers)
print(len(response2.text))
