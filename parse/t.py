import os
from os.path import basename
for root, dirs, files in os.walk("../kurals"):
    for filename in files:
        if filename.endswith(".txt"):
#	    print filename
            base =  os.path.basename(filename)
	    print os.path.splitext(base)[0]
