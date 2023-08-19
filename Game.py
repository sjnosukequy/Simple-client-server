import pygame, sys
from Players import Player
from Menu import Menu
from Network import Network
from Server import Server
from multiprocessing import Process

states = ['menu', 'server', 'client']
states_idx = 0
threads = []

class Game:
    def __init__(self):
        self.state = states[states_idx]
        self.P1 = Player(self, 'P1', (100,100), 20, 'red')
        self.P2 = Player(self, 'P1', (100,100), 20, 'blue')
        self.Menu = Menu(self)
        self.network = None
        self.server = None
        self.screen_w = screen_w
        self.screen_h = screen_h
    
    def run(self):
        self.state = states[states_idx]
        
        if self.state == 'menu':
            self.menu_run()
        elif self.state == 'server':
            pygame.display.set_caption("Host")
            if not self.server:
                self.server = Server()
                threads.append(Process(target= self.server.run))
                threads[0].start()

            if not self.network:
                 self.network = Network()

            self.P1.update()
            self.P2.pos[0], self.P2.pos[1] = Read_pos(self.network.send(send_pos(self.P1.pos)))
            self.P1.render(screen)
            self.P2.render(screen)
        else:
            pygame.display.set_caption("Client")
            if not self.network:
                 self.network = Network()
                 self.P2.pos[0], self.P2.pos[1] = Read_pos(self.network.getpos())
                 
            self.P2.update()
            self.P1.pos[0], self.P1.pos[1] = Read_pos(self.network.send(send_pos(self.P2.pos)))
            self.P2.render(screen)
            self.P1.render(screen)
    
    def menu_run(self):
        global states_idx
        res = self.Menu.run(screen)
        if res == 'server':
            states_idx = 1
        if res == 'client':
            states_idx = 2

    def game_run(self):
        pass

def Read_pos(text):
    text = text.split(",")
    return int(str(text[0])), int(str(text[1]))

def send_pos(pos):
    return str(pos[0]) + ',' + str(pos[1])


if __name__ == '__main__':
    screen_w = 640
    screen_h = 480
    screen = pygame.display.set_mode((screen_w, screen_h))
    clock = pygame.time.Clock()
    game = Game()

    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if game.server:
                    threads[0].kill()
                    threads[0].join()
                    
                pygame.quit()
                sys.exit()
        screen.fill('purple')
        game.run()
        pygame.display.flip()
        