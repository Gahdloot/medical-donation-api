#third party endpoint tester
import requests

url= 'https://sandbox.myidentitypass.com/api/v2/biometrics/merchant/data/verification/bvn_validation'

parameter = {
    'number': 22485750837
}

headers = {
    'Accepts': 'application/json',
    'x-api-key': 'test_ucc8c5fyl6rl78idn3lqjp:ogINip3R6hrzzARkTI42vv13ybY',
    'app-id': 'e9265dad-9424-420c-8290-e0b19a7944d7'
}

response = requests.post(url, params=parameter, headers=headers)

print(response.json())