#!/usr/bin/python
#-*- coding: utf-8 -*-
import pygame
from code.const import WIN_HEIGHT, WIN_WIDTH , MAIN_COLOR_FONT, MENU_SELECTION
from pygame import Surface, Rect

class Menu:

  def __init__(self, window):
    self.window = window
    self.surf = pygame.image.load('./Assets/bgGame.png')
    self.retangulo = self.surf.get_rect(left=0, top=0)

  def run(self,):
    pygame.mixer_music.load('./Assets/menuMusic.mp3')
    pygame.mixer_music.play(-1)
    while True: 
      self.window.blit(source=self.surf, dest=self.retangulo)
      self.menu_text(50, "Battle", MAIN_COLOR_FONT , ((WIN_WIDTH /2),70 ))
      self.menu_text(50, "Ship", MAIN_COLOR_FONT, ((WIN_WIDTH /2),120 ))

      for i in range(len(MENU_SELECTION)):
          self.menu_text(20, MENU_SELECTION[i], MAIN_COLOR_FONT, ((WIN_WIDTH /2),180 + 32 * i ))


      pygame.display.flip() 
      
      for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  #close
                    quit()  #end

  def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: pygame.font.SysFont = pygame.font.SysFont(name="Arial Black", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
