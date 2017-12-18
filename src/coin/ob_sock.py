import gdax, time

import numpy as np
import matplotlib as plt
# class myWebsocketClient(gdax.WebsocketClient):
#     def on_open(self):
#         self.url = "wss://ws-feed.gdax.com/"
#         self.products = ["LTC-USD"]
#         self.message_count = 0
#         print("Lets count the messages!")
#     def on_message(self, msg):
#         self.message_count += 1
#         print(msg)
#         # if 'price' in msg and 'type' in msg:
#         #     print ("Message type:", msg["type"],
#         #            "\t@ {:.3f}".format(float(msg["price"])))
#     def on_close(self):
#         print("-- Goodbye! --")
#
# wsClient = myWebsocketClient()
# wsClient.start()
# print(wsClient.url, wsClient.products)
# while (wsClient.message_count < 10):
#     print ("\nmessage_count =", "{} \n".format(wsClient.message_count))
#     time.sleep(1)
# wsClient.close()

order_book = gdax.OrderBook(product_id='BTC-USD')
order_book.start()

time.sleep(4)

cur_book = order_book.get_current_book()
book = np.array(cur_book).astype()
print(book)


order_book.close()
