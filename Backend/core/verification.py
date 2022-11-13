import requests

# for verification, we use identitypass Api for verifying users data

class Verify:
    URL = 'https://sandbox.myidentitypass.com/api/v2/biometrics/merchant/data/verification/bvn_validation'
    HEADERS = {
    'Accepts': 'application/json',
    'x-api-key': 'test_ucc8c5fyl6rl78idn3lqjp:ogINip3R6hrzzARkTI42vv13ybY',
    'app-id': 'e9265dad-9424-420c-8290-e0b19a7944d7'
}

    def bvn_verification(**kwargs):
        response = requests.post(Verify.URL, data=kwargs, headers=Verify.HEADERS)

        if response.json()['status'] == True and response.json()["detail"]["verification"] == "VERIFIED":
            return True
        return False

