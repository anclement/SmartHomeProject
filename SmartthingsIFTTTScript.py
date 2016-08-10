import requests
import json
import subprocess
import time
url = 'https://maker.ifttt.com/trigger/Name/with/key/'
if __name__ == '__main__':
    while True:
    	time.sleep(5)
        p = subprocess.Popen("arp-scan -l | grep 192.168.1.98", stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        p_status = p.wait()
        if output:
            print "Yay, the device is connected to your network!"
            response = requests.put(url)
            print(response.text)
			
        
        else:
            print "The device is not present!"
