#encoding=utf-8

import socket

class my_class(object):
    pass

def service_client(new_socket):
    """为客户端返回数据"""

    # 1. 接受浏览器发送过来的请求
    request = new_socket.recv(1024)
    print(request)

    # 2. 返回http格式的数据，给浏览器
    # 2.1 准备发送给浏览器的数据---header
    response = "HTTP/1.1 200 OK\r\n"
    response += "\r\n "
    # 2.2 准备发送给浏览器的数据---body
    new_socket.send()


def main():
    """用来创建完整的http控制"""
    # 1. 创建套接字
    tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    # 2. 绑定
    tcp_socket.bind(("",8080))

    # 3. 设置为监听套接字
    tcp_socket.listen(128)
    
    # 4. 等待新客户端的链接
    new_socket,client_addr = tcp_socket.accept()


    # 5. 为客户端服务
    service_client(new_socket)





if __name__ == "__main__":
    main()