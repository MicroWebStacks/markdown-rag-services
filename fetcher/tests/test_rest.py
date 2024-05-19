import requests
import utils as utl

def send_post_request():
    # Define the URL of the Flask app
    url = 'http://127.0.0.1:8001/fetch'
    
    # Define the JSON payload for the POST request
    payload = {
        "fetch_list": [
            {
                "type": "github",
                "repository": "HomeSmartMesh/website",
                "ref": "main",
                "path": "repos",
                "filter": "content/3dprinting/**/*"
            }
        ]
    }
    
    print("Sending the POST request")
    response = requests.post(url, json=payload)
    # Print the status code and response data
    print("Status Code:", response.status_code)
    utl.save_json(response.json(),"response.json")

# Call the function to send the request
send_post_request()
