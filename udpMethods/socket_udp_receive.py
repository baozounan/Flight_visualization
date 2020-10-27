# encoding:utf-8
import socket
def udp_receive_message(ip_addr,port):
    """使用udp连接方式循环接收数据，输入IP地址(字符串类型)和端口（数值类型）"""
    ip_addr_str = str(ip_addr)  # 转换成字符串类型
    # 1.创建套接字
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    # 2.绑定本地信息
    addr = (ip_addr_str,port)
    udp_socket.bind(addr)
    # 3接受数据
    while True:
        rec_data = udp_socket.recvfrom(1024)
        rec_msg = rec_data[0]
        send_addr = rec_data[1]
        # 打印收到的数据
        # print(rec_data)
        print(rec_msg)
        print(type(rec_msg))
        # print(send_addr)
        # print("%s:%s" % (str(send_addr), rec_msg.decode("gb18030")))
    # 关闭套接字
    udp_socket.close()