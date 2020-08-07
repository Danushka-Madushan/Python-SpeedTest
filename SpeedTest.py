import re
import json
import urllib
import msvcrt as x
import speedtest
import sys
import time
import os as O
from sys import exit


Banner = '''>> Internet Speed Test | Powerd By Ookla | 

>> 1) RUN INTERNET SPEEDTEST

>> 2) Download Speed

>> 3) Upload Speed 

>> 4) Ping 

>> 5) IP Details

>> 6) Exit

>> Enter Your Choice >>  '''

def test():
    s = speedtest.Speedtest()
    s.get_servers()
    s.get_best_server()
    s.download()
    s.upload()
    res = s.results.dict()
    return res["download"], res["upload"], res["ping"]

def print_s(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)
    
def Connect(host='https://www.google.com'):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False

def _input(message,in_type=str):
    while True:
        try:
            return in_type(input(message))
        except:
            pass

Number = 0
Channel = 1

print_s(">> Establishing Connection To Speedtest Server")
time.sleep(0.4)
print_s(".")
time.sleep(0.4)
print_s(".")
time.sleep(0.4)
print_s(".\n")
time.sleep(0.4)
try:

    if Connect():
        print_s(">> Connected!..\n>> Proseeding...")
        O.system("cls") 
    else:
        print_s(">> Connection Faild!..\n>> Please Check Your Connection & Try Again..\n>> Client Exiting...")
        exit()
except Exception as IdentiFier:
    exit()   

while (Channel == int(1)):
    try:

        option = int(input(Banner))
        if option not in (1,2,3,4,5,6,):
            print_s(">> Not a Valid Option!..")
            O.system("cls")  

        if option == 1: 

            for i in range(1):
                print_s("\n>> Running Speedtest...\n")
                d, u, p = test()
                print_s(">> Test Complete!..\n \n")
                print('>> Download Speed: {:.2f} Mbp/s'.format(d / 1024000))
                print('>> Upload Speed: {:.2f} Mbp/s'.format(u / 1024000))
                print('>> Ping: {} ms\n \n'.format(p))
                print_s(">> Enter [1] For Main Menu\n")
                print_s(">> Enter Any Number For Exit..")
                if __name__ == '__main__':
                    Channel = _input(">> ", int)
                O.system("cls")


        if option == 2:
            print_s("\n>> Running Speedtest...\n")
            d, u, p = test()
            print_s(">> Test Complete!..\n \n")
            print('>> Download Speed: {:.2f} Mbp/s\n \n'.format(d / 1024000))
            print_s(">> Enter [1] For Main Menu\n")
            print_s(">> Enter Any Number For Exit..")
            if __name__ == '__main__':
                    Channel = _input(">> ", int)
            O.system("cls")

        if option == 3:
            print_s("\n>> Running Speedtest...\n")
            d, u, p = test()
            print_s(">> Test Complete!..\n \n")
            print('>> Upload Speed: {:.2f} Mbp/s\n \n'.format(u / 1024000))
            print_s(">> Enter [1] For Main Menu\n")
            print_s(">> Enter Any Number For Exit..")
            if __name__ == '__main__':
                    Channel = _input(">> ", int)
            O.system("CLS")
    
        if option == 4:
            print_s("\n>> Running Speedtest...\n")
            d, u, p = test()
            print_s(">> Test Complete!..\n \n")
            print('>> Ping: {} ms\n \n'.format(p))
            print_s(">> Enter [1] For Main Menu\n")
            print_s(">> Enter Any Number For Exit..")
            if __name__ == '__main__':
                    Channel = _input(">> ", int)
            O.system("CLS")
    
        if option == 5:
            print_s("\n>> Running IP Test...\n")
            url = 'http://ipinfo.io/json'
            response = urllib.request.urlopen(url)
            data = json.load(response)
            IP=data['ip']
            org=data['org']
            city = data['city']
            country=data['country']
            region=data['region']
            print_s(">> Test Complete!..\n\n")
            print_s(">> IP Adress : " + IP + "\n")
            print_s(">> Country   : " + country + "\n" )
            print_s(">> Province  : " + region + "\n")
            print_s(">> City      : " + city + "\n")
            print_s(">> ISP/AS    : " + org + "\n\n")
            print_s(">> Enter [1] For Main Menu\n")
            print_s(">> Enter Any Number For Exit..")
            if __name__ == '__main__':
                    Channel = _input(">> ", int)
            O.system("CLS")

        if option == 6:
            print_s(">> Client Exiting...")
            break

    except Exception as IdentiFier:
        print_s(">> Not a Valid Option!..")
        O.system("cls")
        continue
else:
    exit()
