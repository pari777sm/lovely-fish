import pgzrun
import random
import os
import pgzhelper

os.environ['SDL_VIDEO_CENTERED'] = '1'

WIDTH = 1000
HEIGHT = 700
TITLE = 'lovly fish'

background2 = Actor('background_one1', (500,350))
fish = Actor('happy_l', (550,350))
seacreatures_list =('octopus', 'crab', 'starfish', 'seahorse', 'whale', 'jellyfish', 'dolphin', 'ballonfish', 'turtle', 'shark_r')
seacreature = Actor(random.choice(seacreatures_list))
waste_list =['bottel1', 'bottel2', 'can', 'paper','khaar','glasses','apple', 'banana' ,'slipper','watermelon' ]
waste = Actor(random.choice(waste_list))
play_button = Actor('start_button', (500,500))
exit_button = Actor ('exit_button25', (900,650))
setting_button =Actor('setting', (100,650))
game_over = Actor('game_over_pa', (-500,350))

yes_button = Actor ('yes_button' , (-500,500))
no_button = Actor ('no_button' , (-500,500))
exit_confirm = Actor('exit_confirm' , (-500,350))
yes_key_button = Actor ('yes_key_2' , (-500,406))
no_key_button = Actor ('no_key_2' , (-500,406))
confirm_close = Actor ('close_1' , (-600,254))
sound_button = Actor ('sound_on', (30,660))
position = 0,0


score = 0
fish_speed = 0
waste_speed = 0
seacreature_speed = 0
heart = 2
game = False
sound_sign = True

seacreature.x = -100
waste.y = -100

waste.x = random.randrange(50, 950 , 25)
seacreature.y = random.randrange(200, 600 , 20)


def update() :
     global background2, fish , fish_speed, waste, waste_speed, score,seacreature, seacreature_speed,heart, game, game_over, yes_button, no_button,exit_button, yes_key_button,sound_button
     
     # ----------------- waste moveand sound ----------
     waste.y += waste_speed
     if waste.y == 150  and sound_sign == True:
          sounds.water_splash.play()
     seacreature.x += seacreature_speed
   

     if waste.y >= 700:
          waste.y=0
          waste.image = random.choice(waste_list)
          waste.x = random.randrange(50, 950 , 25)
          
          
     # -------------------- fish move ----------------
     if keyboard.left   and fish.x >=140 and game == True:
          fish.x -= fish_speed
          fish.image = 'happy_l'
                         
     if keyboard.right and fish.x <=860 and game == True:
          fish.x += fish_speed
          fish.image = 'happy_r'

     if keyboard.up   and fish.y >=190 and game == True:
          fish.y -= fish_speed
          
     if keyboard.down   and fish.y <=635 and game == True:
          fish.y += fish_speed
     # ----------- restart game after shark attack -----
     if keyboard.space :
               
          if score > 0 or heart > 0 :
               game = True
               fish_speed = 4
               waste_speed = 3
               seacreature_speed = 4
               play_button.x = -500
               
               if fish.image == 'dead_r':
                    fish.image = 'happy_r'
               elif fish.image == 'dead_l' :
                    fish.image = 'happy_l'
          else :
               game_over.x = 500

     # -------------- negative score after eating waste -----
     if fish.colliderect(waste):
          score -= 1

          if score <= 0 and heart > 0 :
               score += 5
               heart -= 1
          elif score < 0 and heart == 0:
               game = False
          

          waste.y=0
          waste.image = random.choice(waste_list)
          waste.x = random.randrange(50, 950 , 25)

     if seacreature.x >= 1100 :
          seacreature.x = 0
          seacreature.image = random.choice(seacreatures_list)  
          seacreature.y = random.randrange(150, 650 , 25)



     if fish.colliderect(seacreature) :
          if seacreature.image == 'shark_l' or seacreature.image =='shark_r' and sound_sign == True:
               sounds.scream3.play()
               game = False

               if heart > 0:
                    heart -=1
               else :
                    score = 0
                    game_over.x = 500
                    # replay_button.x = 500
                    yes_button.x = 300
                    no_button.x = 700

               seacreature.x = 0
               seacreature.image = random.choice(seacreatures_list)  
               seacreature.y = random.randrange(150, 650 , 25)
               
               if fish.image == 'happy_r':
                    fish.image = 'dead_r'
                    fish_speed = 0
                    waste_speed = 0
                    seacreature_speed = 0

               else :
                    fish.image = 'dead_l'
                    
                    fish_speed = 0
                    waste_speed= 0
                    seacreature_speed = 0
          else :
               score +=1
               if score > 5 :
                    score = 0
                    heart +=1
               seacreature.x = 0
               seacreature.image = random.choice(seacreatures_list)  
               seacreature.y = random.randrange(150, 650 , 25)   
     if heart <= 0 and score == 0 :
          game= False
          fish_speed = 0
          waste_speed = 0
          seacreature_speed = 0
          game_over.x = 500
          # replay_button.x = 500
          yes_button.x = 300
          no_button.x = 700

             
     
def on_mouse_up(pos) :
     global game, fish_speed, waste_speed, seacreature_speed, heart, score, confirm_close,no_key_button, yes_key_button,sound_sign
     if play_button.collidepoint(pos):
          game = True
          fish_speed = 4
          waste_speed = 3
          seacreature_speed = 4
          play_button.x = -500

     # if replay_button.collidepoint(pos):
     if yes_button.collidepoint(pos):
          game = True
          fish_speed = 4
          waste_speed = 3
          seacreature_speed = 4          
          heart = 2
          score = 0
          # replay_button.x = -500
          yes_button.x = -500
          no_button.x = -500
          game_over.x = -500
          if fish.image == 'dead_r':
               fish.image = 'happy_r'
          elif fish.image == 'dead_l':
               fish.image = 'happy_l'
     elif no_button.collidepoint(pos):
          exit_confirm.x = 500
          yes_key_button.x =405
          no_key_button.x =595
          confirm_close.x = 750
          

     if confirm_close.collidepoint(pos):
          exit_confirm.x = -500
          yes_key_button.x = -500
          no_key_button.x = -500
          confirm_close.x = -500     
     elif yes_key_button.collidepoint(pos):
          exit()
     elif no_key_button.collidepoint(pos) :
          exit_confirm.x = -500
          yes_key_button.x = -500
          no_key_button.x = -500
          confirm_close.x = -500
          fish_speed = 4
          waste_speed = 3
          seacreature_speed = 4


     if exit_button.collidepoint(pos):
          exit_confirm.x = 500
          yes_key_button.x =405
          no_key_button.x =595
          confirm_close.x = 750
          waste_speed = 0
          seacreature_speed = 0
          fish_speed = 0

     if sound_button.collidepoint(pos):
          if sound_button.image == 'sound_on' :
               sound_button.image = 'sound_off'
               sound_sign = False
          elif sound_button.image == 'sound_off' :
               sound_button.image = 'sound_on'
               sound_sign = True


def draw() :
     global background2, fish, waste , waste_speed , score, seacreature,game_over, play_button,yes_button, no_button, exit_button, yes_key_button, no_key_button, confirm_close,sound_button

     background2.draw()
     waste.draw()
     seacreature.draw()
     fish.draw()
     game_over.draw()
     play_button.draw()
     # replay_button.draw()
     yes_button.draw()
     no_button.draw()
     exit_button.draw()
     exit_confirm.draw()
     yes_key_button.draw()
     no_key_button.draw()
     confirm_close.draw()
     sound_button.draw()
# ..........................score...................................
     screen.draw.text(f"score = {score}", fontsize = 25, color = 'black',background = 'gray',shadow = (-1,-1), pos =(0,0))
     screen.draw.text(f"heart = {heart}", fontsize = 25, color = 'black',background = 'gray',shadow = (-1,-1), pos =(0,20))
     

def on_mouse_move(pos) :
     if exit_button.collidepoint(pos) :
          exit_button.image = 'exit_button50'
     else :
          exit_button.image = 'exit_button25'

     
     if yes_key_button.collidepoint(pos) :
          yes_key_button.image = 'yes_key_1'
     else :
          yes_key_button.image = 'yes_key_2'


     if no_key_button.collidepoint(pos) :
          no_key_button.image = 'no_key_1'
     else :
          no_key_button.image = 'no_key_2'





pgzrun.go()