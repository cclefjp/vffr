''' listfutures.py - futureの種類を列挙する '''

# from vffr internal
from getfr import getfr
from unixtime import currentunixtime, agounixtime

def listfutures():
    ''' getfrを用いてfuturesの種類を列挙する '''
    tstart = agounixtime(days=1)
    tend = currentunixtime()

    rawdict = getfr(tstart=tstart, tend=tend)
    resultlist = rawdict['result']

    futures = set()
    for element in resultlist:
        if 'future' in element:
            futures.add(element['future'])
    return futures

