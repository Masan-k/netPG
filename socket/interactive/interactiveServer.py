import socket
import time

M_SIZE = 1024

HOST = '127.0.0.1'
PORT = 8890

LOCADDR = (HOST, PORT)

sock = socket.socket(socket.AF_INET, type=socket.SOCK_DGRAM)
sock.bind(LOCADDR)

while True:
    try :
        print('Waiting message')
        message, cli_addr = sock.recvfrom(M_SIZE)
        message = message.decode(encoding='utf-8')
        print(f'Received message is [{message}]')

        #time.sleep(1) Clientが受信待ちになるまで待つため...無くても正常に動く

        print('Send response to Client')
        sock.sendto('Success to receive message'.encode(encoding='utf-8'), cli_addr)

    except KeyboardInterrupt:
        print ('\n closing socket \n')
        sock.close()
        break
