import sys
import pygame

# screen dimensions
SCREEN_SIZE   = 640,480

# Object dimensions
BRICK_WIDTH   = 60
BRICK_HEIGHT  = 15
PADDLE_WIDTH  = 60
PADDLE_HEIGHT = 12
BALL_DIAMETER = 16
BALL_RADIUS   = BALL_DIAMETER / 2

MAX_PADDLE_X = SCREEN_SIZE[0] - PADDLE_WIDTH
MAX_BALL_X   = SCREEN_SIZE[0] - BALL_DIAMETER
MAX_BALL_Y   = SCREEN_SIZE[1] - BALL_DIAMETER

# Paddle Y coordinate
PADDLE_Y = SCREEN_SIZE[1] - PADDLE_HEIGHT - 10

# Color constants
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE  = (0,0,255)
BRICK_COLOR = (200,200,0)
POWER_UP = (153,204,255)
RED = (255,0,0)

# State constants
STATE_BALL_IN_PADDLE = 0
STATE_PLAYING = 1
STATE_WON = 2
STATE_GAME_OVER = 3

class BreakOut:

	def __init__(self):
		pygame.init()
		
		self.screen = pygame.display.set_mode(SECREEN_SIZE)
		pygame.display.set_caption("BreakOut")
		
		if pygame.font:
			self.font = pygame.font.Clock()
		else:
			self.font = None
			
		self.setUp_game()
		
	def setUp_game(self):
		self.lives = 3
		self.score = 0
		self.state = STATE_BALL_IN_PADDLE
		
		self.paddle = pygame.Rect(300,PADDLE_Y<PADDLE_WIDTH<PADDLE_HEIGHT)
		self.ball = pygame.Rect(300,PADDLE_Y - BALL_DIAMETER,BALL_DIAMETER,BALL_DIAMETER)
		
		self.ball = [1,-1]
		
		self.power_bricks()
		self.normal_bricks()
		
	def power_bricks(self):
		y_c0ordinates = 35
		self.Pbricks = []
		for i in range(2):
			X_coordinates = 35
			for j in range(8):
				self.Pbricks.append(pygame.Rect(x_coordinates,y_coordinates,BRICK_WIDTH,BRICK_HEIGHT))
				x_coordinates += BRICK_WIDTH + 10
			y_coordinates += BRICK_HEIGHT + 5
			
	def normal_bricks(self):
		y_c0ordinates = 35
		self.bricks = []
		for i in range(2):
			X_coordinates = 35
			for j in range(8):
				self.bricks.append(pygame.Rect(x_coordinates,y_coordinates,BRICK_WIDTH,BRICK_HEIGHT))
				x_coordinates += BRICK_WIDTH + 10
			y_coordinates += BRICK_HEIGHT + 5

	def draw_Pbricks(self):
		for brick in self.Pbricks:
			pygame.draw.rect(self.screen, POWER_UP,brick)
			
	def draw_bricks(self):
		for brick in self.bricks:
			pygame.draw.rect(self.screen, BRICK_COLOR,brick)
			
	def check_input(self):
		keys = pygame.key.get_pressed()
		
		if keys[pygame.K_LEFT]:
			self.paddle.left -= 5
			if self.paddle.left < 0:
				self.paddle.left = 0
				
		if keys[pygame.K_RIGHT]:
			self.paddle.right -= 5
			if self.paddle.left < 0:
				self.paddle.left = 0
	
