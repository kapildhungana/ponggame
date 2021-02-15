import pygame, sys, random

def ball_animation():
	global ball_speed_x, ball_speed_y, player_score, opponent_score, score_time
	
	ball.x += ball_speed_x
	ball.y += ball_speed_y

	if ball.top <= 0 or ball.bottom >= screen_height:
		pygame.mixer.Sound.play(plob_sound)
		ball_speed_y *= -1
		
	# Player Score
	if ball.left <= 0: 
		pygame.mixer.Sound.play(score_sound)
		score_time = pygame.time.get_ticks()
		player_score += 1
		
	# Opponent Score
	if ball.right >= screen_width:
		pygame.mixer.Sound.play(score_sound)
		score_time = pygame.time.get_ticks()
		opponent_score += 1
		
	if ball.colliderect(player) and ball_speed_x > 0:
		pygame.mixer.Sound.play(plob_sound)
		if abs(ball.right - player.left) < 10:
			ball_speed_x *= -1	
		elif abs(ball.bottom - player.top) < 10 and ball_speed_y > 0:
			ball_speed_y *= -1
		elif abs(ball.top - player.bottom) < 10 and ball_speed_y < 0:
			ball_speed_y *= -1

	if ball.colliderect(opponent) and ball_speed_x < 0:
		pygame.mixer.Sound.play(plob_sound)
		if abs(ball.left - opponent.right) < 10:
			ball_speed_x *= -1	
		elif abs(ball.bottom - opponent.top) < 10 and ball_speed_y > 0:
			ball_speed_y *= -1
		elif abs(ball.top - opponent.bottom) < 10 and ball_speed_y < 0:
			ball_speed_y *= -1
	
	if ball.colliderect(block):
		pygame.mixer.Sound.play(plob_sound)
		if ball_speed_x > 0:
			if abs(ball.right - block.left) < 10:
				ball_speed_x *= -1	
			elif abs(ball.bottom - block.top) < 10 and ball_speed_y > 0:
				ball_speed_y *= -1
			elif abs(ball.top - block.bottom) < 10 and ball_speed_y < 0:
				ball_speed_y *= -1
		if ball_speed_x < 0:
			if abs(ball.left - block.right) < 10:
				ball_speed_x *= -1	
			elif abs(ball.bottom - block.top) < 10 and ball_speed_y > 0:
				ball_speed_y *= -1
			elif abs(ball.top - block.bottom) < 10 and ball_speed_y < 0:
				ball_speed_y *= -1

	if ball.colliderect(block1):
		pygame.mixer.Sound.play(plob_sound)
		if ball_speed_x > 0:
			if abs(ball.right - block1.left) < 10:
				ball_speed_x *= -1	
			elif abs(ball.bottom - block1.top) < 10 and ball_speed_y > 0:
				ball_speed_y *= -1
			elif abs(ball.top - block1.bottom) < 10 and ball_speed_y < 0:
				ball_speed_y *= -1
		if ball_speed_x < 0:
			if abs(ball.left - block1.right) < 10:
				ball_speed_x *= -1	
			elif abs(ball.bottom - block1.top) < 10 and ball_speed_y > 0:
				ball_speed_y *= -1
			elif abs(ball.top - block1.bottom) < 10 and ball_speed_y < 0:
				ball_speed_y *= -1
	
	if ball.colliderect(portr):
		ball.x=screen_width/2
		ball.y=screen_height/2
		if ball_speed_x > 0:
			if abs(ball.right - portr.left) < 10:
				ball_speed_x *= -1	
			elif abs(ball.bottom - portr.top) < 10 and ball_speed_y > 0:
				ball_speed_y *= -1
			elif abs(ball.top - portr.bottom) < 10 and ball_speed_y < 0:
				ball_speed_y *= -1
		if ball_speed_x < 0:
			if abs(ball.left - portr.right) < 10:
				ball_speed_x *= -1	
			elif abs(ball.bottom - portr.top) < 10 and ball_speed_y > 0:
				ball_speed_y *= -1
			elif abs(ball.top - portr.bottom) < 10 and ball_speed_y < 0:
				ball_speed_y *= -1
	
	if ball.colliderect(portl):
		ball.x=screen_width/2
		ball.y=screen_height/2
		if ball_speed_x > 0:
			if abs(ball.right - portl.left) < 10:
				ball_speed_x *= -1	
			elif abs(ball.bottom - portl.top) < 10 and ball_speed_y > 0:
				ball_speed_y *= -1
			elif abs(ball.top - portl.bottom) < 10 and ball_speed_y < 0:
				ball_speed_y *= -1
		if ball_speed_x < 0:
			if abs(ball.left - portl.right) < 10:
				ball_speed_x *= -1	
			elif abs(ball.bottom - portl.top) < 10 and ball_speed_y > 0:
				ball_speed_y *= -1
			elif abs(ball.top - portl.bottom) < 10 and ball_speed_y < 0:
				ball_speed_y *= -1

		

def player_animation():
	player.y += player_speed

	if player.top <= 0:
		player.top = 0
	if player.bottom >= screen_height:
		player.bottom = screen_height

def opponent_ai():
	x=opponent.top
	y=opponent.bottom
	if (x+y)/2< ball.y:
		opponent.y += opponent_speed
	if (x+y)/2 > ball.y:
		opponent.y -= opponent_speed

	if opponent.top <= 0:
		opponent.top = 0
	if opponent.bottom >= screen_height:
		opponent.bottom = screen_height

def block_ai():
	global block_speed
	#if block.top < ball.y:
	block.y += block_speed
	#if block.bottom > ball.y:
	#block.y -= block_speed

	if block.top <= 0:
		block_speed= -block_speed
	if block.bottom >screen_height:
		block_speed =-block_speed

def block1_ai():
	global block1_speed
	#if block.top < ball.y:
	block1.y += block1_speed
	#if block.bottom > ball.y:
	#block.y -= block_speed

	if block1.top <= 0:
		block1_speed= -block1_speed
	if block1.bottom >screen_height:
		block1_speed =-block1_speed

def ball_start():
	global ball_speed_x, ball_speed_y, ball_moving, score_time

	ball.center = (screen_width/2, screen_height/2)
	current_time = pygame.time.get_ticks()

	if current_time - score_time < 700:
		number_three = basic_font.render("3",False,light_grey)
		screen.blit(number_three,(screen_width/2 - 10, screen_height/2 + 20))
	if 700 < current_time - score_time < 1400:
		number_two = basic_font.render("2",False,light_grey)
		screen.blit(number_two,(screen_width/2 - 10, screen_height/2 + 20))
	if 1400 < current_time - score_time < 2100:
		number_one = basic_font.render("1",False,light_grey)
		screen.blit(number_one,(screen_width/2 - 10, screen_height/2 + 20))

	if current_time - score_time < 2100:
		ball_speed_y, ball_speed_x = 0,0
	else:
		ball_speed_x = 7 * random.choice((1,-1))
		ball_speed_y = 5.5 * random.choice((1,-1))
		score_time = None

# General setup
pygame.mixer.pre_init(44100,-16,1, 1024)
pygame.init()
clock = pygame.time.Clock()

# Main Window
screen_width = 1280
screen_height = 650#960
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Pong')

# Colors
light_grey = (200,200,200)
red=(200,0,0)
blue=(0,0,200)
sky=(0,0,50)
orange=(255,100,0)
green=pygame.Color('green')
yellow=pygame.Color('yellow')
bg_color = pygame.Color('grey12')

# Game Rectangles
ball = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, 20, 20)
player = pygame.Rect(screen_width - 20, screen_height / 2 - 70, 10,140)
opponent = pygame.Rect(10, screen_height / 2 - 70, 10,140)
block=pygame.Rect(screen_width / 2-190 , screen_height / 2 + 80, 50, 140)
block1=pygame.Rect(screen_width / 2+190 , screen_height / 2 - 280, 50, 140)
portl=pygame.Rect(screen_width/2-250, 25, 50, 50)
portr=pygame.Rect(screen_width/2+130, screen_height-45, 50, 50)

# Game Variables
ball_speed_x = 7 * random.choice((1,-1))
ball_speed_y = 5.5 * random.choice((1,-1))
player_speed = 0
opponent_speed = 7
block_speed=1.5
block1_speed=1.5
ball_moving = False
score_time = True

# sound 
plob_sound = pygame.mixer.Sound("pong.ogg")
score_sound = pygame.mixer.Sound("score.ogg")

# Score Text
player_score = 0
opponent_score = 0
basic_font = pygame.font.Font('freesansbold.ttf', 32)
mode=0
win=0
won=0
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				player_speed -= 6
			if event.key == pygame.K_DOWN:
				player_speed += 6
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_UP:
				player_speed += 6
			if event.key == pygame.K_DOWN:
				player_speed -= 6
		if event.type == pygame.KEYUP:
			if event.key==pygame.K_LEFT:
				mode=1
				opponent_score=0
				player_score=0

	if mode==0:
		#ball_animation()
		screen.fill(orange)
		if win==0:
			title = basic_font.render(f'$$$$$$ PONG GAME $$$$$$$',False,light_grey)
			enter = basic_font.render(f'Press left key to start the game',False,light_grey)
			screen.blit(enter,(screen_width/2-200,370))
			screen.blit(title,(screen_width/2-200,150))
		if win==1:
			title = basic_font.render(f'$$$$$$ PONG GAME $$$$$$$',False,light_grey)
			enter = basic_font.render(f'Press left key to play again',False,light_grey)
			if won==0:
				w=basic_font.render(f'$$$$$$ YOU WON $$$$$$',False,light_grey)
			else:
				w=basic_font.render(f'$$$$$$ YOU LOST $$$$$$',False,light_grey)
			screen.blit(title,(screen_width/2-230,150))
			screen.blit(enter,(screen_width/2-200,470))
			screen.blit(w,(screen_width/2-200,330))

	if mode==1:
		#Game Logic
		ball_animation()
		player_animation()
		opponent_ai()
		block_ai()
		block1_ai()

		# Visuals 
		screen.fill(sky)#green)#bg_color)
		pygame.draw.rect(screen, blue, player)
		pygame.draw.rect(screen, light_grey, block)
		pygame.draw.rect(screen, light_grey, block1)
		pygame.draw.rect(screen, red, opponent)
		pygame.draw.ellipse(screen, yellow, ball)
		pygame.draw.ellipse(screen, (0,0,0), portl)
		pygame.draw.ellipse(screen, (0,0,0), portr)
		pygame.draw.aaline(screen, light_grey, (screen_width / 2, 0),(screen_width / 2, screen_height))

		if score_time:
			ball_start()

		player_text = basic_font.render(f'{player_score}',False,light_grey)
		screen.blit(player_text,(660,470))

		opponent_text = basic_font.render(f'{opponent_score}',False,light_grey)
		screen.blit(opponent_text,(600,470))
		if opponent_score>=3:
			win=1
			won=1
			mode=0
		if player_score>=3:
			win=1
			won=2
			mode=0
		
			

	pygame.display.flip()
	clock.tick(60)