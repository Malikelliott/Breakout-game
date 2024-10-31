from turtledemo.nim import SCREENWIDTH, SCREENHEIGHT

import pygame
import self
from pygame import mixer

#Initialize the game
pygame.init()

#create screen
SCREENWIDTH = 900
SCREENHEIGHT = int(SCREENWIDTH * 0.8)
screen = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))



#Title
pygame.display.set_caption("Breakout")

#STATE
state = 0

#Text
font = pygame.font.Font('freesansbold.ttf', 32)
fontSmaller = pygame.font.Font('freesansbold.ttf', 24)

#Sounds
clicked_sound = mixer.Sound('mouse-click-sound-233951.mp3')
applause_sound = mixer.Sound('short-crowd-cheer-236776.mp3')
boo_sound = mixer.Sound('aww-8277.mp3')
clack_sound = mixer.Sound('clack-85854.mp3')

#Scores
score = 0
level = 1

#Buttons
brick_img = pygame.image.load('brick.jpg')
brick = pygame.transform.scale(brick_img,(450,50))
one_player_game = pygame.Rect((0, 250, SCREENWIDTH, 50))
button1txt = font.render("START GAME" ,True,(0,0,0))

help_button = pygame.Rect((0, 350, SCREENWIDTH, 50))
helptxt = font.render("HOW TO PLAY" ,True,(0,0,0))
helpInfo1 = fontSmaller.render("- Move your character left and right with A/D or LEFT/RIGHT keys.",True,(0,0,0))
helpInfo2 = fontSmaller.render("- dont drop the ball.",True,(0,0,0))
helpInfo3 = fontSmaller.render( "- different coloured bricks require different hit amounts." ,True,(0,0,0))
helpInfo4 = fontSmaller.render( "- vtbttr." ,True,(0,0,0))

options = pygame.Rect((0, 450, SCREENWIDTH, 50))
optionstxt = font.render("OPTIONS" ,True,(0,0,0))
optInfo1 = fontSmaller.render("Powerups: ",True,(0,0,0))


credits = pygame.Rect((0, 550, SCREENWIDTH, 50))
credtxt = font.render("CREDITS" ,True,(0,0,0))
credInfo1 = fontSmaller.render("Created By: Me",True,(0,0,0))
credInfo2 = fontSmaller.render("Artwork By: Me & various sources",True,(0,0,0))
credInfo3 = fontSmaller.render("Programming By: Me",True,(0,0,0))
credInfo4 = fontSmaller.render("Music & Sounds By: Pixaby.com &",True,(0,0,0))
credInfo5 = fontSmaller.render("Project Created: October 21st, 2024",True,(0,0,0))


back = pygame.Rect((0, SCREENHEIGHT - 100, SCREENWIDTH, 50))
backtxt = font.render("BACK" ,True,(0,0,0))

quit_button = pygame.Rect((SCREENWIDTH - 110, 10, 100, 50))
quittxt = font.render("QUIT" ,True,(0,0,0))

#Player
player = pygame.Rect((SCREENWIDTH/2 - 60, SCREENHEIGHT -50, 100, 30))


#Puck
puck_size = 50
puckImg = pygame.image.load('puck.png')
puckImg = pygame.transform.scale(puckImg,(puck_size,puck_size)) #resize puck
puckXSpeed = -0.05
puckYSpeed = -0.1
puckX = player.x
puckY = player.y
def place_puck(x,y):
    screen.blit(puckImg, (puckX,puckY))



def show_score(x,y):
    score_text = font.render("Score: " + str(score),True,(200,0,0))
    screen.blit(score_text, (x,y))

def show_level(x,y):
    level_text = font.render("Level: " + str(level), True, (0, 0, 200))
    screen.blit(level_text, (x, y))


#Surface
#surface_image = pygame.image.load('').convert()
#surface_image = pygame.transform.scale(surface_image, (SCREENWIDTH, SCREENHEIGHT))


                               #### RUNNING CODE STARTS HERE ####

run = True
while run:

    mouse_pos = pygame.mouse.get_pos()

    if state == 0: #main menu
        screen.fill((0, 0, 255))  # screen resets each time
        pygame.draw.rect(screen, (255, 0, 0), one_player_game)
        screen.blit(button1txt, (15, 260))
        #pygame.draw.rect(screen, (0, 255, 255), two_player_game)
        #screen.blit(button2txt, (15, 260))
        pygame.draw.rect(screen, (0, 255, 0), help_button)
        screen.blit(helptxt, (15, 360))
        pygame.draw.rect(screen, (255, 255, 0), options)
        screen.blit(optionstxt, (15, 460))
        pygame.draw.rect(screen, (128, 0, 255), credits)
        screen.blit(credtxt, (15, 560))

        puckXSpeed = -0.03
        puckYSpeed = -0.1
        puckX = player.x
        puckY = player.y -80
        p1_score = 0
        p2_score = 0

        if one_player_game.collidepoint(mouse_pos):
            #one_player_game.Color(100,0,0)
            if pygame.mouse.get_pressed()[0] == 1:
                clicked_sound.play()
                state = 1
                p2_is_human = False



        if help_button.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1:
                clicked_sound.play()
                state = 2

        if options.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1:
                clicked_sound.play()
                state = 3

        if credits.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1:
                clicked_sound.play()
                state = 4

    elif state == 1: #The game
        #Load the players, goal and puck
        screen.fill((0, 0, 64))
        pygame.draw.rect(screen, (255, 0, 0), player)
        #pygame.draw.rect(screen, (0, 0, 0), p1goal)
        #pygame.draw.rect(screen, (0, 0, 255), player2)
        #pygame.draw.rect(screen, (0, 0, 0), p2goal)
        #pygame.draw.rect(screen, (0, 0, 0), seperation)
        show_score(SCREENWIDTH/2 - 150,10)
        show_level(SCREENWIDTH/2 + 60, 10)
        pygame.draw.rect(screen, (70, 0, 70), quit_button)
        screen.blit(quittxt, (SCREENWIDTH - 100, 20))
        place_puck(puckX,puckY)

        #Puck Movement
        puckX += puckXSpeed
        puckY += puckYSpeed

        #puck hits player 1, it changes direction and goes faster
        if (((player.x - puckX < 25) & (player.x - puckX > -25)) &
                ((player.y - puckY < puck_size) & (player.y - puckY > -puck_size))):
            clack_sound.play()
            puckXSpeed *= -1.5



        if puckY < 0:
            clack_sound.play()
            puckYSpeed = 1.5


        #if ball hits edge
        if puckX < 10 :
            puckXSpeed = 1.5

        if puckX > SCREENWIDTH - 10 :
            puckXSpeed = -1.5


        key = pygame.key.get_pressed()

        #Player 1 controls
        if key[pygame.K_a]:
            player.move_ip(-1,0)
        elif key[pygame.K_d]:
            player.move_ip(1, 0)
        #elif key[pygame.K_w]:
            #player1.move_ip(0, -1)
       # elif key[pygame.K_s]:
            #player1.move_ip(0, 1)

        if player.x > SCREENWIDTH - 130:
            player.x = SCREENWIDTH - 130
        elif player.x < 30:
            player.x = 30

        if player.y > SCREENHEIGHT - 100:
            player.y = SCREENHEIGHT - 100
        elif player.y < 0:
            player.y = 0




        #Return to menu if quit button is pressed
        if quit_button.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1:
                clicked_sound.play()
                state = 0

    elif state == 2: #how to play
        screen.fill((70, 150, 0))
        pygame.draw.rect(screen, (255, 255, 255), back)
        screen.blit(backtxt, (15, SCREENHEIGHT - 95))
        screen.blit(helpInfo1, (15, 100))
        screen.blit(helpInfo2, (15, 150))
        screen.blit(helpInfo3, (15, 200))
        screen.blit(helpInfo4, (15, 250))


        if back.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1:
                clicked_sound.play()
                state = 0

    elif state == 3: #options
        screen.fill((70, 70, 70))
        pygame.draw.rect(screen, (255, 255, 255), back)
        screen.blit(backtxt, (15, SCREENHEIGHT - 95))
        screen.blit(optInfo1, (15, 100))


        if back.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1:
                clicked_sound.play()
                state = 0

    elif state == 4: #credits
        screen.fill((150, 70, 0))
        pygame.draw.rect(screen, (255, 255, 255), back)
        screen.blit(backtxt, (15, SCREENHEIGHT - 95))
        screen.blit(credInfo1, (15, 100))
        screen.blit(credInfo2, (15, 150))
        screen.blit(credInfo3, (15, 200))
        screen.blit(credInfo4, (15, 250))
        screen.blit(credInfo5, (15, 300))
        if back.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1:
                clicked_sound.play()
                state = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
