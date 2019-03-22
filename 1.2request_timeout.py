import requests

url = 'http://www.youtube.com'
response = requests.get(url, timeout=3)
