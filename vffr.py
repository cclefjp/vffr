''' vffr.py - FTXのFunding Rateを視覚化する '''

# from vffr internal
from unixtime import currentunixtime, aweekunixtime
from unixtime import agounixtime
from getfr import getfr
from listfutures import listfutures

# from python standard library
from time import sleep

# from external libraries

import numpy as np
import matplotlib.pyplot as plt



try:

    futures = listfutures()
    print(futures)

    # tstart = aweekunixtime()
    # tstart = agounixtime(hours=24)
    tstart = agounixtime(days=30)
    tend = currentunixtime()
    # tend = agounixtime(hours=15)

    # 結果格納
    rearranged = {}

    for future in futures:
        print(future, 'のfunding rate履歴を取得しています。')
        rawdict = getfr(tstart, tend, future)
        resultarr = rawdict['result']


        for elem in resultarr:
            name = elem['future']
            rate = elem['rate']
            time = elem['time']

            if not name in rearranged:
                rearranged[name] = { 'rates': [], 'times': [] }
        
            rearranged[name]['rates'].append(rate)
            rearranged[name]['times'].append(time)
        
        sleep(0.3)

    xdat = rearranged['BTC-PERP']['times']
    xdat = xdat[::-1] # 新しい順に並んでいるので逆順にする
    print('取得できた最古のタイムスタンプ:', xdat[0])
    count = len(xdat)
    x = np.asarray(xdat)

    bundle = 10
    i = 0
    for future in futures:
        ydat = rearranged[future]['rates']
        if(len(ydat) == count):
            y = np.asarray(ydat)
            y = y[::-1] # 新しい順に並んでいるので逆順にする
            plt.plot(x, y, label=future)
        i += 1
        if i % bundle == 0:
            plt.legend()
            plt.show()
    # print(rearranged)

except:
    import traceback
    traceback.print_exc()