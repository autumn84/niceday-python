import json
import io

f = io.open("Settings.json", encoding='utf-8')
setting = json.load(f)
api_key = setting['APIKey']
api_secret = setting['SecretKey']
f.close()

from binance.client import Client
client = Client(api_key, api_secret)

# get market depth
depth = client.get_order_book(symbol='LRCETH')
print(depth)
