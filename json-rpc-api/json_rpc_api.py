
# API Wrapper

import requests
import json

class api:


    url = "http://localhost:8545"
    headers = {'content-type': 'application/json'}


    def apiCall(self, method, params):
        payload = dict(jsonrpc="2.0", method=method, params=params, id=1)

        response = requests.post(self.url, data=json.dumps(payload), headers=self.headers).json()


    def eth_getBalance(self, address, defaultblock="latest"):

        return self.apicall (
            "eth_getBalance",
            ["0xe46e33d279b3168f540bfe49e9df44ae1c7f982a", defaultblock]
        )

