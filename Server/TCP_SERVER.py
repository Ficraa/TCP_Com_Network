import socket
import pyautogui
import pydirectinput

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(("0.0.0.0", 9090))
serverSocket.listen()
while (True):
    (clientConnected, clientAddress) = serverSocket.accept()
    print("Accepted a connection request from %s:%s" %
          (clientAddress[0], clientAddress[1]))

    while True:
        try:
            dataFromClient = clientConnected.recv(1024)
            msg = dataFromClient.decode()
            print(msg)
            if msg.rsplit('(', 1)[0] == "move":
                pydirectinput.moveTo(int(msg[5:].rsplit(',', 1)[0]), int(
                    msg[5:-1].rsplit(',', 1)[1]))
            elif msg == "left":
                pydirectinput.press("left")
            elif msg == "right":
                pydirectinput.press("right")
            elif msg == "up":
                pydirectinput.press("up")
            elif msg == "down":
                pydirectinput.press("down")
            elif msg == "click":
                pydirectinput.click()
            clientConnected.send("h".encode())
        except:
            break
