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
회원가입 로직에 넣은 뒤, 해당 인증번호를 처리하는 로직을 넣으면 참 좋겠다.
예를들어서 전화번호 인증 화면에서, 처음 send_sns 함수를 부른 뒤에 어디 변수에 넣어두고 매개 변수에 verify_auth_number(): 함수에서
post된 request body의 auth_number과 비교해서 status code를 뱉는..? 