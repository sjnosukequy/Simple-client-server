import socket
import sys
from _thread import *  # type: ignore

pos = [[100, 100], [100, 100]]

class Server:
    def __init__(self):
        self.stop = False
        self.server = "localhost"
        self.port = 5555

        self.Current_Player = 0
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            self.s.bind((self.server, self.port))
        except socket.error as e:
            str(e)

        self.s.listen(2)
        print("waiting for connection, server started !!")

    def run(self):
        while True:
            conn, addr = self.s.accept()
            print("connecting to", addr)
            start_new_thread(self.thread_client, (conn, self.Current_Player))
            self.Current_Player += 1

    def thread_client(self, conn, Player):
        conn.send(str.encode(send_pos(pos[Player])))
        reply = ""
        while True:
            try:
                data = Read_pos(conn.recv(2048).decode())
                pos[Player][0], pos[Player][1] = data[0], data[1]

                if not data:
                    print("Disconnected")
                    break
                else:
                    if Player == 1:
                        reply = pos[0]
                    else:
                        reply = pos[1]

                    # print("Received: ", reply)
                    # print("Sending : ", reply)

                conn.sendall(str.encode(send_pos(reply)))              
            except:
                break

        print("Lost connection")
        conn.close()
        self.Current_Player -= 1

def Read_pos(text):
    text = text.split(",")
    return int(str(text[0])), int(str(text[1]))


def send_pos(pos):
    return str(pos[0]) + ',' + str(pos[1])
