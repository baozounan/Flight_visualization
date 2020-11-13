import socket
def udp_send_message():
    #创建一个udp套接字
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #可以使用套接字收发数据
    udp_socket.sendto(b"ahahaa",("127.0.0.1",7080))
    #关闭套接字
    udp_socket.close()