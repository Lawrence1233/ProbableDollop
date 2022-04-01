#coding:utf-8
import socket,time,json
import threading
ip=[]
td=0#线程数量
s = socket.socket()
s.bind(('0.0.0.0', 5000))
s.setblocking(False)


def new_connect():
    global ip
    try:
        s.listen(128)
        c,addr=s.accept()
        ip.append(c)
        print(addr,'connect')
        print(len(ip))
    except:
        pass

def forward(msg):
    global ip

    for j in ip:
        th_forward(j,msg)
    return

def th_forward(ip,message):
    try:
        ip.send(message.encode())

    except:
        import traceback
        traceback.print_exc()
        return



def recv():
    global ip,td
    if td > len(ip):
        return
    for i in ip:
        td+=1
        th=threading.Thread(target=recv_th,args=(i,))
        th.start()
    return


def recv_th(ip2):
    global s
    global ip,td

    try:

        ip2.setblocking(True)
        msg=ip2.recv(1024).decode()

        forward(msg)


        ip2.setblocking(False)



    except Exception as ERR:
        if ip2 in ip:
            ip.remove(ip2)

        import traceback
        traceback.print_exc()
        td -= 1
        return
    td -= 1
    return
stime=time.time()
while True:
    new_connect()
    recv()
    if time.time()-stime > 3:
        print('实时在线：',len(ip))
        stime=time.time()
