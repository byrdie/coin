import gdax, time

import numpy as np
import matplotlib.pyplot as plt


public_client = gdax.PublicClient()

book = public_client.get_product_order_book('BTC-USD', level=2)


bids = np.array(book['bids'])
asks = np.array(book['asks'])

bids = bids[:,0:2].astype(np.float)
asks = asks[:,0:2].astype(np.float)
# bids[:,2] = bids[:,2].astype(np.float)

b_x = bids[:,0]
b_y = bids[:,1]
bcum = np.cumsum(b_y)

a_x = asks[:,0]
a_y = asks[:,1]
acum = np.cumsum(a_y)


plt.plot(b_x, bcum, a_x, acum, ls='steps')
plt.show()