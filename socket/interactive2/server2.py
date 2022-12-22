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
FROM_ADDRESS = (HOST, PORT2) #diff
TO_ADDRESS = (HOST,PORT1)    #diff

sock = socket.socket(socket.AF_INET, type=socket.SOCK_DGRAM)
sock.bind(FROM_ADDRESS)

q = queue.Queue()
receiveMessage = "none"

s1Pos = [100,100]
s2Pos = [200,200]

def receive():
  while True:
    receiveMessage, cli_addr = sock.recvfrom(M_SIZE)
    receiveMessage = receiveMessage.decode(encoding='utf-8')
    q.put(receiveMessage)

def sendMessage(inputMessage):
  send_len = sock.sendto(inputMessage.encode('utf-8'), TO_ADDRESS)
  #rx_message, addr = sock.recvfrom(M_SIZE)

pygame.init()
mainInfoFont = pygame.font.SysFont("ubuntu",15)
screen = pygame.display.set_mode([300,300])
pygame.display.set_caption("interactive")

t_receive = threading.Thread(target=receive)
t_receive.setDaemon(True)
t_receive.start()

inputKey = ""
MOVE = 5

while True:
  pygame.display.update()
  screen.fill((0,0,0))

  while not q.empty():
    receiveMessage = q.get()
    if receiveMessage == 'k':
      s2Pos[1] = s2Pos[1] - MOVE 
    if receiveMessage == 'j':
      s2Pos[1] = s2Pos[1] + MOVE 
    if receiveMessage == 'h':
      s2Pos[0] = s2Pos[0] - MOVE 
    if receiveMessage == 'l':
      s2Pos[0] = s2Pos[0] + MOVE 


  for event in pygame.event.get():
    if event.type == pygame.locals.KEYDOWN: 
      if event.key == pygame.locals.K_ESCAPE:
        pygame.quit()
        sys.exit()
      else:
        inputKey = pygame.key.name(event.key) 
        if inputKey == 'k':
          s1Pos[1] = s1Pos[1] - MOVE 
        if inputKey == 'j':
          s1Pos[1] = s1Pos[1] + MOVE 
        if inputKey == 'h':
          s1Pos[0] = s1Pos[0] - MOVE 
        if inputKey == 'l':
          s1Pos[0] = s1Pos[0] + MOVE 

        t_sendMessage = threading.Thread(target=sendMessage, args=(inputKey,))
        t_sendMessage.start() 

  screen.blit(mainInfoFont.render('server1 inputKey >> ' + inputKey, True, (255, 255, 255)), [10,10]) 
  screen.blit(mainInfoFont.render('s1Pos >> ' + str(s1Pos[0]) + ':' + str(s1Pos[1]), True, (255, 255, 255)), [10,30]) 
  screen.blit(mainInfoFont.render('received message  >> ' + receiveMessage, True, (255, 255, 255)), [10,50]) 

  pygame.draw.rect(screen, (255,0,0), (s1Pos[0],s1Pos[1],15,15))
  pygame.draw.rect(screen, (0,0,255), (s2Pos[0],s2Pos[1],15,15))
