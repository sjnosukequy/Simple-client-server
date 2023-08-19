import pygame

class Player:
    def __init__(self, game, e_type, pos, size, color, speed = 4 ):
        '''
        e_type = 'P1' / 'P2'
        '''
        self.type = e_type
        self.game = game
        self.pos = list(pos)
        self.Dir = [0,0]
        self.size = size
        self.color = color
        self.speed = speed

    def update(self):
        self.Movement()

        self.pos[0] += self.Dir[0]
        if self.Bound_check():
            if self.Dir[0] < 0:
                self.pos[0] = 0
            if self.Dir[0] >  0:
                self.pos[0] = self.game.screen_w - self.size

        self.pos[1] += self.Dir[1]
        if self.Bound_check():
            if self.Dir[1] < 0:
                self.pos[1] = 0
            if self.Dir[1] > 0:
                self.pos[1] = self.game.screen_h - self.size
    
    def Bound_check(self):
        rect = self.rect()

        if rect.left < 0:
            return True
        if rect.right > self.game.screen_w:
            return True
        if rect.top < 0:
            return True
        if rect.bottom > self.game.screen_h:
            return True
        
        return False

    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size, self.size)
    
    def render(self, dispaly):
        rect = self.rect()
        pygame.draw.rect(dispaly, self.color, rect)
    
    def Movement(self):
        keys = pygame.key.get_pressed()
        if self.type == 'P1':
            if keys[pygame.K_w]:
                self.Dir[1] = -1 * self.speed
            elif keys[pygame.K_s]:
                self.Dir[1] = 1 * self.speed
            else:
                self.Dir[1] = 0

            if keys[pygame.K_a]:
                self.Dir[0] = -1 * self.speed
            elif keys[pygame.K_d]:
                self.Dir[0] = 1 * self.speed
            else:
                self.Dir[0] = 0

        if self.type == 'P2':
            if keys[pygame.K_UP]:
                self.Dir[1] = -1 * self.speed
            elif keys[pygame.K_DOWN]:
                self.Dir[1] = 1 * self.speed
            else:
                self.Dir[1] = 0

            if keys[pygame.K_LEFT]:
                self.Dir[0] = -1 * self.speed
            elif keys[pygame.K_RIGHT]:
                self.Dir[0] = 1 * self.speed
            else:
                self.Dir[0] = 0

