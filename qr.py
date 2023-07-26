import qrcode
import os
from PIL import Image
import json

def make_qrcode():
    """
    qrcode를 생성하는 함수
    """
    save_path = "qrcodes/blog.png"
    thumb_path = "qrcodes/thumbnail/qrtaxi_thumb.jpg"

    if os.path.exists(save_path):
        os.remove(save_path)

    thumb_img = Image.open(thumb_path)
    thumb_img.thumbnail((200, 200))

    qr = qrcode.QRCode(
        box_size=20,
        border=1
    )
    data = {
        "img_url": "https://imasimdi.tistory.com",
        "location": "1"
    }
    qr.add_data(json.dumps(data))
    qr.make()

    qr_result = qr.make_image().convert('RGB')
    pos = ((qr_result.size[0] - thumb_img.size[0]) // 2, (qr_result.size[1] - thumb_img.size[1]) // 2)
    qr_result.paste(thumb_img, pos)
    qr_result.save("qrcodes/blog.png")


