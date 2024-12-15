#!/usr/bin/python
#-*- coding: utf-8 -*-
import pygame
from code.const import WIN_HEIGHT, WIN_WIDTH
from code.Menu import Menu

def main():
    pygame.init()
    window = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))  # Ajuste conforme suas constantes
    menu = Menu(window)
    menu.run()

if __name__ == "__main__":
    main()