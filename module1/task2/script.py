import urllib
import urllib2

url = 'https://stepic.org/'
req = urllib2.Request(url)
response = urllib2.urlopen(req)
result = response.read()

match = result.find(".css")
print result[match - 50: match + 50]

