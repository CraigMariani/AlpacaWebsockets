from websocket import create_connection
import simplejson as json
from secret import Secret
import pprint

uri = 'wss://stream.data.alpaca.markets/v1beta1/crypto?exchanges=CBSE'
ws = create_connection(uri)

auth_message = {"action":"auth","key": Secret.key, "secret": Secret.secret_key}
ws.send(json.dumps(auth_message))

# subscription = {"action":"subscribe","trades":["BTCUSD"],"quotes":["LTCUSD","ETHUSD"],"bars":["BCHUSD"]}
subscription = {"action":"subscribe","trades":["BTCUSD"]}
ws.send(json.dumps(subscription))
while True:
    data = json.loads(ws.recv())
    pprint.pprint(data[0])
    print('****************************')
    exit