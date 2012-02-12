# coding: utf-8

import urllib2
import time
import json


search_url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&num=%(limit)s&q="%(url)s"'

def get_position_url(url, deep):
    """Try to search url in yandex (google) and return position in issuance"""
    print '=' * 80
    print url
    f = urllib2.urlopen(search_url % dict(limit=deep, url=url))
    print 'search for %s' % url

    issuance = f.read()
    if issuance:
        issuance = json.loads(issuance)
        if issuance.get('responseStatus', -1) != 200:
            print 'RESPONSE ERROR:', issuance.get('responseStatus')
            return -1
    else:
        return -1

    print 'Results len', len(issuance.get('responseData', {}).get('results', []))

    time.sleep(1.5)
    for i, dct in enumerate(issuance.get('responseData', {}).get('results', [])):
        if url in dct.get('url', ''):
            print 'Position:', i
            return i


def main():
    deep = 100
    try:
        with open('urls.dat') as f:
            for url in f:
                s_url = url.strip()
                if s_url:
                    get_position_url(s_url, deep)
    except Exception, e:
        print 'ERROR', e


if __name__ == '__main__':
    main()

