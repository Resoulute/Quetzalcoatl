import pygame, sys

state = 0
icon = pygame.image.load("images\\quetzalcoatlIcon.png")

#reading through the configurations
options = open("config.txt", 'r')
for line in options:
	#use this loop to go through each of the lines and get settings, or not do that cause that does sound kinda dumb af
	print(line)

options.close()

size = width, height = 640, 480
black = 0,0,0
white = 255,255,255
pos = xpos, ypos = 320, 240

squareSize = width, height = 160, 120
screen = pygame.display.set_mode(size)
square = pygame.Surface(squareSize)
squareRect = square.get_rect()

Square = pygame.draw.rect(square, white, squareRect, 5)

class Block(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

print("Hello world")


pygame.display.set_caption("Quetzalcoatl Game Engine")
pygame.display.set_icon(icon)
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()

		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_DOWN:
				ypos += 10; pos = xpos, ypos;
			if event.key == pygame.K_UP:
				ypos -= 10; pos = xpos, ypos;
			if event.key == pygame.K_LEFT:
				xpos -= 10; pos = xpos, ypos;
			if event.key == pygame.K_RIGHT:
				xpos += 10; pos = xpos, ypos;

	screen.fill(black)
	screen.blit(square, pos)
	pygame.display.update()