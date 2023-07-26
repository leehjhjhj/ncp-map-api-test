import requests
from decouple import config
import hashlib
import hmac
import base64
import requests
import time
import json
import random

def make_auth_number():
    """
    인증번호를 생성하는 함수
    """
    random_six_digit = random.randint(100000, 999999)
    return random_six_digit


def send_sms():
    """
    sms를 보내주는 로직
    """
    timestamp = int(time.time() * 1000)
    timestamp = str(timestamp)

    access_key = config('ACCESS_KEY')			# access key id (from portal or Sub Account)
    secret_key = config('SECRET_KEY')

    secret_key = bytes(secret_key, 'UTF-8')
    serviceId = config('SERVICE_ID')

    short_url = f"/sms/v2/services/{serviceId}/messages"
    long_url = f"https://sens.apigw.ntruss.com/sms/v2/services/{serviceId}/messages"

    message = "POST" + " " + short_url + "\n" + timestamp + "\n" + access_key
    message = bytes(message, 'UTF-8')
    signature = base64.b64encode(hmac.new(secret_key, message, digestmod=hashlib.sha256).digest())

    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "x-ncp-apigw-timestamp": timestamp,
        "x-ncp-iam-access-key": access_key,
        "x-ncp-apigw-signature-v2": signature,
    }
    auth_number = make_auth_number()
    data = {
                "type":"SMS",
                "from":"01082593234",
                "countryCode":"82",
                "content": "내용",
                "messages":[
                    {
                        "to":"01082593234",
                        "content": f"[큐택] 인증번호 [{auth_number}]를 입력해주세요."
                    }
                ]
            }
    res = requests.post(long_url, headers=headers, data=json.dumps(data))
    return auth_number

auth_number = send_sms()