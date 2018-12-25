* register user

```
curl --header "Content-Type: application/json" \
	--request POST \
	--data '{"user": {"email": "prabhatiitbhu@gmail.com","password": "01Pass1234","username": "prabhatiitbhu"}}' \
	http://localhost:8000/api/users/register/

```
* login user

```
curl --header "Content-Type: application/json" \
	--request POST \
	--data '{"user": {"email": "prabhatiitbhu@gmail.com","password": "01Pass1234"}}' \
	http://localhost:8000/api/users/login/
```
* test token

```
python token_test.py
```