import requests

HOST = "http://127.0.0.1:8000"

res = requests.post(HOST + '/api-token-auth/', {
    'username':'admin',
    'password':'qkrwm207@',
})

res.raise_for_status()
token = res.json()['token']
print(token)

# 인증이 필요한 요청에 아래의 headers를 붙임
headers = {'Authorization' : 'JWT ' + token, 'Accept' : 'application/json'}

# Post Create
data = {
    'title' : '제목 by code (3)', 
    'text' : 'API내용 by code (3)', 
    'created_date' : '2023-06-06T21:29', 
    'published_date' : '2023-06-06T21:29'
}

file = {'image' : open('/Users/qkrwm/Desktop/dog.jpg', 'rb')}
res = requests.post(HOST + '/api_root/post/', data=data, files=file, headers=headers)

print(res)
print(res.json())

"""

CLI를 이용한 테스트 명령어 (윈도우)

curl -v -X POST http://127.0.0.1:8000/api_root/post/ \
-F "title=2017103984 박건희" \
-F "text=2017103984 박건희" \
-F "created_date=2023-06-06T18:50" \
-F "published_date=2023-06-06T18:50" \
-F "image=@/Users/qkrwm/Desktop/cat.jpg; type=image/jpg" \
-u "admin:qkrwm207@" \
# OR use token : -H "Authorization:JWT a0be4089a0b9a33efbff0b82c4bd3eac44198205" \
-H "Accept: application/json" \

"""