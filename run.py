# stop windows services that we dont like lol
#
import win32serviceutil
import win32service

import os
import time
import json


with open('config.json') as f:
    data = json.load(f)
    SERVICES = data['SERVICES']

def start(service):
    win32serviceutil.StartService(service.get('name'))

    
def stop(service):
    win32serviceutil.StopService(service.get('name'))

# every 5 seconds stop the services

EXIT = False

def main():
    while EXIT == False:
        time.sleep(5)
        os.system('cls')
        run()
        # get keyboard interupt
        

def run():
    try:
        for service in SERVICES:
            # create a switch case for each service
            if service.get('action') == 'start':
                start(service)
            else:
                stop(service)
    except:
        pass
    finally:
        for service in SERVICES:
            # Print the status of each service
            status = win32serviceutil.QueryServiceStatus(service.get('name'))[1]
            if status == 4:
                status = 'Running'
            else:
                status = 'Stopped'
            print(service.get('display_name') + ": " + status)

if __name__ == '__main__':
    main()