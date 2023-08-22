import base64

class save_img:
    def __init__(self, img_base64):
        self.img_base64 = img_base64
        print(self.img_base64)
    
    def save(self, path, qrcode):
        imgdata = base64.b64decode(self.img_base64)
        img = open(path, 'wb')
        img.write(imgdata)
        img.close()
        qrcode.setText('已经保存到'+path+'啦')
