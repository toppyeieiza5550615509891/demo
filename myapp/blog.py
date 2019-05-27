from urllib import request as urlrequest
from urllib import request

proxy_host = '157.230.33.25:8080'    # host and port of your proxy
url = 'http://www.twitter.com'
req = urlrequest.Request(url)
req.set_proxy(proxy_host, 'http')

request.urlopen(url)
# req = urlrequest.Request(url)
# req.set_proxy(proxy_host, 'http')

# response = urlrequest.urlopen(req)
# print(response.read().decode('utf8'))