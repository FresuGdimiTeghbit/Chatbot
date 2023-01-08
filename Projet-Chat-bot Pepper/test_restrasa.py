import urllib.request as urllib2
import json
import random
import time

url = 'http://10.104.21.120:5002/webhooks/rest/webhook/'
text = "hello"

data = '{"sender":"nao", "message":"' + text + '"}'
data_encode=data.encode("utf-8")
req = urllib2.Request(url, data=data_encode)
f = urllib2.urlopen(req)
class Response:
    pass
response = Response()
response.code = f.getcode()
response.body = f.read()
print(response.body)
r = json.loads(response.body)
if (r):
	r = r[0]['text'].encode("UTF-8")
print(r)
