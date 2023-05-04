

import datetime
import re

def create_membership():
    now = datetime.datetime.now()
    stnr_date = now.strftime('%Y%m%d')
    
    users = []
    user = {}

    while True:

        while True: 
        input_id/username=input("아이디를 입력하세요:  ")
        if 2<=len(unsername)<=4 and re.match('^[가-힣]{2,4}$', username):
            user['username']=username
            break
        else:
            print('아이디를 다시 입력하세요.')

        while True:
        password=input("비밀번호를 입력하세요.")
        if len(password)>=8:
            if password[0].isupper():
                if '!' in password or '@' in password or '#' in password or '$' in password:
                    user['password']=password
                    break
        else: 
            print('비밀번호를 다시 입력하세요.')

                     #else:
                        #print('특수문자 (!, @, #, $) 중 1가지를 포함시켜 주세요.')
               # else:
                   # print('총 글자 수는 8글자 이상이어야 합니다.')
           # else:
               # print('첫 문자는 영문 대문자이어야 합니다.')  
    
        while True:
            email=input('이메일을 입력하세요.')
            regex_email = r"^[a-z0-9]+?[a-z0-9]+[@]\w+[.]\w+[.]?\w{2,3}$"
                if email.endswith('com') and @ in email:
                    user['email'] = email
                    break
            else:
                print('이메일을 다시 입력하세요.')


    user['stnr_date'] = stnr_date

	users.append(user)

    return users



"""
id 제한 조건
- 한글만 입력 받아야 함
- 총 글자 수는 2-4글자

password 제한 조건
- 첫 문자는 영문 대문자
- 총 글자 수는 8글자 이상
- 특수문자 (!, @, #, $) 중 1가지 반드시 포함

email 제한 조건
- @를 제외한 특수문자는 입력될 수 없음 (입력 가능한 문자는 숫자와 영문)
- 통상적인 email 포맷을 따름
  * @을 포함하고, '.com'으로 이메일 주소가 끝나야 함
  

**/데이터 예시/**
{홍산하, Asdf1234!, sannah@naver.com, 20230427}
{김한준, Q1w2e3r4!, zhivagokim@naver.com, 20230427}
{천승범, Zxcv4860!, vision6@naver.com, 20230427}

반복문과 조건문을 잘 활용하여, 사용자가 입력을 중단할 때까지 입력 받을 수 있도록 코드를 작성할 것
"""

def load_to_txt(user_list):
    f = open('memberdb.txt', 'w', encoding='UTF-8')
    f.close()
    
def run():
    user_list = create_membership()
    load_to_txt(user_list)
    
run()