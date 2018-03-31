import pygame
import random

#Define Colour
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)




class Spaceship(pygame.sprite.Sprite):
	"""docstring for Spaceship"""
	def __init__(self):
		super(Spaceship, self).__init__()
		
		self.image = pygame.image.load("spaceship1.png").convert()
		self.image.set_colorkey(WHITE)

		self.rect = self.image.get_rect()


class Shoot(pygame.sprite.Sprite):
    """docstring for Shoot"""
    def __init__(self):
        super(Shoot, self).__init__()

        self.image = pygame.image.load("shot.gif").convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()




class Ufo(pygame.sprite.Sprite):
	"""This class represent the Block
	It is derieved from Sprite class in pygame
	All functionality of Sprite is now in Block class"""
	def __init__(self):

		# Call the parent file 'sprite' constructor
		#It is inportant to call the parent class constructor in 'Sprite' to allow sprite to initialize
		super().__init__()


		self.image = pygame.image.load("ufo.png").convert()
		self.image.set_colorkey(BLACK)

# image.
# Update the position of this object by setting the values
# of rect.x and rect.y
		self.rect = self.image.get_rect()

# Initialize Pygame
pygame.init()
 
# Set the height and width of the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode([screen_width, screen_height])


# This is a list of 'sprites.' Each block in the program is
# added to this list.
# The list is managed by a class called 'Group.'
ufo_list = pygame.sprite.Group()
shoot_list = pygame.sprite.Group()

# This is a list of every sprite.
# All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()

for i in range(50):
    # This represents a block
    ufoInit = Ufo()
 
    # Set a random location for the block
    ufoInit.rect.x = random.randrange(screen_width)
    ufoInit.rect.y = random.randrange(screen_height)
 
    # Add the block to the list of objects
    ufo_list.add(ufoInit)
    all_sprites_list.add(ufoInit)

# Create a RED player block
player = Spaceship()
all_sprites_list.add(player)


# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
score = 0

bg = pygame.image.load("backgroundSpace1.jpg")
FPS = 120
# How many seconds the "game" is played.
playtime = 0.0
#######################################Game Loop###############################################################
while not done:
    milliseconds = clock.tick(FPS) #amount of milliseconds passed since the last frame
    playtime += milliseconds / 1000.

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouseLeft = True
            shootInit = Shoot()
            shoot_list.add(shootInit)
            all_sprites_list.add(shootInit)
            shootInit.rect.x = pos[0]+21
            shootInit.rect.y = pos[1]
            shootInit.y_axis = pos[1]
 
    # Clear the screen
    # mypicture = pygame.image.load("background1.jpg")
    # mypicture = mypicture.convert()
   

    screen.fill(WHITE)
    screen.blit(bg, (0, 0))

    # Get the current mouse position. This returns the position
    # as a list of two numbers.
    pos = pygame.mouse.get_pos()
 
    # Fetch the x and y out of the list,
    # just like we'd fetch letters out of a string.
    # Set the player object to the mouse location
    player.rect.x = pos[0]
    player.rect.y = pos[1]



    # See if the player block has collided with anything.
    blocks_hit_list = pygame.sprite.groupcollide(shoot_list, ufo_list,True,True, None)
    # col = pygame.sprite.spritecollideany(player, ufo_list, collided = None)
    for shoot in shoot_list:
        shoot.rect.y-= 9
        if shoot.rect.y < -15:
            shoot_list.remove (shoot)
        # print(shoot.rect.y)
    # Check the list of collisions.
    for block in blocks_hit_list:
        score +=1
        print(score)
    # print(shoot_list)


    # Draw all the spites
    all_sprites_list.draw(screen)

    # Limit to 60 frames per second
    clock.tick(60)
    text = "FPS: {0:.2f}   Score: {1:2}   Playtime: {1:.2f} Secs".format(clock.get_fps(),score,playtime)
    pygame.display.set_caption(text)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
pygame.quit()