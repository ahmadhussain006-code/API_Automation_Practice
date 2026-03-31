import random
import requests


BASE_URL = "https://automationexercise.com"


def generate_email():
    return f"ahmad_test_{random.randint(10000, 99999)}@test.com"


def test_create_verify_get_update_delete_user():
    email = generate_email()
    password = "Test@123"

    create_payload = {
        "name": "Ahmad Hussain",
        "email": email,
        "password": password,
        "title": "Mr",
        "birth_date": "24",
        "birth_month": "11",
        "birth_year": "1991",
        "firstname": "Ahmad",
        "lastname": "Hussain",
        "company": "QA Company",
        "address1": "Lucknow Street",
        "address2": "UP",
        "country": "India",
        "zipcode": "226001",
        "state": "UP",
        "city": "Lucknow",
        "mobile_number": "9999999999"
    }

    create_response = requests.post(f"{BASE_URL}/api/createAccount", data=create_payload)
    print("CREATE RESPONSE:", create_response.status_code, create_response.text)
    assert create_response.status_code == 200 or create_response.status_code == 201

    login_payload = {
        "email": email,
        "password": password
    }

    login_response = requests.post(f"{BASE_URL}/api/verifyLogin", data=login_payload)
    print("LOGIN RESPONSE:", login_response.status_code, login_response.text)
    assert login_response.status_code == 200

    get_response = requests.get(
        f"{BASE_URL}/api/getUserDetailByEmail",
        params={"email": email}
    )
    print("GET USER RESPONSE:", get_response.status_code, get_response.text)
    assert get_response.status_code == 200
    assert email in get_response.text

    update_payload = {
        "name": "Ahmad Hussain Updated",
        "email": email,
        "password": password,
        "title": "Mr",
        "birth_date": "24",
        "birth_month": "11",
        "birth_year": "1991",
        "firstname": "Ahmad",
        "lastname": "Hussain",
        "company": "QA Company Updated",
        "address1": "Updated Address",
        "address2": "UP",
        "country": "India",
        "zipcode": "226001",
        "state": "UP",
        "city": "Lucknow",
        "mobile_number": "9999999999"
    }

    update_response = requests.put(f"{BASE_URL}/api/updateAccount", data=update_payload)
    print("UPDATE RESPONSE:", update_response.status_code, update_response.text)
    assert update_response.status_code == 200

    delete_payload = {
        "email": email,
        "password": password
    }

    delete_response = requests.delete(f"{BASE_URL}/api/deleteAccount", data=delete_payload)
    print("DELETE RESPONSE:", delete_response.status_code, delete_response.text)
    assert delete_response.status_code == 200