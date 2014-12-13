#!/usr/bin/env python
# -*- coding: utf-8 -*-


##
# Get commercial somoni to main  exchange rates from kkb.tj
##

from lxml import html
import requests

URL = 'http://www.kkb.tj/ru/page/RatesExchanges'
NAME_MAPPING = {
    u'Доллар США': 'USD',
    u'Евро': 'EUR',
    u'Российский рубль': 'RUR',
    u'Казахстанский тенге': 'KAZ',
}

def _getKKBPage(params):
    return requests.post(URL, data=params).text

def _parsePage(text):
    results = dict()

    tree = html.fromstring(text)
    rows = tree.xpath('//div[@class="div_text"]//table[@class="tbl_text"]/tbody[2]/tr')

    for row in rows:
        cells = row.xpath('td/text()')

        if len(cells)==4:
            cur_count = int(cells[0])
            cur_name = cells[1]
            cur_sell = float(cells[2])
            cur_buy = float(cells[3])

            if cur_name in NAME_MAPPING.keys():
                cur_code = NAME_MAPPING[cur_name]
                results[cur_code] = round(cur_sell/cur_count, 3)

    return results

def getRates(day, month, year):
    params = dict(
        day=day,
        month=month,
        year=year
    )
    return _parsePage(_getKKBPage(params))
