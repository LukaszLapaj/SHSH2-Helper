import os
import platform
import urllib.request

# Device information
ECID = ''
MODEL = ''
BOARDCONFIG = ''
bloobsPerVersion = 3

if platform.system() == 'Windows':
    url = 'https://api.ipsw.me/v2.1/' + MODEL + '/latest/version'
    request = urllib.request.Request(
        url,
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/78.0.3904.97 Safari/537.36 '
        }
    )

    html = urllib.request.urlopen(request)
    VERSION = html.read().decode('utf-8')

    PATH = MODEL
    if BOARDCONFIG != '':
        PATH += '_' + BOARDCONFIG
    PATH += '_' + ECID

    try:
        os.mkdir(PATH)
        os.chdir(PATH)
    except FileExistsError:
        os.chdir(PATH)

    try:
        os.mkdir(VERSION)
        os.chdir(VERSION)
    except FileExistsError:
        os.chdir(VERSION)

    for i in range(bloobsPerVersion):
        call = '..\\..\\tsschecker.exe --device ' + MODEL + ' --ecid ' + ECID + ' --save --nocache --latest'
        if BOARDCONFIG != '':
            call += ' ' + BOARDCONFIG
        os.system(call)

else:
    print("Unsupported platform")
