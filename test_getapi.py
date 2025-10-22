import pytest
import requests

def test_getapi():
    response = requests.get("https://gorest.co.in/public/v2/users/7500453/posts")
    print(response.text)
    assert response.status_code == 200
    json_data = response.json()
    print(json_data[0]['id'])
    assert json_data[0]['id'] == 165483
    print(json_data[1]['id'])
    assert json_data[1]['id'] == 165482