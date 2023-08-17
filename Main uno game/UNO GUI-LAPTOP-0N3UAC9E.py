import pygame
import time
from deck_of_cards import *
from deck_of_cards import Deck


pygame.init() #initialises pygame
x = 800
y = 600
white = (255,255,255)
black = (0,0,0)
green = (0,255,0)
red = (255,0,0)
blue = (0,0,255)
orange = (255,165,0)
mouseposition = pygame.mouse.get_pos()
'''deck1 = Deck()
deck1.shuffle()
Player1 = Player('Player1')
AI = Player('AI')
Player1.draw(deck1, 10)
Player1.showhand()
AI.draw(deck1, 10)
AI.showhand()'''


    
def text_objects(text, font): #this function takes the rectangle and puts it over the whole of the text so it can be moved as one
    textSurface = font.render(text, True, black) 
    return textSurface, textSurface.get_rect()

def gametext_display(text,divby_x,divby_y,fontsize):
    gametext = pygame.font.Font('freesansbold.ttf', fontsize)
    TextSurf,TextRect = text_objects(text, gametext)
    TextRect.center = ((x/divby_x) ,(y/divby_y))
    uno_window.blit(TextSurf, TextRect)

def deal_deck_selected():
        deck = Deck()
        deck.shuffle()
        Player1 = Player("Player1")
        Player1.draw(deck, 10)
        Player1.showhand()
        Computer = AI('Computer')
        Computer.draw(deck, 10)
        Computer.showhand()
    

def start_game_s():
    gametext_display('Press the ENTER key once to deal the UNO cards', 2, 12, 15)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                deal_deck_selected()
                retrieve_uno_card_image()
                    

def deck_image(width,height):
    pos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global deckImg
    deckImg = pygame.image.load('deck_image.png')
    uno_window.blit(deckImg, (width,height))

        

def background_image(x,y):
    global background
    background = pygame.image.load('background.jpg').convert()
    uno_window.blit(background, (x,y))

def add_screen():
    global uno_window
    uno_window = pygame.display.set_mode((x, y)) #creates a window with specified resolution (x,y)
    pygame.display.set_caption('Python UNO') #sets window title
    fps = pygame.time.Clock() #creates a clock that counts fps
    fps.tick(60)
    uno_window.fill(white)
    bwidth= 800
    bheight = 800
    background_image(x,y)
    pygame.display.update()
    
def retrieve_uno_card_image():
    for card in Player1.hand:
        displayimage(cardImg,12,10)
        
    
    

def displayimage(image_name,div_iwidth, div_iheight):
    iwidth = x/div_iwidth
    iheight = y/div_iheight
    uno_window.blit(image_name, (iwidth,iheight))
    pygame.display.update()
    

def turnswitcher():
    pass
        
def createbutton(button_name,x1,y2,w1,h2,inactive_colour,active_colour,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x1+w1 > mouse[0] > x1 and y2+h2 > mouse[1] > y2:
        pygame.draw.rect(uno_window, active_colour,(x1,y2,w1,h2))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(uno_window, inactive_colour,(x1,y2,w1,h2))
        
    button_font_size = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(button_name, button_font_size)
    textRect.center = ( (x1+(w1/2)), (y2+(h2/2)) )
    uno_window.blit(textSurf, textRect)

def startup_menu():
    add_screen()
    startup = True
    while startup:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        uno_window.fill(white)
        gametext_display('Welcome to UNO',2,2,50)
        singeplayer_button = createbutton('SINGLEPLAYER',150,450,100,50,green,orange,singleplayer)
        mutliplayer_button = createbutton('MULTILPLAYER',370,450,100,50,blue,orange,multiplayer)
        quit_button = createbutton('QUIT',550,450,100,50,red,orange,quitgame)
        pygame.display.update()

def quitgame():
    pygame.quit()
    quit()

def singleplayer():
    add_screen()
    play = True
    while play:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        uno_window.fill(white)
        gametext_display('Player1', 12, 12, 15)
        gametext_display('Computer', 1.2, 12, 15)
        width = (x/2.5) #location on screen
        height = (y/3) #location on screen
        start_game_s()
        deck_image(width,height)
        pygame.display.update()
        start_game_s()

def multiplayer():
    add_screen()
    startup = True
    while startup:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        uno_window.fill(white)
        multiplayer_local_button = createbutton('Multiplayer Local',250,450,100,50,blue,orange,multiplayer_local)
        multiplayer_online_button = createbutton('Multiplayer Online',500,450,100,50,blue,orange,multiplayer_online)
        pygame.display.update()

def multiplayer_local():
    pass

def multiplayer_online():
    pass

def uno_gui():
    startup_menu()

uno_gui()
#cards = uno_card_images_dict()
#print(cards)
#uno_card_images_dict()
        







