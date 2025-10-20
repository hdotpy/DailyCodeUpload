import requests,time

def test_postapi():
    token = "4e1db3d9c3f7a2830fa41d196d36e8b166c2c06b85421d63cc2bce7220141a40"
    url = "https://gorest.co.in//public/v2/users"

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    def unique_title():
        return f"update_{int(time.time())}@example.com"
    
    payload = {
        "name": "Test User",
        "email":unique_title(),
        "gender":"male",
        "status":"active"
    }

    response = requests.post(url, json=payload, headers=headers)

    json_data = response.json()
    print(response.status_code)
    print(json_data)
    assert response.status_code == 201
    assert json_data['name'] == "Test User"
    assert json_data['status'] == "active"