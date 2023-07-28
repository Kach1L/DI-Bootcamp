from urllib.request import urlopen
from time import time

website = urlopen('https://www.dc.com')
open_time = time()
output = website.read()
close_time = time()
website.close()
print(f'The loading time of website is',round(close_time - open_time,3),'seconds')