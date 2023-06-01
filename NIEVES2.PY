import pygame
import random



class Bolas:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800,600)) 
        pygame.display.set_caption("Bolas")

        self.player = Ball(400,300,30,(255,255,255))
        self.player1 = Ball(300,200,30,(0,0,0))
        self.metronomo = pygame.time.Clock()

    def main_loop(self):
        game_over = False
        dy = random.randint(-10,10)
        dx = random.randint(-10,10)
        dy1 = random.randint(-10,10)
        dx1 = random.randint(-10,10)
        while game_over == False: 
            self.metronomo.tick(60)  
            for evento in pygame.event.get(): 
                if evento.type == pygame.QUIT:  
                    game_over = True
                    

                        
            self.screen.fill((0,255,0))
            
            self.player.draw(self.screen)
            self.player1.draw(self.screen)
           
            self.player.x += dx
            self.player.y += dy

            self.player1.x += dx1
            self.player1.y += dy1
            
            if self.player.y <= self.player.radio or self.player.y >= 600 - self.player.radio:
                dy = -dy
            if self.player.x <= self.player.radio or self.player.x >= 800 - self.player.radio:
                dx = -dx
            
            if self.player1.y <= self.player1.radio or self.player1.y >= 600 - self.player1.radio:
                dy1 = -dy1
            if self.player1.x <= self.player1.radio or self.player1.x >= 800 - self.player1.radio:
                dx1 = -dx1
            
            pygame.display.flip()

class Ball:
    def __init__(self, x,y,radio, color ):
        self.x = x
        self.y = y
        self.radio = radio
        self.color = color

        
    def draw(self,surface):
        pygame.draw.circle(surface,self.color,(self.x,self.y), self.radio)

if __name__ == "__main__":
    bola = Bolas()
    bola.main_loop()