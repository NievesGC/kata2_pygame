import pygame
import random



class Bolas:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800,600)) 
        pygame.display.set_caption("Bolas")

        #self.player = Ball(400,300,30,(255,255,255), random.randint(-15,15),random.randint(-15,15),)
        self.player = Ball(400,300,10,dx=10,dy=15)
        self.metronomo = pygame.time.Clock()

    def main_loop(self):
        game_over = False
        while game_over == False: 
            self.metronomo.tick(60)  
            for evento in pygame.event.get(): 
                if evento.type == pygame.QUIT:  
                    game_over = True
                    

                        
            self.screen.fill((0,255,0))
            
            self.player.draw(self.screen)
           
            self.player.x += self.player.dx
            self.player.y += self.player.dy
            
            

            if self.player.y >= 600 - self.player.radio or self.player.y <= 0 + self.player.radio:
                self.player.dy = -self.player.dy
            if self.player.x >= 800 - self.player.radio or self.player.x <= 0 + self.player.radio:
                self.player.dx = -self.player.dx       
            
            pygame.display.flip()

class Ball:
    def __init__(self, x,y,radio, color =(255,255,255),dy = 0, dx = 0):
        self.x = x
        self.y = y
        self.radio = radio
        self.color = color
        self.dx= dx
        self.dy = dy
        
    def draw(self,surface):
        pygame.draw.circle(surface,self.color,(self.x,self.y), self.radio)

if __name__ == "__main__":
    bola = Bolas()
    bola.main_loop()