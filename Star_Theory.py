import pygame
import random

"""To Do List"""
# 1. Give Baddies Bullets
# 2. Have Shot Baddies Drop Items
# 3. Introduce Different Classes of Baddies
# 4. Create Splash Screen
# 5. Start Menu
# 6. High Score List
# 7. Start Using png Sprite images
# 8. Create Distinct Bullet, Hero, and Enemy Classes
# 9. Add explosion animation

"""Done"""
# Pause Function
# Speed Up Function
# Shoot Laser
# Rainbow Laser
# Wrap Around
# Starfield



def main_loop():

	restart = False

	if pygame.init():
		pygame.quit()
		
	pygame.init()

	BLACK = (000,000,000)
	WHITE = (255,255,255)
	LGRAY = (200,200,200)
	GRAY = (100,100,100)
	RED   = (255,000,000)
	BLUE  = (000,000,255)
	GREEN = (000,255,000)
	DGREEN = (000,175,000)
		
	class Block(pygame.sprite.Sprite):
		"""
		This class represents the ball.
		It derives from the "Sprite" class in Pygame.
		"""
		def __init__(self, color, width, height):
			""" Constructor. Pass in the color of the block,
			and its x and y position. """
			
			# Call the parent class (Sprite) constructor
			super(Block, self).__init__()
			
			# Create an image of the block, and fill it with a color.
			# This could also be an image loaded from the disk.
			self.image = pygame.Surface([width, height])
			self.image.fill(color)
			#self.image.set_colorkey(BLACK)
			
			# Draw the ellipse
			pygame.draw.ellipse(self.image, color, [0, 0, width, height])

			# Fetch the rectangle object that has the dimensions of the image
			# Update the position of this object by setting the values
			# of rect.x and rect.y
			self.rect = self.image.get_rect()
			
	class Hero(pygame.sprite.Sprite):
		def __init__(self):
			super(Hero, self).__init__()
			self.image = pygame.image.load("hero.bmp")
			self.image.set_colorkey(RED)
			self.rect = self.image.get_rect()
			
	# initialize Pygame
	#if not pygame.init():
	#	pygame.init()

	#set the height and width of the screen
	screen_width = 700
	screen_height = 400
	screen = pygame.display.set_mode([screen_width, screen_height])
	score = 0

	def startScreen():
		while True:
			welcome = myFont.render("Welcome to Star Theory!", 1, (WHITE))
			screen.blit(welcome, (screen_width/4, 0))
			pygame.display.flip()
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					return
					
	def pauseScreen():
		while True:
			pause = myFont.render("Game Paused", 1, (WHITE))
			screen.blit(pause, (0, 0))
			pygame.display.flip()
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
					return
					
	# Groups.
	block_list = pygame.sprite.Group()
	bullet_list = pygame.sprite.Group()
	star_list = pygame.sprite.Group()
	all_sprites_list = pygame.sprite.Group()
	side_panel_list = pygame.sprite.Group()
	bullet_panel_list = pygame.sprite.Group()

	player = Hero()
	all_sprites_list.add(player)

	adjusted_screen_width = screen_width - 20

	for i in range(10):
		# this represents a block
		bad_color = random.randint(50, 250)
		block = Block((bad_color,bad_color,bad_color), 20, 15)
		
		# set a random location for the block
		block.rect.x = random.randrange(adjusted_screen_width)
		block.rect.y = random.randrange(-200, 0)
		
		# add the block to the list of objects
		block_list.add(block)
		all_sprites_list.add(block)
			
	# create player bullet
	bullet = Block(RED, 3, screen_height)


	# create sidepanel
	sidepanel = Block(BLACK, 20, screen_height)
	sidepanel.rect.x = adjusted_screen_width
	sidepanel.rect.y = 0
	side_panel_list.add(sidepanel)

	# bullet_energy_bar
	bullet_energy_bar = Block(WHITE, 20, screen_height)
	bullet_energy_bar.rect.x = adjusted_screen_width
	bullet_energy_bar.y = 0
	bullet_panel_list.add(bullet_energy_bar)

	done = False

	clock = pygame.time.Clock()

	player.rect.x = screen_width/2
	player.rect.y = screen_height - 35

	good_speed = 5

	center = 15


	# add score keeper on screen
	myFont = pygame.font.SysFont("monospace", 22)
	myFont.set_bold(True)

	startScreen()

	while not done:
		key = pygame.key.get_pressed()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
			if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
				done = True
			if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
				pauseScreen()
		if key[pygame.K_SPACE]:
			# First, empty the current bullet_list to ensure deletion of stray bullets
			if bullet_energy_bar.rect.y < screen_height:
				if len(bullet_list) > 1:
					bullet_list.empty()
				gray_scale = random.randint(0, 255)
				bullet = Block((gray_scale,gray_scale,gray_scale),
					random.randint(1, 3), screen_height)
				bullet_list.add(bullet)
				bullet.rect.x = player.rect.x + center
				bullet.rect.y = screen_height - 8
				if bullet_energy_bar.rect.y < screen_height:
					bullet_energy_bar.rect.y += 1
		if not key[pygame.K_SPACE] and bullet_energy_bar.rect.y > 0:
			bullet_energy_bar.rect.y -= 1
						
		#key = pygame.key.get_pressed()
		if key[pygame.K_LSHIFT]:
		    good_speed = 10
		else:
		    good_speed = 5
		if key[pygame.K_LEFT]:
			if player.rect.x < 1:
				player.rect.x = adjusted_screen_width #screen_width
				bullet.rect.x = player.rect.x + center
			else:
				player.rect.x -= good_speed
				bullet.rect.x = player.rect.x + center
		if key[pygame.K_RIGHT]:
			if player.rect.x > adjusted_screen_width: #screen_width:
				player.rect.x = 0
				bullet.rect.x = player.rect.x + center
			else:
				player.rect.x += good_speed
				bullet.rect.x = player.rect.x + center
			
		# clear the screen to be drawn upon
		screen.fill(BLACK)
		
		# make more shinies at random intervals
		if random.randint(0, 10) == 3:	
			new_bad_color = random.randint(50, 250)
			block = Block((new_bad_color,new_bad_color,new_bad_color), 20, 15)
			block.rect.x = random.randrange(adjusted_screen_width) #(screen_width)
			block.rect.y = random.randrange(-200, 0)
			block_list.add(block)
			all_sprites_list.add(block)

		#check for baddie shot
		for bullet in bullet_list:
			bullet_hit_list = pygame.sprite.spritecollide(bullet, block_list, True)
			for block in bullet_hit_list:
				bullet_list.remove(bullet)
				score += 1
				
		#check for death (collision)
		death = pygame.sprite.spritecollide(player, block_list, False)
		if death:
			while done == False:
				death_text = myFont.render("DEAD: " + str(score) +
					" POINTS", 1, (WHITE))
				screen.blit(death_text, (0, 0))
				pygame.display.flip()
				for event in pygame.event.get():
					if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
						done = True	
					elif event.type == pygame.KEYDOWN and event.key == pygame.K_y:
						restart = True
						done = True
			
		# animate the baddies
		for block in block_list:
			# moving down
			block.rect.y += random.randrange(0, 5)
			if block.rect.y > screen_height:
				block.rect.y = 0
			# moving left and right
			block.rect.x += random.randrange(-8, 8)
			if block.rect.x > adjusted_screen_width: #screen_width:
				block.rect.x = 0
			if block.rect.x < 0:
				block.rect.x = adjusted_screen_width #screen_width

		# animate bullets
		for bullet in bullet_list:
			bullet.rect.y -= screen_height
			
		randcolor = random.randrange(100, 255)
		randxy = random.randrange(1, 5)
		star = Block((randcolor,randcolor,randcolor), randxy, randxy)
		star.rect.x = random.randrange(0, adjusted_screen_width) #screen_width)
		star.rect.y = random.randrange(-200, screen_height)
		star_list.add(star)
		
		# animate stars
		for star in star_list:
			star.rect.y += 1
			if star.rect.y > screen_height:
				star_list.remove(star)	

		# draw all the sprites
		star_list.draw(screen)
		bullet_list.draw(screen)	
		all_sprites_list.draw(screen)
		side_panel_list.draw(screen)
		bullet_panel_list.draw(screen)
		
		# draw the scoreboard
		scoreBoard = myFont.render(str(score), 1, (WHITE))
		screen.blit(scoreBoard, (0, 0))#(screen_width/2, screen_height/2))
		
		# limit to 60 frames per second
		clock.tick(60)
		
		# Go ahead and update the screen with what we've drawn
		pygame.display.flip()
	
	#pygame.display.quit()
	pygame.quit()
	if restart == True:
	    main_loop()
main_loop()
