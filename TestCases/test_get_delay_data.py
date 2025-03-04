import requests
import json
import jsonpath
import pytest

API_URL ="http://rs28.rocketsoftware.com:8803/gpm/perform.xml?resource=,RSPLEX01,SYSPLEX&id=8D0160"
# API_URL ="http://rs28.rocketsoftware.com:8803/gpm/perform.xml?resource=,RSPLEX01,SYSPLEX&id=8D0160&range=20250304042550,20250304042550"
headerData={'Accept': 'application/json'}
def test_get_delay_data_json():
    response = requests.get(API_URL,headers=headerData)
    print(response.text)

def test_get_delay_data_percent():
    response = requests.get(API_URL,headers=headerData)
    percent = jsonpath.jsonpath(response.json(), 'report[0].row[0].percent')
    print(percent[0])

def test_get_delay_data_status_code():
    response = requests.get(API_URL)
    assert response.status_code == 200
