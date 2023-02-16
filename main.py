import requests
# My fake server: https://my-json-server.typicode.com/KRISMOK95/MT

url = "https://my-json-server.typicode.com/KRISMOK95/MT/Failures/1"

response = requests.get(url)

response_json = response.json()
print(response_json)

####

num1 = 10
num2 = 20
total = num1 + num2
print(f"Sum: " , total)
new_data = {
    "id": 4, "title": "explosion"
}
url_post = "https://my-json-server.typicode.com/KRISMOK95/MT/Failures/"

post_response = requests.post(url_post, json=new_data)

post_response_json = post_response.json()
print(post_response_json)