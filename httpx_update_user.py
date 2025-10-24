import httpx

from tools.fakers import fake

base_url = 'http://localhost:8000'

create_user_payload = {
  "email": fake.email(),
  "password": "string",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}

login_payload = {
  "email": create_user_payload['email'],
  "password": create_user_payload['password']
}

update_user_payload = {
  "email": "user@mail.com",
  "lastName": "Userov",
  "firstName": "User",
  "middleName": "Userovich"
}

with httpx.Client(base_url=base_url, timeout=10) as client:

    try:
        create_user_response = client.post('/api/v1/users', json=create_user_payload)
        create_user_response.raise_for_status()
        create_user_response_data = create_user_response.json()

        login_response = client.post('/api/v1/authentication/login', json=login_payload)
        login_response.raise_for_status()
        login_response_data = login_response.json()

        access_token = login_response_data['token']['accessToken']
        client.headers = {"Authorization": f"Bearer {access_token}"}

        update_user_response = client.patch(
            f'/api/v1/users/{create_user_response_data['user']['id']}',
            json=update_user_payload
        )
        update_user_response.raise_for_status()
        update_user_response_data = update_user_response.json()

        print('Updated User Data', update_user_response_data)

    except httpx.HTTPStatusError as e:
        print(f"Ошибка запроса: {e}")

    except httpx.ReadTimeout:
        print("Запрос превысил лимит времени")
