from socket import *
import os
import sys

clientSock = socket(AF_INET, SOCK_STREAM)
def inita():
    try:
        clientSock.connect(('127.0.0.1', 8888))
        print('연결에 성공했습니다.')
        filename = 'ip.txt'
        clientSock.sendall(filename.encode('utf-8'))

        data_transferred = 0

        print("파일 %s 전송 시작" %filename)
        with open(filename, 'rb') as f:
            try:
                data = f.read(1024) #1024바이트 읽는다
                while data: #데이터가 없을 때까지
                    data_transferred += clientSock.send(data) #1024바이트 보내고 크기 저장
                    data = f.read(1024) #1024바이트 읽음
            except Exception as ex:
                print(ex)
        print("전송완료 %s, 전송량 %d" %(filename, data_transferred))
    except:
        print("연결 실패")
        return False
inita()
