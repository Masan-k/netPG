#!/usr/bin/env python
import asyncio
import websockets
import json
import pygame
import sys
import threading
import queue
import time

#def receiveLoop(ws):
def receiveLoop(ws):
  global q
    #RECEIVE.add(await websocket.recv()) 
    #RECEIVE.add(await websocket.recv()) 
  while True:
    time.sleep(2)
    print(" call dummy ")
    #print("thread print")
  #while True:
    #print("start receive")
    #q.put(await ws.recv())
    #print(q.get())
    #print("end receive")
    #print(await ws.recv())
    #RECEIVE.add(await websocket.recv()) 
  #async def gameMain(ws):

async def gameMainLoop(websocket):
  global q
  value = "X"
  usersCount = "X"

  pygame.init()
  black= (0, 0, 0)
  green= (0, 255, 0)
  width= 640
  height= 480
  screen= pygame.display.set_mode((width, height))
  pygame.display.set_caption("client1")
  font= pygame.font.Font(None, 30)
  clock= pygame.time.Clock()

  #RECEIVE = set()
 
  inputKey = "(-)"
  #q.put(await websocket.recv())
  #q.put(await websocket.recv())
  #RECEIVE.add(await websocket.recv()) 
  #RECEIVE.add(await websocket.recv())
  fpsCount = 0

  while True: 
    while not q.empty():
      print(q.get())

    fpsCount = fpsCount + 1
    if fpsCount % 600 == 0:
      fpscount = 0
      await websocket.send(json.dumps({"action": "get"}))
      #RECEIVE.add(await websocket.recv())
      #q.put(await websocket.recv())

    pygame.display.update()
    screen.fill(black)

    for event in pygame.event.get():
      if event.type== pygame.QUIT:
        pygame.quit()
        sys.exit()

      if event.type== pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          pygame.quit()
          sys.exit()
        if pygame.key.name(event.key) == 'p':
          await websocket.send(json.dumps({"action": "plus"}))
          #RECEIVE.add(await websocket.recv())
          #q.put(await websocket.recv())

        if pygame.key.name(event.key) == 'm':
          await websocket.send(json.dumps({"action": "minus"}))
          #q.put(await websocket.recv())
          #RECEIVE.add(await websocket.recv())

        inputKey = pygame.key.name(event.key)

        '''
    for recv in RECEIVE:
      typeValue = json.loads(recv)["type"] 
      if typeValue == 'users':
        usersCount = json.loads(recv)["count"] 
      elif typeValue == 'value':
        value = json.loads(recv)["value"]
      elif typeValue == 'get':
        value = json.loads(recv)["value"]
        userCount = json.loads(recv)["count"]
    RECEIVE.clear()
    '''

    screen.blit(font.render(str(usersCount) + "user online", True, (255, 255, 255)), [10, 50]) 
    screen.blit(font.render("value >> " + str(value), True, (255, 255, 255)), [10,80]) 
    screen.blit(font.render('p: value + 1' , True, (255, 255, 255)), [10, 180]) 
    screen.blit(font.render('m: value - 1' , True, (255, 255, 255)), [10, 210]) 


async def main():
  async with websockets.connect("ws://localhost:6789") as websocket:
    
    #await receiveLoop(websocket)
    #await gameMainLoop(websocket)
    t1 = threading.Thread(target=receiveLoop, args=(websocket, ))
    t2 = threading.Thread(target=gameMainLoop, args=(websocket, ))

    t1.start()
    t2.start()

    #t1.join()
    #t2.join()

    #await loopReceive(websocket,qu)
    #threading.Thread(target=loopReceive, args=(websocket,qu)).start()
    #c1 = receiveLoop(websocket)
    #c2 = gameMainLoop(websocket)
    #await asyncio.gather(c1, c2) #2つの処理の終了を待つ

q = queue.Queue()
if __name__ == "__main__":
  asyncio.run(main())

