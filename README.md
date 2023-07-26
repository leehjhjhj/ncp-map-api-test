# 큐택을 위한 NCP api 연습레포
## distance_test.py
- example response
```json
{
	"distance": "230m",
	"expect_duration": "1분 21초"
}
```
## static_map_test.py
- example response<br>
![Alt text](images/map_image.png)

## sms.py
- example result<br>
![Alt text](images/sms_exmaple.png)<br>
회원가입 로직에 넣은 뒤, 해당 인증번호를 처리하는 로직을 넣으면 참 좋겠다.<br>
예를들어서 전화번호 인증 화면에서, 처음 send_sns 함수를 부른 뒤에 어디 변수에 넣어두고 매개 변수에 verify_auth_number(): 함수에서<br>
post된 request body의 auth_number과 비교해서 status code를 뱉는..?

## qr.py
- exmple result <br>
![Alt text](qrcodes/blog.png)
- data에 location을 넣어야 할지? (추가적인 javascript 코드 필요)
- 아니면 url에 location 정보를 넣어아햘지? ex) https://qrtaxi.com/1
- 후자는 사용자 임의로 장소를 바꿔서 taxi를 부르게 될 수도 있는 위험이 있다.