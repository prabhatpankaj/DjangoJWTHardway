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

* update user profile

```
curl --header "Content-Type: application/json" \
	 --header "Authorization: Token eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiZXhwIjoxNTUwOTM2OTQ0fQ._yGt9nvfiFmd_kWsQD6igwt6CWKy3OZiw8cE-sWaSzo" \
	--request PUT \
	--data '{"user": {"email": "prabhatiitbhu@gmail.com","profile": {"bio": "hello this is my bio"}}}' \
	http://localhost:8000/api/user/

```

* get user profile

```

curl --header "Content-Type: application/json" \
	--request GET \
	http://localhost:8000/api/profiles/prabhatiitbhu/

```

* follow somene profile

```
curl --header "Authorization: Token eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiZXhwIjoxNTUwOTM2OTQ0fQ._yGt9nvfiFmd_kWsQD6igwt6CWKy3OZiw8cE-sWaSzo" \
	--request POST \
	http://localhost:8000/api/profiles/otherusername/follow/

```
* test token

```
python token_test.py
```