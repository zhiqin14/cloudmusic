# *-* coding = 'utf-8' *-* #
import requests
import base64
import sys
from var_config import var_config
from ui_cloudmusic import Ui_CloudMusic
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtGui import QPixmap, QImage
from PySide2.QtCore import QByteArray

const = var_config()

class CloudMusic(QMainWindow, Ui_CloudMusic):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.setup()
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
                        'cookie': const.cookie}
    
    def setup(self):
        if not const.is_login:
            self.loginButton.setEnabled(True)
        else:
            self.loginButton.setEnabled(False)
            self.loginStatus.setText('已经登陆啦')
        self.loginButton.clicked.connect(self.to_login)
    
    def to_login(self):
        key = requests.get(const.api_url+const.key_generate, headers=self.headers).json()['data']['unikey']
        print(key)
        qr_base64 = requests.get(const.api_url+const.qr_generate+f'?key={key}&qrimg="base64"', headers=self.headers).json()['data']['qrimg'].split(',')[1]
        qr_imgdata = base64.b64decode(qr_base64)
        qr_array = QByteArray(qr_imgdata)
        qr_img = QImage.fromData(qr_array)
        qr_pixmap = QPixmap.fromImage(qr_img)
        self.qrcode.setPixmap(qr_pixmap)
        scan_result = requests.get(const.api_url+const.qr_scan_status+f'key={key}').json()
        while scan_result['code'] != 803:
            if scan_result['code'] == 800:
                self.loginStatus.setText('二维码过期了捏，重新登录叭')
            elif scan_result['code'] == 802:
                self.loginStatus.setText('扫码成功！')
            scan_result = requests.get(const.api_url+const.qr_scan_status+f'key={key}').json()
        with open('cookie.txt', 'w', encoding='utf-8') as file:
            file.write(scan_result['cookie'])
        self.loginStatus.setText('成功了捏')
        self.loginButton.setEnabled(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CloudMusic()
    sys.exit(app.exec_())

