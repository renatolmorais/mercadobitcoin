#encoding: UTF-8

import sys,os
import requests
import json
from datetime import datetime
from time import time

def tsnow():
	now = time()
	return {
		'timestamp': now,
		'dateobj': datetime.fromtimestamp(now),
		'year': datetime.fromtimestamp(now).strftime('%Y'),
		'month': datetime.fromtimestamp(now).strftime('%m'),
		'day': datetime.fromtimestamp(now).strftime('%d'),
		'hour': datetime.fromtimestamp(now).strftime('%H'),
		'minute': datetime.fromtimestamp(now).strftime('%M'),
		'second': datetime.fromtimestamp(now).strftime('%S'),
		'date': datetime.fromtimestamp(now).strftime('%d/%m/%Y'),
		'strdate': datetime.fromtimestamp(now).strftime('%Y%m%d'),
		'time': datetime.fromtimestamp(now).strftime('%H:%M:%S'),
		'strtime': datetime.fromtimestamp(now).strftime('%H-%M-%S'),
		'strdatetime': datetime.fromtimestamp(now).strftime('%Y%m%d-%H-%M-%S'),
	}

def now(format=''):
	if format == '':
		return datetime.now().strftime('%Y/%m/%d, %H:%M:%S -> ')
	else:
		return datetime.now().strftime(format)

url = 'http://www.mercadobitcoin.net/api/{coin}/{method}/'

def get_ticker(coin):
	resp = requests.get(
		url.format(
			coin=coin,
			method='ticker'
		)
	)
	if resp.status_code == 200:
		return {
			'timestamp': tsnow().get('strdatetime'),
			'content': json.loads(resp.text)
		}
	else:
		return {}

if __name__ == '__main__':
	print get_ticker('BTC')
	#print now('%H:%M:%S')