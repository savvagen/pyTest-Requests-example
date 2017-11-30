import pytest
import requests
import json
from hamcrest import *
from requests import Request, Session
from entity.user import User
from entity.content_type import ContentType
from entity.customer import *




def get_last_user_id(self):
    url = 'http://localhost:8086/users/all'
    r = requests.get(url)
    user_list = json.loads(r.text)
    last_user = user_list[-1]
    return last_user['user_id']

content_type = ContentType()


class TestServices(object):




    def test_google_maps_service(self):
        url = 'http://maps.googleapis.com/maps/api/directions/json'
        params = dict(
            origin='Chicago,IL',
            destination='Los+Angeles,CA',
            waypoints='Joplin,MO|Oklahoma+City,OK',
            sensor='false'
        )
        r = requests.get(url=url, params=params)
        data = json.loads(r.text)
        assert_that(r.status_code, equal_to(200))
        assert_that(r.json()['status'], equal_to('OK'))
        assert_that(data.get('status'), equal_to('OK'))


    def test_hello_world(self):
        r = requests.get('http://localhost:8086/helloworld')
        body = json.loads(r.text)
        assert_that(r.status_code, equal_to(200))
        assert_that(r.json()['content'], equal_to('Hello, World!'))
        assert_that(body['content'], equal_to('Hello, World!'))


    def test_hello_world(self):
        data = {'name': 'Savva'}
        r = requests.get('http://localhost:8086/helloworld', params=data)
        body = json.loads(r.text)
        assert_that(r.status_code, equal_to(200))
        assert_that(r.json()['content'], equal_to('Hello, Savva!'))
        assert_that(body.get('content'), equal_to('Hello, Savva!'))


    def test_user(self):
        url = 'http://localhost:8086/testUser/1'
        headers = {'content-type': 'application/json', 'accept': 'application/json'}
        r = requests.get(url, headers=headers)
        body = json.loads(r.text)
        assert_that(r.status_code, equal_to(200))
        assert_that(r.json()['id'], 1)
        assert_that(r.json()['firstName'], 'Savva')
        assert_that(body['email'], 'test@gmail.com')
        assert_that(body.get('lastName'), equal_to('Genchevskiy'))


    def test_user_status(self):
        url = 'http://localhost:8086/testUser/status/1'
        headers = {'content-type': 'application/json', 'accept': 'application/json'}
        r = requests.get(url, headers=headers)
        body = json.loads(r.text)
        assert_that(r.status_code, equal_to(200))
        assert_that(body['status'], equal_to('exist'))
        assert_that(body['value']['email'], equal_to('test@gmail.com'))
        assert_that(body.get('value').get('firstName'), equal_to('Savva'))



    def test_with_post_request_user_create(self):
        url = 'http://localhost:8086/users/add'
        data = {
            "email": "test_user1@gmail.com",
            "fullname": "Savva Genchevskiy",
            "password": "s.g19021992",
            "username": "savva_gench"
        }
        headers = {'content-type': 'application/json', 'accept': 'application/json'}
        r = requests.post(url, json.dumps(data), headers=headers)
        body = json.loads(r.text)
        assert_that(r.status_code, equal_to(200))
        assert_that(r.headers.get('content-type'), equal_to('application/json;charset=UTF-8'))
        assert_that(body['status'], 'Saved')
        assert_that(r.json().get('value').get('username'), 'savva_gench')



    def test_with_user_create(self):
        url = 'http://localhost:8086/users/add'
        data = {
            "email": "test_user1@gmail.com",
            "fullname": "Savva Genchevskiy",
            "password": "s.g19021992",
            "username": "savva_gench"
        }
        headers = {'content-type': 'application/json', 'accept': 'application/json'}
        r = requests.post(url, json=data, headers=headers)
        body = json.loads(r.text)
        assert_that(r.status_code, equal_to(200))
        assert_that(r.headers['Content-Type'], equal_to('application/json;charset=UTF-8'))
        assert_that(body['status'], 'Saved')
        assert_that(r.json().get('value').get('username'), 'savva_gench')



    def test_post_with_params(self):
        url = 'http://localhost:8086/users/add'
        params = {
            "fullname": "Savva Genchevskiy",
            "password": "s.g19021992",
            "username": "savva_gench",
            "email": "test_user1@gmail.com",
        }
        headers = {'content-type': 'application/json', 'accept': 'application/json'}
        r = requests.get(url, params=params, headers=headers)
        assert_that(r.status_code, less_than(300))
        assert_that(r.status_code, equal_to(200))
        assert_that(r.text, equal_to('Saved'))



    def test_delete_user(self):
        user_id = get_last_user_id(self)
        url = 'http://localhost:8086/users/remove/' + str(user_id)
        headers = {'content-type': 'application/json', 'accept': 'application/json'}
        r = requests.delete(url, headers=headers)
        body = json.loads(r.text)
        assert_that(r.status_code, equal_to(200))
        assert_that(r.headers.get('content-type'), 'application/json;charset=UTF-8')
        assert_that(body['status'], 'deleted')
        assert_that(body['value']['user_id'], user_id)
        assert_that(r.json().get('value').get('username'), 'savva_gench')



    def test_get_all_users(self):
        url = 'http://localhost:8086/users/all'
        r = requests.get(url)
        user_list = json.loads(r.text)
        first_user = user_list[0]
        last_user = user_list[-1]
        assert_that(r.status_code, equal_to(200))
        assert_that(first_user['user_id'], 1992)
        assert_that(user_list[-1]['username'], 'savva_gench')
        # print(user_list[-1]) -- print the last user in the list



    def test_prepare_session_test(self):
        s = requests.Session()
        s.headers.update({'content-type': 'application/json', 'accept': 'application/json'})
        s.cookies.update({"my_cookie": 'test'})
        url = 'http://localhost:8086/users/add'
        data = {
            "email": "test_user1@gmail.com",
            "fullname": "Savva Genchevskiy",
            "password": "s.g19021992",
            "username": "savva_gench"
        }
        r = s.post(url, json=data)
        body = json.loads(r.text)
        assert_that(r.status_code, equal_to(200))
        assert_that(r.headers['Content-Type'], equal_to('application/json;charset=UTF-8'))
        assert_that(body['status'], 'Saved')
        assert_that(r.json().get('value').get('username'), 'savva_gench')



    def test_prepare_request_test(self):
        s = Session()
        url = 'http://localhost:8086/users/add'
        data = {
            "email": "test_user1@gmail.com",
            "fullname": "Savva Genchevskiy",
            "password": "s.g19021992",
            "username": "savva_gench"
        }
        headers = {'content-type': 'application/json', 'accept': 'application/json'}
        req = Request('POST', url, json=data, headers=headers)
        prepped = req.prepare()
        r = s.send(prepped)
        body = json.loads(r.text)
        assert_that(r.status_code, equal_to(200))
        assert_that(r.headers['Content-Type'], equal_to('application/json;charset=UTF-8'))
        assert_that(body['status'], 'Saved')
        assert_that(r.json().get('value').get('username'), 'savva_gench')




    def test_with_post_request_user_create(self):
        url = 'http://localhost:8086/users/add'
        user = User('test_user1@gmail.com', 'Savva Genchevskiy', 's.g19021992', 'savva_gench')
        headers = {'content-type': content_type.JSON, 'accept': content_type.JSON}
        # data = json.dumps(user, default=lambda o: o.__dict__)
        data = json.dumps(user.__dict__)
        r = requests.post(url, data=data, headers=headers)
        body = json.loads(r.text)
        assert_that(200, r.status_code)
        assert_that(r.headers.get('content-type'), content_type.JSON_UTF8)
        assert_that(body['status'], 'Saved')
        assert_that(r.json().get('value').get('username'), user.username)




    def test_get_customer_deserialize_json(self):
        url = 'http://localhost:8086/testUser/1'
        headers = {'content-type': 'application/json', 'accept': 'application/json'}
        r = requests.get(url, headers=headers)
        customer = json.loads(r.text, object_hook=as_customer)
        assert_that(200, r.status_code)
        assert_that(customer.id, 1)
        assert_that(customer.firstName, 'Savva')
        assert_that(customer.email, 'test@gmail.com')
