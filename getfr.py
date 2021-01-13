''' getfr.py - funding rateのAPIを叩いて結果を得る '''

# from standard library
import json

# from external libraries
import requests

## FTX APIのURL
BASEURL = 'https://ftx.com/api/funding_rates'

def getfr(tstart, tend, future=None):
    ''' FTX APIからFunding Rateを得る
    返り値: 得たresponseをdictに変換したもの
    '''
    t0 = int(tstart)
    t1 = int(tend)
    assert t1 > t0

    getparam = {
        'start_time': t0,
        'end_time': t1
    }
    if future is not None:
        getparam['future'] = str(future)
    
    response = requests.get(url=BASEURL, params=getparam)
    assert response.status_code == 200

    return json.loads(response.text)