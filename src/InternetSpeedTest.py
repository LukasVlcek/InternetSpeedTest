#!/usr/bin/env python

import os
import sys
from datetime import datetime

def main():
    try:
        speedTestResults = doSpeedTest()
        print speedTestResults

    except Exception as e:
        print 'Error: %s' % e
        sys.exit(1)

    sys.exit()

def doSpeedTest():
    result = os.popen("/usr/local/bin/speedtest-cli --simple").read()
    if 'Cannot' in result:
        return {'date': datetime.now(), 'upload': 0, 'download': 0, 'ping': 0}

    resultSet = result.split('\n')
    pingResult = resultSet[0]
    downloadResult = resultSet[1]
    uploadResult = resultSet[2]

    pingResult = float(pingResult.replace('Ping: ', '').replace(' ms', ''))
    downloadResult = float(downloadResult.replace('Download: ', '').replace(' Mbit/s', ''))
    uploadResult = float(uploadResult.replace('Upload: ', '').replace(' Mbit/s', ''))

    return {'date': datetime.now().strftime("%d. %m. %Y, %H:%M:%S"), 'upload': uploadResult, 'download': downloadResult, 'ping': pingResult}

if __name__ == '__main__':
    main();
