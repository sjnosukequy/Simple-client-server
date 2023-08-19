import pygame
pygame.init()

Font = pygame.font.Font('Pixeltype.ttf', 50)

def BUTTON(content, color, pos, size):
    rect = pygame.Rect(pos[0] - size[0]//2 , pos[1] - size[1]//2, size[0], size[1])
    text = Font.render(content, False, color)
    return text, rect

class Menu:
    def __init__(self, game):
        self.game = game
        self.server, self.ser_rect = BUTTON("sever", 'orange', (320,200), (110, 50))
        self.client, self.cl_rect = BUTTON('Client', "Blue", (320, 260), (110, 50))

    def run(self, surf):
        self.render(surf)

        mouse = pygame.mouse.get_pos()

        if self.ser_rect.collidepoint(mouse[0], mouse[1]):
            pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_HAND)
        elif self.cl_rect.collidepoint(mouse[0], mouse[1]):
            pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
             pygame.mouse.set_system_cursor(0)
             
        mouse_click = pygame.mouse.get_pressed()
        if mouse_click[0]:
            if self.ser_rect.collidepoint(mouse[0], mouse[1]):
                pygame.mouse.set_system_cursor(0)
                return 'server'
            if self.cl_rect.collidepoint(mouse[0], mouse[1]):
                pygame.mouse.set_system_cursor(0)
                return 'client'

    def render(self, surf):
        ## SERVER
        sur_surf = pygame.Surface((self.ser_rect.width, self.ser_rect.height))
        sur_surf.fill('black')
        surf.blit(sur_surf, self.ser_rect)
        text_rect = self.server.get_rect(center = self.ser_rect.center)
        surf.blit(self.server, text_rect)

        ##CLIENT
        sur_surf = pygame.Surface((self.cl_rect.width, self.cl_rect.height))
        sur_surf.fill('black')
        surf.blit(sur_surf, self.cl_rect)
        text_rect = self.client.get_rect(center = self.cl_rect.center)
        surf.blit(self.client, text_rect)
