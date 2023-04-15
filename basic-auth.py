#!python
import requests
from requests.auth import HTTPBasicAuth

# Set up the request URL and credentials
url = "http://172.16.1.5:9200/_security/user?pretty=true"
username = "elastic"
password = "xxxx"

# Make the request
response = requests.get(url, auth=HTTPBasicAuth(username, password))

# Check the response status code
if response.status_code == 200:
    # Print the response content
    print(response.text)
else:
    # Print an error message
    print("Error:", response.status_code, response.reason)

'''
import requests
url = "https://postman-echo.com/basic-auth"
header = {"Authorization" : "Basic cG9zdG1hbjpwYXNzd29yZA=="}
response = requests.get(url, headers=header)
print(response.status_code)
print(response.json())
'''    