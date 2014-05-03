import mechanize
import html2text
import nltk
import cookielib
from urllib import urlopen
import sys
import time

# Browser
br = mechanize.Browser()

# Cookie Jar
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)

# Browser options
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

# Follows refresh 0 but not hangs on refresh > 0
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

# Want debugging messages?
#br.set_debug_http(True)
#br.set_debug_redirects(True)
#br.set_debug_responses(True)

# User-Agent (this is cheating, ok?)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]


br.open('http://tamilvu.org/slet/l2100/l2100sec.jsp?&book_id=31&head_id=26&auth_id=29:31:30:32:33:34:35:')


def get_kural(no):
	r=br.open('http://tamilvu.org/slet/l2100/l2100uri.jsp?song_no=' + str(no))
	html = r.read()

	raw = nltk.clean_html(html)  

	
	filename = str(no)+ '.txt'
        open(filename, 'wb').write(raw)
	br.close()

start_kural = int(sys.argv[1])

success = False
attempts = 0

while not success and attempts < 10:
	try:
		for i in range(start_kural,1331):
			get_kural(i)
			print "scrapping Kural No : " + str(i)
			time.sleep(10)	
			success = True
	except:
			i = i+1

if not success:
	raise functionCallFailedError


