
# API Wrapper

import requests
import json

class api:


    url = "http://localhost:8545"
    headers = {'content-type': 'application/json'}


    def apiCall(self, method, params=[]):
        payload = dict(jsonrpc="2.0", method=method, params=params, id=1)

        response = requests.post(self.url, data=json.dumps(payload), headers=self.headers).json()

    # curl -X POST --data '{"jsonrpc":"2.0","method":"web3_clientVersion",[])

    def web3_clientVersion(self):
        
        return self.apiCall(
            "web3_clientVersion"
        )
        
    def web3_sha3 (self, hex): 

        return self.apiCall(
            "web3_sha3",
            [hex]
        )
        
    def net_version(self): 

        return self.apiCall(
            "net_version"
        )
        

    def net_listening(self): 
        
        return self.apiCall(
            "net_listening"
        )

    def net_peerCount(self): 

        return self.apiCall(
            "net_peerCount"
        )

    def eth_protocolVersion(self): 

        return self.apiCall(
            "eth_protocolVersion"
        )

    def eth_syncing(self): 

        return self.apiCall(
            "eth_syncing" 
        )

    def eth_coinbase(self): 

        return self.apiCall(
            "eth_coinbase" 
        )

    def eth_mining(self): 

        return self.apiCall(
            "eth_mining" 
        )

    def eth_hashrate(self): 

        return self.apiCall(
            "eth_hashrate" 
        )

    @property
    def eth_gasPrice(self): 

        return self.apiCall(
            "eth_gasPrice" 
        )

    @property
    def eth_accounts(self): 

        return self.apiCall(
            "eth_accounts" 
        )

    def eth_blockNumber(self): 

        return self.apiCall(
            "eth_blockNumber" 
        )

    def eth_getBalance (self, address, default_block): 

        return self.apiCall(
            "eth_getBalance",
            [address, default_block]
        )
        
    def eth_getStorageAt(self): 

        return self.apiCall(
            "eth_getStorageAt",
            ["0x407d73d8a49eeb85d32cf465507dd71d507100c1", "0x0", "0x2"]
        )
    
    def eth_getTransactionCount(self): 

        return self.apiCall(
            "eth_getTransactionCount",
            ["0x407d73d8a49eeb85d32cf465507dd71d507100c1","latest"]
        )

    def eth_getBlockTransactionCountByHash(self): 

        return self.apiCall(
            "eth_getBlockTransactionCountByHash",
            ["0xb903239f8543d04b5dc1ba6579132b143087c68db1b2168786408fcbce568238"]
        )

    def eth_getBlockTransactionCountByNumber(self): 

        return self.apiCall(
            "eth_getBlockTransactionCountByNumber",
            ["0xe8"]
        )

    def eth_getUncleCountByBlockHash(self): 

        return self.apiCall(
            "eth_getUncleCountByBlockHash",
            ["0xb903239f8543d04b5dc1ba6579132b143087c68db1b2168786408fcbce568238"]
        )

    def eth_getUncleCountByBlockNumber(self): 

        return self.apiCall(
            "eth_getUncleCountByBlockNumber",
            ["0xe8"]
        )

    def eth_getCode(self): 

        return self.apiCall(
            "eth_getCode",
            ["0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b", "0x2"]
        )

    def eth_sign(self): 

        return self.apiCall(
            "eth_sign" 

,["0xd1ade25ccd3d550a7eb532ac759cac7be09c2719", "Schoolbus"])
    def eth_sendTransaction(self): 

        return self.apiCall(
            "eth_sendTransaction",
            #[{see above}]
        )

    def eth_sendRawTransaction(self): 

        return self.apiCall(
            "eth_sendRawTransaction",
            #[{see above}]
        )

    def eth_call(self): 

        return self.apiCall(
            "eth_call",
            #[{see above}]
        )

    def eth_estimateGas(self): 

        return self.apiCall(
            "eth_estimateGas",
            #[{see above}]
        )

    def eth_getBlockByHash(self): 

        return self.apiCall(
            "eth_getBlockByHash",
            ["0xe670ec64341771606e55d6b4ca35a1a6b75ee3d5145a99d05921026d1527331", true]
        )

    def eth_getBlockByNumber(self): 

        return self.apiCall(
            "eth_getBlockByNumber",
            ["0x1b4", true]
        )

    def eth_getTransactionByHash(self): 

        return self.apiCall(
            "eth_getTransactionByHash",
            ["0xb903239f8543d04b5dc1ba6579132b143087c68db1b2168786408fcbce568238"]
        )

    def eth_getTransactionByBlockHashAndIndex(self): 

        return self.apiCall(
            "eth_getTransactionByBlockHashAndIndex",
            ["0xc6ef2fc5426d6ad6fd9e2a26abeab0aa2411b7ab17f30a99d3cb96aed1d1055b", "0x0"]
        )

    def eth_getTransactionByBlockNumberAndIndex(self): 

        return self.apiCall(
            "eth_getTransactionByBlockNumberAndIndex" 

,["0x29c", "0x0"])
    def eth_getTransactionReceipt(self): 

        return self.apiCall(
            "eth_getTransactionReceipt" 

,["0xb903239f8543d04b5dc1ba6579132b143087c68db1b2168786408fcbce568238"])
    def eth_getUncleByBlockHashAndIndex(self): 

        return self.apiCall(
            "eth_getUncleByBlockHashAndIndex" 

,["0xc6ef2fc5426d6ad6fd9e2a26abeab0aa2411b7ab17f30a99d3cb96aed1d1055b", "0x0"])
    def eth_getUncleByBlockNumberAndIndex(self): 

        return self.apiCall(
            "eth_getUncleByBlockNumberAndIndex" 

,["0x29c", "0x0"])
    def eth_getCompilers(self): 

        return self.apiCall(
            "eth_getCompilers" 
        )

,[])
    def eth_compileSolidity(self): 

        return self.apiCall(
            "eth_compileSolidity" 

,[solidityCode])
    def eth_compileLLL(self): 

        return self.apiCall(
            "eth_compileLLL" 

,["(returnlll (suicide (caller)))"])
    def eth_compileSerpent(self): 

        return self.apiCall(
            "eth_compileSerpent" 

,[serpentCode])
    def eth_newFilter(self): 

        return self.apiCall(
            "eth_newFilter" 

,[{"topics":["0x12341234"]}])
    def eth_newBlockFilter(self): 

        return self.apiCall(
            "eth_newBlockFilter" 
        )

,[])
    def eth_newPendingTransactionFilter(self): 

        return self.apiCall(
            "eth_newPendingTransactionFilter" 
        )

,[])
    def eth_uninstallFilter(self): 

        return self.apiCall(
            "eth_uninstallFilter" 

,["0xb"])
    def eth_getFilterChanges(self): 

        return self.apiCall(
            "eth_getFilterChanges" 

,["0x16"])
    def eth_getFilterLogs(self): 

        return self.apiCall(
            "eth_getFilterLogs" 

,["0x16"])
    def eth_getLogs(self): 

        return self.apiCall(
            "eth_getLogs" 

,[{"topics":["0x000000000000000000000000a94f5374fce5edbc8e2a8697c15331677e6ebf0b"]}])
    def eth_getWork(self): 

        return self.apiCall(
            "eth_getWork" 
        )

,[])
    def eth_submitWork(self): 

        return self.apiCall(
            "eth_submitWork" 

, ["0x0000000000000001", "0x1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef", "0xD1GE5700000000000000000000000000D1GE5700000000000000000000000000"])
    def eth_submitHashrate(self): 

        return self.apiCall(
            "eth_submitHashrate" 

, ["0x0000000000000000000000000000000000000000000000000000000000500000", "0x59daa26581d0acd1fce254fb7e85952f4c09d0915afd33d3886cd914bc7d283c"])
    def db_putString(self): 

        return self.apiCall(
            "db_putString" 

,["testDB","myKey","myString"])
    def db_getString(self): 

        return self.apiCall(
            "db_getString" 

,["testDB","myKey"])
    def db_putHex(self): 

        return self.apiCall(
            "db_putHex" 

,["testDB","myKey","0x68656c6c6f20776f726c64"])
    def db_getHex(self): 

        return self.apiCall(
            "db_getHex" 

,["testDB","myKey"])
    def shh_version(self): 

        return self.apiCall(
            "shh_version" 
        )

,[])
    def shh_post(self): 

        return self.apiCall(
            "shh_post" 

,[{"from":"0xc931d93e97ab07fe42d923478ba2465f2..","topics": ["0x68656c6c6f20776f726c64"],"payload":"0x68656c6c6f20776f726c64","ttl":0x64,"priority":0x64}])
    def shh_newIdentity(self): 

        return self.apiCall(
            "shh_newIdentity" 
        )

,[])
    def shh_hasIdentity(self): 

        return self.apiCall(
            "shh_hasIdentity" 

,["0x04f96a5e25610293e42a73908e93ccc8c4d4dc0edcfa9fa872f50cb214e08ebf61a03e245533f97284d442460f2998cd41858798ddfd4d661997d3940272b717b1"])
    def shh_newIdentity(self): 

        return self.apiCall(
            "shh_newIdentity" 
        )

,[])
    def shh_hasIdentity(self): 

        return self.apiCall(
            "shh_hasIdentity" 

,["0x04f96a5e25610293e42a73908e93ccc8c4d4dc0edcfa9fa872f50cb214e08ebf61a03e245533f97284d442460f2998cd41858798ddfd4d661997d3940272b717b1"])
    def shh_newFilter(self): 

        return self.apiCall(
            "shh_newFilter" 

,[{"topics": ['0x12341234bf4b564f'],"to": "0x2341234bf4b2341234bf4b564f..."}])
    def shh_uninstallFilter(self): 

        return self.apiCall(
            "shh_uninstallFilter" 

,["0x7"])
    def shh_getFilterChanges(self): 

        return self.apiCall(
            "shh_getFilterChanges" 

,["0x7"])
    def shh_getMessages(self): 

        return self.apiCall(
            "shh_getMessages" 

,["0x7"])