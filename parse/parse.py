# -*- coding: UTF-8 -*-

import sys

kural = sys.argv[1]

text = open(kural,'r').read().decode('utf8')
#text = [line.strip() for line in open(kural)]
#text_unicode = unicode(text, 'utf-8')
#print text

#list = test.decode("utf-8").split('.')

#print list(text)
#print text.split('.')

for character in text:
	print character
