import socket

M_SIZE = 1024
SERV_ADDRESS = ('127.0.0.1', 8890)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    try:
        print('Input any messages, Type [end] to exit')
        message = input()
        if message != 'end':
            send_len = sock.sendto(message.encode('utf-8'), SERV_ADDRESS)
            print("send_len >> " + str(send_len))

            print('Waiting response from Server')
            rx_message, addr = sock.recvfrom(M_SIZE)
            print("[Server]: " + rx_message.decode(encoding='utf-8'))

        else:
            print('closing socket')
            sock.close()
            break

    except KeyboardInterrupt:
        print('closing socket')
        sock.close()
        break
