import json
try:
    # For python3
    import urllib.error
    import urllib.parse
    import urllib.request
except:
    # For python2
    import imp
    import urllib2
    import urlparse
    urllib = imp.new_module('urllib')
    urllib.error = urllib2
    urllib.parse = urlparse
    urllib.request = urllib2
try:
    url = "https://raw.githubusercontent.com/PixelStarext-Devices/monthly_updates_ota/14/devices.json
    response = urllib.request.urlopen(url, timeout=10)
    data = json.loads(response.read())
    for res in data:
        for version in res['supported_versions']:
            if version['version_code'] == '14':
                print (res['codename'])
                break
except:
    print ("")
