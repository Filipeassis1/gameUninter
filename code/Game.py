#!/usr/bin/python
#-*- coding: utf-8 -*-
import pygame
from code.const import WIN_HEIGHT, WIN_WIDTH, MENU_SELECTION 
from code.Menu import Menu 
from code.Level import Level 


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    
    def run(self):

        while True:
            menu = Menu(self.window)
            score = Score(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_SELECTION[0], MENU_SELECTION[1], MENU_SELECTION[2]]:
                level = Level(self.window, 'New game', menu_return)
                level_return = level.run()
            elif menu_return == MENU_SELECTION[4]:
                pygame.quit()  #close
                quit()  #end
            else:
                pass
