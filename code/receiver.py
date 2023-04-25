from socket import *
import os
while(True):
    serverSock = socket(AF_INET, SOCK_STREAM)
    serverSock.bind(('', 6445))
    serverSock.listen(1)
    connectionSock, addr = serverSock.accept()
    print(str(addr),'에서 접속')
    filename = connectionSock.recv(1024) #클라이언트한테 파일이름(이진 바이트 스트림 형태)을 전달 받는다
    data_transferred = 0
    nowdir = os.getcwd()
    with open(nowdir + "/../receiving_data/" + filename.decode('utf-8') + '.txt', 'wb') as f: #현재dir에 filename으로 파일을 받는다
        try:
            data = connectionSock.recv(1024) #1024바이트 읽는다
            while data: #데이터가 있을 때까지
                f.write(data) #1024바이트 쓴다
                data_transferred += len(data)
                data = connectionSock.recv(1024) #1024바이트를 받아 온다
        except Exception as ex:
            print(ex)
    print('파일 %s 받기 완료. 전송량 %d' %(filename, data_transferred))
