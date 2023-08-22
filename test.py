'''
 def login():
#     global login_status, cookie
#     if not login_status:
#         key = requests.get(f'{api_url}/login/qr/key?timestamp={time_stamp}')
#         if key.json()['code'] == 200:
#             real_key = key.json()['data']['unikey']
#             qrcode = requests.get(f'{api_url}/login/qr/create?key={real_key}&qrimg=base64&timestamp={time_stamp}')
#             if qrcode.json()['code'] == 200:
#                 base64_str = qrcode.json()['data']['qrimg']
#                 print(base64_str)
#                 head, content = base64_str.split(',')
#                 imgdata = base64.b64decode(content)
#                 with open('qr_login.png', 'wb') as f:
#                     f.write(imgdata)
#                 os.startfile('qr_login.png')
#                 qrcode_status = 0
#                 while True:
#                     code_status = requests.get(f'{api_url}/login/qr/check?key={real_key}&timestamp={time_stamp}')
#                     qrcode_status = code_status.json()['code']
#                     if qrcode_status == 800:
#                         print(code_status.json()['message'])
#                         break
#                     elif qrcode_status == 803:
#                         break
#                 print('登录成功！')
#                 with open('cookie.txt', 'w', encoding='utf-8') as f:
#                     f.write(code_status.json()['cookie'])
#                 login_status = True
#     else:
#         req = requests.get(f'{api_url}/login/status?timestamp={time_stamp}&cookie={cookie}')
#         # print(cookie)
#         print(req.json())


# login()
'''