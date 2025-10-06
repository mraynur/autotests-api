import httpx

base_url = 'http://localhost:8000'

login_payload = {
    "email": "test@example.com",
    "password": "test"
}

with httpx.Client(base_url=base_url, timeout=10) as client:

    try:
        payload_response = client.post('/api/v1/authentication/login', json=login_payload)
        payload_response.raise_for_status()
        payload_response_data = payload_response.json()

        access_token = payload_response_data['token']['accessToken']

        client.headers = {"Authorization": f"Bearer {access_token}"}

        user_response = client.get('/api/v1/users/me')
        user_response.raise_for_status()
        user_response_data = user_response.json()

        print("User Data:", user_response_data)
        print("Status Code:", user_response.status_code)

    except httpx.HTTPStatusError as e:
        print(f"Ошибка запроса: {e}")

    except httpx.ReadTimeout:
        print("Запрос превысил лимит времени")
