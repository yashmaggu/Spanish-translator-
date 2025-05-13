import requests
import json

def test_translation():
    url = "http://localhost:8001/translate"
    payload = {"text": "Hello, how are you today?"}
    headers = {"Content-Type": "application/json"}
    
    print(f"Testing translation with input: {payload['text']}")
    try:
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        print(f"Status code: {response.status_code}")
        if response.status_code == 200:
            result = response.json()
            print(f"Translation result: {result}")
        else:
            print(f"Error response: {response.text}")
    except Exception as e:
        print(f"Exception occurred: {str(e)}")

if __name__ == "__main__":
    test_translation()
