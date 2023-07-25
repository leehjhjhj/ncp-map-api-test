import json
import urllib
from urllib.request import Request, urlopen
from decouple import config

def get_location(loc):
    """
    도로명 주소로 좌표 찾는 로직
    """
    client_id = config('CLIENT_ID')
    client_secret = config('CLIENT_SECRET')
    url = f"https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode?query=" \
    			+ urllib.parse.quote(loc)
    

    request = urllib.request.Request(url)
    request.add_header('X-NCP-APIGW-API-KEY-ID', client_id)
    request.add_header('X-NCP-APIGW-API-KEY', client_secret)
    
    response = urlopen(request)
    res = response.getcode()
    
    if (res == 200) :
        response_body = response.read().decode('utf-8')
        response_body = json.loads(response_body)

        if response_body['meta']['totalCount'] == 1 : 

            lat = response_body['addresses'][0]['y']
            lon = response_body['addresses'][0]['x']
            return (lon, lat)
        else :
            print('location not exist')
        
    else :
        print('ERROR')


def get_optimal_route(start, goal):
    """
    두 사이의 길을 찾아주는 로직
    """
    client_id = config('CLIENT_ID')
    client_secret = config('CLIENT_SECRET')

    url = f"https://naveropenapi.apigw.ntruss.com/map-direction/v1/driving?start={start[0]},{start[1]}&goal={goal[0]},{goal[1]}&option=trafast"
    request = urllib.request.Request(url)
    request.add_header('X-NCP-APIGW-API-KEY-ID', client_id)
    request.add_header(f'X-NCP-APIGW-API-KEY', client_secret)
    
    response = urllib.request.urlopen(request)
    res = response.getcode()
    
    if (res == 200) :
        response_body = response.read().decode('utf-8')
        return json.loads(response_body)
            
    else :
        print('ERROR')

def milliseconds_to_minutes_seconds(milliseconds):
    """
    밀리세컨즈로 나오는 duration 값을 ~분 ~초로 바꿔주는 로직
    """
    seconds = milliseconds // 1000
    minutes, seconds = divmod(seconds, 60)
    return f"{minutes}분 {seconds}초"

# start = '서울특별시 중계로 12길 24'
# goal = '서울특별시 노원구 중계로14가길 29'
start = [127.0813173, 37.6470251]
goal = [127.0824232, 37.6481097]
# 여기서 start는 기사의 현재 위치이고 goal은 미리 테이블에 저장된 QR코드의 위치

result = get_optimal_route(start, goal)

summary = result['route']['trafast'][0]['summary']

distance = summary['distance']
duration = milliseconds_to_minutes_seconds(summary['duration'])

res = {
        "distance": f"{distance}m",
        "duration": duration
       }

print(res)
