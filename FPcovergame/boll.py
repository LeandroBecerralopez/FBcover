import pygame as py
import sys,random

class Bird(py.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = py.image.load("bird.png")
		self.rect = self.image.get_rect()
		self.rect.x = 100
		self.rect.y  = 300
	def update(self):
		global hight
		if hight>0:
			self.rect.y -=4
			hight = hight-1
		else:
			self.rect.y +=4
class Tubes(py.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image1 = py.image.load("dtube.png")
		self.image2 = py.image.load("utube.png")
		self.rect1 =self.image1.get_rect()
		self.rect2 =self.image2.get_rect()
	def  update(self):
		self.rect1.x -=3
		self.rect2.x -=3
		if self.rect1.x<-90:
			self.rect1.x = 470
			self.rect2.x = 470
			self.rect1.y = random.randrange(300,500,50)
			self.rect2.y = self.rect1.y -766
class Ground(py.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = py.image.load("grond.png")
		self.rect = self.image.get_rect()
		self.rect.x = 0
		self.rect.y = 560
	def update(self):
		self.rect.x -= 3
		if self.rect.x <-360:
			self.rect.x = 0
class Game(object):
	def __init__(self):
		self.game_over  = False
		self.score=0
		self.bird = Bird()
		self.ground = Ground()
		self.tubes_list = py.sprite.Group()
		for i in [0,1,2]:
			tubes = Tubes()
			tubes.rect1.x = 360+(i*190)
			tubes.rect2.x = 360+(i*190)
			tubes.rect1.y = random.randrange(300,500,50)
			tubes.rect2.y = tubes.rect1.y-150-626
			self.tubes_list.add(tubes)
	def process_envents(self):
		global done,hight
		for event in py.event.get():
			if event.type == py.QUIT:
				done = True
			#Eventos teclado
			if event.type == py.KEYDOWN:
				if event.key == py.K_SPACE:
					hight = 13
					if self.game_over:
						self.__init__()

			if event.type == py.KEYUP:
				if event.key == py.K_SPACE:
					pass
	def run_logic(self):
		if not self.game_over:
			self.tubes_list.update() 
			self.ground.update()
			self.bird.update()
			for dutube in self.tubes_list:
				if self.bird.rect.colliderect(dutube.rect1) or self.bird.rect.colliderect(dutube.rect2):
					self.game_over = True
			if self.bird.rect.y>=self.ground.rect.y-35:
				self.game_over = True
	def display_Frame(self,screen,backg):
		screen.blit(backg,[0,0])
		if self.game_over:
			font = py.font.Font("04B_19__.ttf",50)
			text = font.render("GAME OVER",True,(247, 241, 168))
			text1 = font.render("SPACE TO",True,(247, 241, 168))
			text2 = font.render("CONTINUE",True,(247, 241, 168))
			screen.blit(text,[50,100])
			screen.blit(text1,[70,400])
			screen.blit(text2,[75,470])
			screen.blit(self.ground.image,self.ground.rect)
			screen.blit(self.bird.image,[140,300])
		if not self.game_over:
			for entity in self.tubes_list:
				screen.blit(entity.image1,entity.rect1)
				screen.blit(entity.image2,entity.rect2)
			screen.blit(self.bird.image,self.bird.rect)
			screen.blit(self.ground.image,self.ground.rect)
		py.display.flip()
def main():
	py.init()
	backg = py.image.load("background.png")
	screen = py.display.set_mode((360,640))
	global hight,done
	done = False
	hight = 0
	clock = py.time.Clock()
	game = Game()
	while not done:
		game.process_envents()
		game.run_logic()
		game.display_Frame(screen,backg)
		clock.tick(60)
	py.quit()
if __name__=="__main__":
	main()

