# -*- coding: utf-8 -*-

import codecs
from nose.tools import *

import currency_rates

def test_parsePage():
	with codecs.open('test/resources/page.html', encoding='utf-8') as f:
		page_content = f.read()

	rates = currency_rates._parsePage(page_content)
	assert rates!=None

	eq_(rates['USD'], 5.4)
	eq_(rates['EUR'], 6.5)
	eq_(rates['RUR'], 0.092)
	eq_(rates['KAZ'], 0.026)
