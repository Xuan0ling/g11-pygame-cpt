##
#author: Yuxuan Pan, Oscar Wang
#last edited 10th Nov 2021
# Pygame base template for opening a window - MVC version
# Simpson College Computer Science
# http://programarcadegames.com/
#

## Pygame setup
import pygame
import time
import random

pygame.init()
bottom_panel = 150
screen_width = 800
screen_height = 400 + bottom_panel

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("That time I crossed over to the other world with 80s records and became a famous musician in the other world")


#define fonts
font = pygame.font.SysFont('Times New Roman', 26)


## MODEL - Data use in system
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (127, 127, 127)
MAGENTA = (255, 51, 143)
CYAN = (0, 255, 255)

Color = (0,0,0)
textdarkcolor =(16,36,65)
textlightcolor =(37,79,143)


width = screen.get_width()
height = screen.get_height()
mouse = pygame.mouse.get_pos()

#imports pictures on relative paths
bg_location = 'img/Background/background.png'
bg = pygame.image.load(bg_location)

longbg_location = 'img/Background/longbackground.png'
longbg = pygame.image.load(longbg_location)

pn_location = 'img/icons/panel.png'
pn = pygame.image.load(pn_location)

box_location = 'img/icons/box.png'
box = pygame.image.load(box_location)
box = pygame.transform.scale(box, (175,50))

mc_location = 'img/maincharater.png'
mc = pygame.image.load(mc_location)
mc = pygame.transform.scale(mc, (mc.get_width() * 2, mc.get_height() * 2))

Slime_location = 'img/slime.png'
sl = pygame.image.load(Slime_location)
sl = pygame.transform.scale(sl, (sl.get_width(), sl.get_height()))

sword_location = 'img/icons/sword.png'
sd = pygame.image.load(sword_location)

victory_location = 'img/icons/victory.png'
vc = pygame.image.load(victory_location)

defeat_location = 'img/icons/defeat.png'
df = pygame.image.load(defeat_location)

potion_location = 'img/icons/potion.png'
pt = pygame.image.load(potion_location)



#sound
#BGM
pygame.mixer.init()

pygame.mixer.music.load("sound/stts.mp3")
pygame.mixer.music.play(loops=-1)
pygame.mixer.music.set_volume(0.1)

#Sound effects

sound_mainhurt = pygame.mixer.Sound("sound/mainhurt.mp3")
sound_slimehurt = pygame.mixer.Sound("sound/slimehurt.mp3")
sound_potion = pygame.mixer.Sound("sound/potion.mp3")


#create function for drawing text
def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))

#function for drawing panel
def draw_panel():
  #draw panel rectangle
  screen.blit(pn, (0, screen_height - bottom_panel))
  draw_text(f'{Anna.name} HP: {Anna.hp}', font, CYAN, 100, screen_height - bottom_panel + 10)
  for count, i in enumerate(Slime_list):
    #show name and health
    draw_text(f'{i.name} HP: {i.hp}', font, CYAN, 550, (screen_height - bottom_panel + 10) + count * 60)

#class menu
class Menu:
  def __init__(self):
    self.color = (255,255,255)

    # light shade of the button
    self.color_light = (255,221,192)

    # dark shade of the button
    self.color_dark = (255,184,144)

    # stores the width of the
    # screen into a variable
    self.pos = [310, 100]
    

    self.mouse = pygame.mouse.get_pos()

  def drawbutton(self,text,xadd,yadd):

    x = self.pos[0]
    y = self.pos[1]
    
    mouse = self.mouse
    smallfont = pygame.font.SysFont('Corbel',35)
    textStart1 = smallfont.render(text, True, textlightcolor)
    textStart2 = smallfont.render(text, True, textdarkcolor)
    if x <= mouse[0] <= x+175  and y <= mouse[1] <= y+50 :
      screen.blit(box, (x,y))
      screen.blit(textStart1, [x+xadd, y+yadd])
      

    else:
      
      screen.blit(box, (x,y))
      screen.blit(textStart2, [x+xadd, y+yadd])
      
  def drawlongbg (self):
    screen.blit(longbg, (longbgx,75))
    
    
  def drawMenu1(self,screen):
    font = pygame.font.SysFont('Calibri', 20, True, True)
    screen.blit(bg, (0,75))
    #fonts and render text
    text1 = font.render("Welcome to the game of 'That time I crossed over to the other ", True, CYAN)
    text2 = font.render("world with 80s records and became a", True, CYAN)
    text3 = font.render("famous musician in the other world.", True, CYAN)
    text4 = font.render('click on next on the screen to proceed.', True, CYAN)
    screen.blit(text1, [100, 180])
    screen.blit(text2, [200, 220])
    screen.blit(text3, [100, 260])
    screen.blit(text4, [200, 300])
    
  def drawMenu2(self,screen):
    font = pygame.font.SysFont('Calibri', 20, True, True)
    screen.blit(bg, (0,75))
    
    text1 = font.render("Anna is a bass player.", True, CYAN)
    text2 = font.render("One day she was practicing bass in her room", True, CYAN)
    text3 = font.render("and listening to her favourite music.", True, CYAN)
    text4 = font.render("She was practicing with all her concentration. ", True, CYAN)
    text5 = font.render("However, something weird happened. ", True, CYAN)
    screen.blit(text1, [100, 180])
    screen.blit(text2, [200, 220])
    screen.blit(text3, [100, 260])
    screen.blit(text4, [200, 300])
    screen.blit(text5, [100, 340])


  def drawMenu3(self,screen):
    font = pygame.font.SysFont('Calibri', 22, False, True)
    screen.blit(bg, (0,75))
    
    text1 = font.render("A big, oval-shaped, dark teleporter appeared in the air,", True, CYAN)
    text2 = font.render("dragging and sucking everything around it.", True, CYAN)
    text3 = font.render("Anna fell into it and travelled to another world.", True, CYAN)
    screen.blit(text1, [100, 180])
    screen.blit(text2, [200, 220])
    screen.blit(text3, [100, 260])


  def drawMenu4(self,screen):
    font = pygame.font.SysFont('Calibri', 22, False, True)
    screen.blit(bg, (0,75))
    
    text1 = font.render("As the player, to help her going back to the main world,", True, CYAN)
    text2 = font.render("you must control Anna,", True, CYAN)
    text3 = font.render("by moving your mouse cursor on the slime monster and attack it.", True, CYAN)
    text4 = font.render("Every round you can either choose to heal or attack,", True, CYAN)
    text5 = font.render("try not to get killed by the monster and win.", True, CYAN)
    screen.blit(text1, [100, 180])
    screen.blit(text1, [100, 180])
    screen.blit(text2, [200, 220])
    screen.blit(text3, [100, 260])
    screen.blit(text4, [200, 300])
    screen.blit(text5, [100, 340])
    

  
  
#class fighter
class Fighter():
  def __init__(self, x, y, name, max_hp, strength):
    self.name = name
    self.max_hp = max_hp
    self.hp = max_hp
    self.strength = strength


#define draw
def draw(image, x, y):
  screen.blit(image,(x, y))
    
#class health bar
class HealthBar():
  def __init__(self, x, y, hp, max_hp):
    self.x = x
    self.y = y
    self.hp = hp
    self.max_hp = max_hp

  def draw(self, hp):
    #update with new health
    self.hp = hp
    #calculate health ratio
    ratio = self.hp / self.max_hp
    pygame.draw.rect(screen, RED, (self.x, self.y, 150, 20))
    pygame.draw.rect(screen, GREEN, (self.x, self.y, 150 * ratio, 20))



# Loop until the user clicks the close button.
donemenu = False
donegame = False
done = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

#global variables
menu = 0
longbgdone = False
longbgx = 0
longbg_speedX = 2





## menu Loop
while not donemenu:
  drawmenu = Menu()
  
  ## CONTROL
  # Check for events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      donemenu = True
    if event.type == pygame.MOUSEBUTTONDOWN:
      if 310 <= mouse[0] <= 310 + 175 and 100 <= mouse[1] <= 100 + 50:
        menu += 1
      if menu == 5:
        donemenu = True

  if (longbgx < -690):
      longbgx = 0  
  if not longbgdone:
    longbgx = longbgx - longbg_speedX
  
                   
  screen.fill(Color)     

  mouse = pygame.mouse.get_pos()

  # Draw
  drawmenu.drawlongbg()

  drawmenu.drawbutton('s t a r t', 42.5, 10)

  if (menu == 1):
    drawmenu.drawMenu1(screen)
    drawmenu.drawbutton('n e x t', 47.5, 10)

  elif (menu == 2):
    drawmenu.drawMenu2(screen)
    drawmenu.drawbutton('n e x t', 47.5, 10)

  elif (menu == 3):
    drawmenu.drawMenu3(screen)
    drawmenu.drawbutton('n e x t', 47.5, 10)

  elif (menu == 4):
    drawmenu.drawMenu4(screen)
    drawmenu.drawbutton('n e x t', 47.5, 10)

  

  # Shadow effect

  # Update Screen
  pygame.display.flip()
  clock.tick(60)

#variables on characters
Anna = Fighter(200, 260, 'Anna', 20, 5)
Slime1 = Fighter(550, 270, 'Slime', 15, 5)
Slime2 = Fighter(700, 270, 'Slime', 15, 5)
num_potion = 1


Slime_list = []
Slime_list.append(Slime1)
Slime_list.append(Slime2)


Anna_health_bar = HealthBar(100, screen_height - bottom_panel + 40, Anna.hp, Anna.max_hp)
Slime1_health_bar = HealthBar(550, screen_height - bottom_panel + 40, Slime1.hp, Slime1.max_hp)
Slime2_health_bar = HealthBar(550, screen_height - bottom_panel + 100, Slime2.hp, Slime2.max_hp)


mx1 = Slime1.max_hp
mx2 = Slime2.max_hp

#main game loop
print("stage 2")
while not donegame:
  
  mouse = pygame.mouse.get_pos()

  
  rand1 = random.randint(-3, 4)
  randpotion = random.randint(-3,3)
  ## CONTROL
  # Check for events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      donegame = True

    if event.type == pygame.MOUSEBUTTONDOWN:
      if Slime1.hp > 0:
        if 550 <= mouse[0] <= 550 + 75 and 285 <= mouse[1] <= 285 + 75:
          Slime1.hp -= Anna.strength + rand1
          print ("You dealt", str(Anna.strength + rand1), "points of damage to Slime 1")
        
          sound_slimehurt.play()
          



      if Slime2.hp > 0:
        if 650 <= mouse[0] <= 650 + 75 and 285 <= mouse[1] <= 285 + 75:
          Slime2.hp -= Anna.strength + rand1
          print ("You dealt ", str(Anna.strength + rand1), " points of damage to Slime 2")
          
          sound_slimehurt.play()

    if num_potion == 1:
      if event.type == pygame.MOUSEBUTTONDOWN:
        if 300 <= mouse[0] <= 300 + 64 and 430 <= mouse[1] <= 430 + 64:
          Anna.hp += 10 + randpotion
          print("You have used the potion to restore", str(10 + randpotion),"points of blood")
          sound_potion.play()
          num_potion -= 1


          
        

        
  if Anna.hp <= 0:
    donegame = True
  if Slime1.hp <= 0 and Slime2.hp <= 0:
    donegame = True


  if Anna.hp < 0:
    Anna.hp = 0
  if Slime1.hp < 0:
    Slime1.hp = 0
    print("You have destroyed a Slime")
  if Slime2.hp < 0:
    Slime2.hp = 0
    print("You have destroyed a Slime")


   

  # Draw
  draw_panel()
  screen.blit(bg, (0,0))


  if num_potion == 1:
    #draw potion
    draw(pt,300,430)

  #maincaracter()
  if Anna.hp > Anna.max_hp:
    Anna.hp = Anna.max_hp
  if Anna.hp > 0:
    draw(mc, 0, 210)
  if Slime1.hp > 0:
    draw(sl, 550, 285)
  if Slime2.hp > 0:
    draw(sl, 650, 285)
    








  Anna_health_bar.draw(Anna.hp)
  Slime1_health_bar.draw(Slime1.hp)
  Slime2_health_bar.draw(Slime2.hp)





  if 550 <= mouse[0] <= 550 + 75 and 285 <= mouse[1] <= 285 + 75:
     #hide mouse
    pygame.mouse.set_visible(False)
    #show sword in place of mouse cursor
    screen.blit(sd, mouse)      

  elif 650 <= mouse[0] <= 650 + 75 and 285 <= mouse[1] <= 285 + 75:
    #hide mouse
    pygame.mouse.set_visible(False)
    #show sword in place of mouse cursor
    screen.blit(sd, mouse)
  

  else:
    pygame.mouse.set_visible(True)




      
  
  

  # Shadow effect
  


  # Update Screen
  pygame.display.flip()
  clock.tick(60)

  rand2 = random.randint(-3, 3)
  if Slime1.hp < mx1 and Slime1.hp > 0:
    time.sleep(0.5)
    
    Anna.hp -= Slime1.strength + rand2
    print ("You have taken", str(Slime1.strength + rand2), "points of damage")
    mx1 = Slime1.hp
    sound_mainhurt.play()

  if Slime2.hp < mx2 and Slime2.hp > 0:
    time.sleep(0.5)
    
    Anna.hp -= Slime2.strength + rand2
    print ("You have taken", str(Slime2.strength + rand2), "points of damage")
    mx2 = Slime2.hp
    sound_mainhurt.play()

  if Anna.hp == 0:
    #WL = Win or Lose
    WL = 0
  else:
    WL = 1




while not done:
  pygame.mouse.set_visible(True)
  mouse = pygame.mouse.get_pos()
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True
    if event.type == pygame.MOUSEBUTTONDOWN:
      clicked = True
    else:
      clicked = False


  mouse = pygame.mouse.get_pos()
  screen.fill(Color)
  screen.blit(bg, (0,0))
  screen.blit(pn, (0, screen_height - bottom_panel))


  

  if WL == 1:
    
    draw(vc,260,100)

    
  elif WL == 0:
    
    draw(df,280,100)
    





  # Update Screen
  pygame.display.flip()
  clock.tick(60)


# Close the window and quit
pygame.quit()