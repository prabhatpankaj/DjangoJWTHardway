import json
import requests
import time

def main():
    user_data = {"user": {"email": "prabhatiitbhu@gmail.com", "password": "01Pass1234"}}
    login = requests.post('http://127.0.0.1:8000/api/users/login/',
                     data=json.dumps(user_data),
                     headers={'Content-Type':'application/json'})
    login_token = login.json()['user']['token']
    token = 'Token '+login_token


    for i in range(30):
        profile = requests.get('http://127.0.0.1:8000/api/user/',
                     headers = {'Accept-Encoding': 'UTF-8','Authorization': token, 'Content-Type': 'application/json'})
        time.sleep(5)
        token = 'Token '+profile.json()['user']['token']
        print token


if __name__ == '__main__':
    main()