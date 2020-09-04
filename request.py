import requests


data = {"text": "free perfume"}
response = requests.post("{}/".format("http://127.0.0.1:5001"), json =data )
#response = requests.get("http://127.0.0.1:5001")
print("The prediction is "+ str(response.json()))
