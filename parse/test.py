# -*- coding: UTF-8 -*-
foo = u'Δ, Й, ק, ‎ م, ๗, あ, 叶, 葉, and 말.'
f = open('test', 'w')
f.write(foo.encode('utf8'))
f.close()

f = open('test', 'r')
print f.read().decode('utf8')
