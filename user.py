#coding:utf-8
import socket
s=socket.socket()
s.connect(('175.178.64.55',5003))
p=s.recv(1024)
print('当前在线: %s 人(来源服务器实时连接数)'%p.decode())
while True:
    name=input('为你自己取一个名字:')
while True:
    message=input('MESSAGE:')
    if message != '':
        s.send(str({name:message}).encode())
    g=s.recv(4096)
    ss=g.decode().split(',')
    ss.pop()
    for i in ss:
        ff=eval(i.replace('\'','\"'))
        for j in ff.items():
            print('用户 ',j[0],'：',j[1])

