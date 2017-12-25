from bittrex.bittrex import *

import json


# load configuration data
with open('config.json') as json_data_file:
    data = json.load(json_data_file)


my_bittrex = Bittrex(data['bittrex']['api_key'], data['bittrex']['secret'])  #note that the version isn't specified.. TODO find out how to get version, and not get a float conversion error (probably have to edit code)

print(my_bittrex.get_balance('BTC'))

def buyShill(shill):
    print(my_bittrex.get_market_history(shill))

buyShill('BTC-ETH')