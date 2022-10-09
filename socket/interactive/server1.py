import socket
import time
import threading
import pygame
import pygame.locals
import sys
import queue 
M_SIZE = 1024

HOST = '127.0.0.1'
PORT1 = 8890
PORT2 = 8891
FROM_ADDRESS = (HOST, PORT1)
TO_ADDRESS = (HOST, PORT2)

sock = socket.socket(socket.AF_INET, type=socket.SOCK_DGRAM)
sock.bind(FROM_ADDRESS)

q = queue.Queue()
receiveMessage = "none"
def receive():
  while True:
    receiveMessage, cli_addr = sock.recvfrom(M_SIZE)
    receiveMessage = receiveMessage.decode(encoding='utf-8')
    q.put(receiveMessage)

def sendMessage(inputMessage):
  send_len = sock.sendto(inputMessage.encode('utf-8'), TO_ADDRESS)
  rx_message, addr = sock.recvfrom(M_SIZE)

pygame.init()
mainInfoFont = pygame.font.SysFont("ubuntu",15)
screen = pygame.display.set_mode([300,300])
pygame.display.set_caption("interactive")

t_receive = threading.Thread(target=receive)
t_receive.start()

inputKey = ""

while True:
  pygame.display.update()
  screen.fill((0,0,0))

  while not q.empty():
    receiveMessage = q.get()

  for event in pygame.event.get():
    if event.type == pygame.locals.KEYDOWN: 
      inputKey = pygame.key.name(event.key) 
      t_sendMessage = threading.Thread(target=sendMessage, args=(inputKey,))
      t_sendMessage.start() 
      if event.key == pygame.locals.K_ESCAPE:
        pygame.quit()
        sys.exit()
  screen.blit(mainInfoFont.render('server1 inputKey >> ' + inputKey, True, (255, 255, 255)), [10,10]) 
  screen.blit(mainInfoFont.render('received message  >> ' + receiveMessage, True, (255, 255, 255)), [10,30]) 

