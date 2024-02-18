import pgzrun
# from pgzhelper import *
import os
import random
import pyautogui



os.environ['SDL_VIDEO_CENTERED'] = '1'


WIDTH = 450
HEIGHT = 450
TITLE = 'lovly fish'



background_menu = Actor('background_menu', (225,225))
play_button = Actor('play_button50' , (-60,55))
setting_button = Actor('setting_button50', (-100, 115))   
about_game = Actor('about_game50' , (-160 , 175)) 
shop_button = Actor('shop_button50' , (-60 , 235))
rulls_button = Actor('rulls_button50', (-80,295))
exit_button = Actor('exit_button50' ,(-70 , 355))
position = 0,0
button_speed = 5
button_delay = 20
menu = True
game_1 = False

def update() :
   if menu :
      if play_button.x <=150   :
         play_button.x += button_speed
      if setting_button.x <=150 and  play_button.x >=button_delay  :
         setting_button.x += button_speed
      if about_game.x <=150  and setting_button.x >= button_delay :
         about_game.x += button_speed
      if shop_button.x <=150  and about_game.x >= button_delay :
         shop_button.x += button_speed
      if rulls_button.x <=150  and shop_button.x >= button_delay :
         rulls_button.x += button_speed
      if exit_button.x <=150  and rulls_button.x >= button_delay :
         exit_button.x += button_speed
               


def draw() :
   global background_menu
   if menu :
      background_menu.draw()
      play_button.draw()
      setting_button.draw() 
      about_game.draw()
      shop_button.draw()
      rulls_button.draw()
      exit_button.draw()
   #  background_menu()
   #   if exit_button :
   #   exit_panel.draw()
   #   yes_button.draw()
   #   no_button.draw()
   if game_1 :
      screen.clear()
      play_button.draw()

# def on_mouse_down(pos) :
#    global exit_button :
# if exit_button.collidepoint() : 
#    exit_button =True
#    button_out_of_screen()
   
   

def on_mouse_move(pos) :
   if play_button.collidepoint(pos) :
      play_button.image = 'play_button25'
   else :
      play_button.image = 'play_button50'
   if setting_button.collidepoint(pos) :
      setting_button.image = 'setting_button25'
   else :
      setting_button.image = 'setting_button50'
   if about_game.collidepoint(pos) :
      about_game.image = 'about_game25'
   else :
      about_game.image = 'about_game50'
   if shop_button.collidepoint(pos) :
      shop_button.image = 'shop_button25'
   else :
      shop_button.image = 'shop_button50'
   if rulls_button.collidepoint(pos) :
      rulls_button.image = 'rulls_button25'
   else :
      rulls_button.image = 'rulls_button50'   
   if exit_button.collidepoint(pos) :
      exit_button.image = 'exit_button25'
   else :
      exit_button.image = 'exit_button50'    



def on_mouse_up(pos) :
   global menu, game_1
   if exit_button.collidepoint(pos):
      button=pyautogui.confirm(text='Do you want to EXIT?', buttons= ['yes','no'])
      if button == 'yes' :
         exit()
      
   if play_button.collidepoint(pos) :
      print('s')
      menu = False
      game_1 = True




pgzrun.go()