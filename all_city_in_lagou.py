import requests
from jsonpath import jsonpath
import json

url = 'https://www.lagou.com/lbs/getAllCitySearchLabels.json'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}
response = requests.get(url=url, headers=headers)
response_dict = json.loads(response.text)
all_city = jsonpath(response_dict, '$..name')
with open('all_city.txt', 'w') as file:
    content = json.dumps(all_city, ensure_ascii=False)
    file.write(content)