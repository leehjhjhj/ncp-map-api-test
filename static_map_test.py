from PIL import Image
import requests
import io
from decouple import config

def get_static_map(goal):
    """
    지정된 좌표가 찍힌 정적 지도를 반환하는 로직
    """
    client_id = config('CLIENT_ID')
    client_secret = config('CLIENT_SECRET')

    headers = {
        "X-NCP-APIGW-API-KEY-ID": client_id,
        "X-NCP-APIGW-API-KEY": client_secret
    }
    url = f"https://naveropenapi.apigw.ntruss.com/map-static/v2/raster?w=400&h=400&markers=type:d|size:mid|pos:{goal[0]}%20{goal[1]}"
    print(url)
    try:
        res = requests.get(url, headers=headers)
        image_data = io.BytesIO(res.content)
        image = Image.open(image_data)
        image.save('map_image.png')
    except:
        print('ERROR')


goal = [127.0813173, 37.6470251]
get_static_map(goal)