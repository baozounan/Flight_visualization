import socket
def udp_send_message():
    #创建一个udp套接字
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #可以使用套接字收发数据
    while True:
        udp_socket.sendto("1000.00，30.95212121,104.3245256\n".encode("utf-8"),("127.0.0.1",7081))
    #关闭套接字
    udp_socket.close()