class var_config():
    def __init__(self):
        self.is_login = False
        self.api_url = 'https://cloudmusic.api.zhiqin.eu.org'
        self.cookie = open('cookie.txt', 'r').read()
        self.logout = '/logout'
        self.login_status = '/login/status'
        self.key_generate = '/login/qr/key'
        self.qr_generate = '/login/qr/create'
        self.qr_scan_status = '/login/qr/check'
        self.get_user_detail = '/user/detail'
        self.get_user_level = '/user/level'
        self.get_user_binding = '/user/binding'
        self.send_sms_code = '/captcha/sent'
        self.verify_sms_code = '/captcha/verify'
        self.update_user_profile = '/user/update'
