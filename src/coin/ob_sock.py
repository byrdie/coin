import gdax, time

import numpy as np
import matplotlib.pyplot as plt

plt.ion()

window = 100

order_book = gdax.OrderBook(product_id='BTC-USD')
order_book.start()

time.sleep(10)

while(True):

    cur_book = order_book.get_current_book()

    bids = np.array(cur_book['bids'])
    bids = bids[:,0:2].astype(np.float)

    asks = np.array(cur_book['asks'])
    asks = asks[:,0:2].astype(np.float)

    price = (bids[-1][0] + asks[0][0]) / 2
    print(price)

    b_x = bids[:,0]
    b_y = bids[:,1]
    b_i = np.where(b_x > (price - window))
    b_x = b_x[b_i]
    b_y = b_y[b_i]
    if b_x.shape[0] == 0:
        plt.pause(0.1)
        continue
    bcum = np.cumsum(b_y[::-1])[::-1]

    a_x = asks[:,0]
    a_y = asks[:,1]
    a_i = np.where(a_x < (price + window))
    a_x = a_x[a_i]
    a_y = a_y[a_i]
    if a_x.shape[0] == 0:
        plt.pause(0.1)
        continue
    acum = np.cumsum(a_y)

    print(b_x.shape)
    print(a_x.shape)

    plt.clf()
    plt.plot(b_x, bcum, a_x, acum, ls='steps')
    plt.pause(0.001)


order_book.close()