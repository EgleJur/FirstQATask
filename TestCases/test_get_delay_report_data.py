import requests
import json
import jsonpath
import pytest
lpar = 'RS21'
# API_URL =f"http://rs28.rocketsoftware.com:8803/gpm/rmfm3.xml?report=DELAY&resource=,{lpar},MVS_IMAGE"
# API_URL ="http://rs28.rocketsoftware.com:8803/gpm/rmfm3.xml?report=DELAY&resource=,RS21,MVS_IMAGE&TIME=20250304035410"
headerData={'Accept': 'application/json'}
def get_url(lpar):
    return f"http://rs28.rocketsoftware.com:8803/gpm/rmfm3.xml?report=DELAY&resource=,{lpar},MVS_IMAGE"
def test_get_delay_data():
    API_URL = get_url(lpar)
    response = requests.get(API_URL,headers=headerData)
    print(response.text)

def test_get_delay_data_percent_RS21():
    API_URL = get_url(lpar)
    response = requests.get(API_URL,headers=headerData)
    delay = jsonpath.jsonpath(response.json(), 'report[0].row[0].col[5]')
    print(delay[0])

def test_get_delay_data_status_code_RS21():
    API_URL = get_url(lpar)
    response = requests.get(API_URL)
    assert response.status_code == 200

def test_get_delay_data_percent_RS22():
    lpar = 'RS22'
    API_URL = get_url(lpar)
    response = requests.get(API_URL,headers=headerData)
    delay = jsonpath.jsonpath(response.json(), 'report[0].row[0].col[5]')
    print(delay[0])

def test_get_delay_data_status_code_RS22():
    lpar = 'RS22'
    API_URL = get_url(lpar)
    response = requests.get(API_URL)
    assert response.status_code == 200