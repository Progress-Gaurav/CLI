# API tests can use either curl or http.client
import pytest
import http.client
import requests
import json

class APIDetails:
    def __init__(self, url):
        self.url = url

    def __eq__(self, other):
        return self.url == other.url

@pytest.fixture
def my_API():
    #url = "https://dummy-json.mock.beeceptor.com/todos" # documentation at https://beeceptor.com/docs/sample-api-for-testing/ 
    #url = "https://jsonplaceholder.typicode.com/posts/1"
    #url = "https://jsonplaceholder.typicode.com/posts/"
    return APIDetails("https://jsonplaceholder.typicode.com/posts/")
    
def test_html():
    r = requests.get("http://www.google.com")
    html_content = r.text
    assert "Google" in html_content

def test_api(my_API):
    url = my_API.url
    
    # alternatives
    #conn = http.client.HTTPConnection("openssl-library.org") 
    #conn.request("GET", "/news/vulnerabilities/index.html") # "/downloads/source")
    
    #resp = requests.get(url) #,
    #    headers = {'Content-Type':'application/x-www-form-urlencoded'},
    #    data = payload,
    #    auth = (client_id, self.client_secret)
    
    # https://www.datacamp.com/tutorial/making-http-requests-in-python 
    resp = requests.get(url)
    str_json = resp.json()

    assert "esse" in str_json[1]['title']
    
    assert resp.status_code != 301 # requests.Response.ok