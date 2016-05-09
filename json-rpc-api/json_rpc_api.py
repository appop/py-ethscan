
# API Wrapper
# Naming convention follows the geth JSON RPC api

import requests
import json

class api:

    url = ""
    headers = {'content-type': 'application/json'}

    def __init__(self, url="http://localhost", port="8545"):
        self.url = url + ":" + port


    def apiCall(self, method, params=[]):
        # type: (object, object) -> object
        payload = dict(jsonrpc="2.0", method=method, params=params, id=1) # we are making synchronous calls, so id can be any value

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

    def eth_getBalance (self, address, default_block="latest"):

        return self.apiCall(
            "eth_getBalance",
            [address, default_block]
        )
        
    def eth_getStorageAt(self, data, quantity, default_block="latest"):

        return self.apiCall(
            "eth_getStorageAt",
            [data, quantity, default_block]
        )
    
    def eth_getTransactionCount(self, data, default_block="latest"):

        return self.apiCall(
            "eth_getTransactionCount",
            [data, default_block]
        )

    def eth_getBlockTransactionCountByHash(self, hash):

        return self.apiCall(
            "eth_getBlockTransactionCountByHash",
            [hash]
        )

    def eth_getBlockTransactionCountByNumber(self, blocknumber):

        return self.apiCall(
            "eth_getBlockTransactionCountByNumber",
            [blocknumber]
        )

    def eth_getUncleCountByBlockHash(self, hash):

        return self.apiCall(
            "eth_getUncleCountByBlockHash",
            [hash]
        )

    def eth_getUncleCountByBlockNumber(self, blocknumber):

        return self.apiCall(
            "eth_getUncleCountByBlockNumber",
            [blocknumber]
        )

    def eth_getCode(self, data, default_block="latest"):

        return self.apiCall(
            "eth_getCode",
            [data, default_block]
        )

    def eth_sign(self, address, data):

        return self.apiCall(
            "eth_sign",
            [address, data]
        )

    def eth_sendTransaction(self, from_address, to_address, gas, gasPrice, value, data):

        return self.apiCall(
            "eth_sendTransaction",
            [{
                "from": from_address,
                "to": to_address,
                "gas": gas,
                "gasPrice": gasPrice,
                "value": value,
                "data": data
            }]
        )

    def eth_sendRawTransaction(self, rawData): 

        return self.apiCall(
            "eth_sendRawTransaction",
            [rawData]
        )

    def eth_call(self, from_address, to_address, gas, gasPrice, value, data, default_block):

        return self.apiCall(
            "eth_call",
            [{
                "from": from_address,
                "to": to_address,
                "gas": gas,
                "gasPrice": gasPrice,
                "value": value,
                "data": data
            }, default_block]
        )

    def eth_estimateGas(self, from_address, to_address, gas, gasPrice, value, data, default_block):

        return self.apiCall(
            "eth_estimateGas",
            [{
                "from": from_address,
                "to": to_address,
                "gas": gas,
                "gasPrice": gasPrice,
                "value": value,
                "data": data
            }, default_block]
        )

    def eth_getBlockByHash(self, hash, full=True):

        return self.apiCall(
            "eth_getBlockByHash",
            [hash, full]
        )

    def eth_getBlockByNumber(self, blocknumber, full=True):

        return self.apiCall(
            "eth_getBlockByNumber",
            [blocknumber, full]
        )

    def eth_getTransactionByHash(self, hash):

        return self.apiCall(
            "eth_getTransactionByHash",
            [hash]
        )

    def eth_getTransactionByBlockHashAndIndex(self, hash, index):

        return self.apiCall(
            "eth_getTransactionByBlockHashAndIndex",
            [hash, index]
        )

    def eth_getTransactionByBlockNumberAndIndex(self, blocknumber, index):

        return self.apiCall(
            "eth_getTransactionByBlockNumberAndIndex",
            [blocknumber, index]
        )

    def eth_getTransactionReceipt(self, hash):

        return self.apiCall(
            "eth_getTransactionReceipt",
            [hash]
        )

    def eth_getUncleByBlockHashAndIndex(self, hash, index):

        return self.apiCall(
            "eth_getUncleByBlockHashAndIndex",
            [hash, index]
        )

    def eth_getUncleByBlockNumberAndIndex(self): 

        return self.apiCall(
            "eth_getUncleByBlockNumberAndIndex",
            ["0x29c", "0x0"]
        )

    def eth_getCompilers(self): 

        return self.apiCall(
            "eth_getCompilers" 
        )

    def eth_compileSolidity(self, solidityCode):

        return self.apiCall(
            "eth_compileSolidity",
            [solidityCode]
        )

    def eth_compileLLL(self, lllCode):

        return self.apiCall(
            "eth_compileLLL",
            [lllCode]
        )

    def eth_compileSerpent(self, serpentCode):

        return self.apiCall(
            "eth_compileSerpent",
            [serpentCode]
        )

    def eth_newFilter(self, address, topics, fromBlock="latest", toBlock="latest"):

        return self.apiCall(
            "eth_newFilter",
            [{
                "fromBlock": fromBlock,
                "toBlock": toBlock,
                "address": address,
                "topics": topics
            }]
        )

    def eth_newBlockFilter(self):

        return self.apiCall(
            "eth_newBlockFilter" 
        )

    def eth_newPendingTransactionFilter(self): 

        return self.apiCall(
            "eth_newPendingTransactionFilter" 
        )

    def eth_uninstallFilter(self, filterId):

        return self.apiCall(
            "eth_uninstallFilter",
            [filterId]
        )

    def eth_getFilterChanges(self, filterId):

        return self.apiCall(
            "eth_getFilterChanges" ,
            [filterId]
        )

    def eth_getFilterLogs(self, filterId):

        return self.apiCall(
            "eth_getFilterLogs",
            [filterId]
        )

    def eth_getLogs(self, filter):

        return self.apiCall(
            "eth_getLogs",
            [filter]
        )

    def eth_getWork(self): 

        return self.apiCall(
            "eth_getWork" 
        )

    def eth_submitWork(self, nonce, pow_hash, mix_digest):

        return self.apiCall(
            "eth_submitWork",
            [nonce, pow_hash, mix_digest]
        )

    def eth_submitHashrate(self, hashrate, id):

        return self.apiCall(
            "eth_submitHashrate",
            [hashrate, id]
        )

    def db_putString(self, database, key, string):

        return self.apiCall(
            "db_putString",
            [database, key, string]
        )

    def db_getString(self, database, key):

        return self.apiCall(
            "db_getString",
            [database, key]
        )

    def db_putHex(self, database, key, hex):

        return self.apiCall(
            "db_putHex",
            [database, key, hex]
        )

    def db_getHex(self, database, key):

        return self.apiCall(
            "db_getHex",
            [database, key]
        )

    def shh_version(self): 

        return self.apiCall(
            "shh_version" 
        )

    def shh_post(self, from_address, to_address, topics, payload, priority, ttl):

        return self.apiCall(
            "shh_post",
            [{
                "from_address": from_address,
                "to_address": to_address,
                "topics": topics,
                "payload": payload,
                "priority": priority,
                "ttl": ttl
        }]
        )

    def shh_newIdentity(self): 

        return self.apiCall(
            "shh_newIdentity" 
        )

    def shh_hasIdentity(self, address):

        return self.apiCall(
            "shh_hasIdentity",
            [address]
        )

    def shh_newFilter(self, topics, to_address):

        return self.apiCall(
            "shh_newFilter",
            [{
                "topics": topics,
                "to": to_address
            }]
        )

    def shh_uninstallFilter(self, filterId):

        return self.apiCall(
            "shh_uninstallFilter",
            [filterId]
        )

    def shh_getFilterChanges(self, filterId):

        return self.apiCall(
            "shh_getFilterChanges",
            [filterId]
        )

    def shh_getMessages(self, filterId):

        return self.apiCall(
            "shh_getMessages",
            [filterId]
        )
