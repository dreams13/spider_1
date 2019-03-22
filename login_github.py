import requests
import re

# <input type="hidden" name="authenticity_token"
# value="tjPJ2Xe7tVzEoSBP7XksVrYyipOn0RC5p0sURTgqgE0scdq9bKWL
# MOXPOIryhyFsj8M0VtLtXlD1I474VnjaOQ==" />

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}
s = requests.session()
s.headers = headers
responses = s.get('https://github.com/login')
# print(responses.text)

caption = 'name="authenticity_token" value="(.*?)" />'
authenticity_token = re.search(caption, responses.text).group(1)
print(authenticity_token)
url = 'https://github.com/session'
payload = {
    'commit': 'Sign in',
    'utf8': '✓',
    'authenticity_token': authenticity_token,
    'login': '932956088@qq.com',
    'password': 'handong102519',
    'webauthn-support': 'supported'
}
s.post(url=url, data=payload)
print(s.headers)


response = s.get('https://github.com/dreams13')
with open('hub.html','wb')as file:
    file.write(response.content)
