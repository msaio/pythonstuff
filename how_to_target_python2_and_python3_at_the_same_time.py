## Python 3 supports this module but python 2 does not:
# import urllib.request as urllib_request

## In python 2, the similar module is:
# import urllib2 as urllib_request

## The question is: How to run this file in both python 2 and python 3 without modifying the code
## The answer:
try:
    import urllib.request as urllib_request #for python 3
except ImportError:
    import urllib2 as urllib_request # for python 2
if __name__ == "__main__":
    html = urllib_request.urlopen("http://www.google.com/")
    print(html.headers['content-type'])

