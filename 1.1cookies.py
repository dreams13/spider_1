import requests

url = 'https://github.com/dreams13'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    'Cookie': '_octo=GH1.1.892628010.1548684475; _ga=GA1.2.46004664.1548684483; user_session=aqZI6LHyEpOihKV1otuo31froz1umBTVhd71s_Gk0dfOPFru; __Host-user_session_same_site=aqZI6LHyEpOihKV1otuo31froz1umBTVhd71s_Gk0dfOPFru; logged_in=yes; dotcom_user=dreams13; tz=Asia%2FShanghai; has_recent_activity=1; _gat=1; _gh_sess=d2JjZEZJbTFQOG4zb3JkcDUrMXUzM0NMQmhnUFY0Z3ViOGhXSG81dlJnTnordHNZMTNPWFh1NldDb0k5bEZMaGJZZW9jZEF3SDFqT3pNVkorR1FaaktZYVJQL2JWSnVrekZIdURXYWVQcUhNTWJLbElzWHV1TVpHa1BXOGJkSlJmRkRWS2VONG9hMkdLaU9QR1RYa3dVUUxZK21ITjNUb2Q4bFByNERneUdyWHNqWTFTeUZSYzlFVUZnSU1ubHloNTY2dFRVOTd0Kzh6MnpYdGdHaFhLTUFCZ2tJMUVRS0p6SzVCQUVoT2Ntcz0tLVBJTmhrRTFpd3B5UjE1amxGUUw5UFE9PQ%3D%3D--25bf65a203ec6da5057869983bebdc031115a861'
}
response = requests.get(url, headers=headers)
# print(response.text)
print(response.cookies)
cookies_dict = requests.utils.dict_from_cookiejar(response.cookies)
print(cookies_dict)


r = requests.get('https://api.github.com/events')
print(r.text)
