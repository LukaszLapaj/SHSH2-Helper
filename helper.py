import os
import platform
import urllib.request

# Device information
ECID = ''
MODEL = ''
BOARDCONFIG = ''
bloobsPerVersion = 3

if platform.system() == 'Windows':
    html = urllib.request.urlopen('https://api.ipsw.me/v2.1/' + MODEL + '/latest/version')
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
