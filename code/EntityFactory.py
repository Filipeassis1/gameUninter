#!/usr/bin/python
#-*- coding: utf-8 -*-

from code.Background import Background 

class EntityFactory:

  @staticmethod
  def get_entity(entity_name: str, position=(0,0)):
      match entity_name:
            case 'f1':
              list_bg = []
              for i in range(2):
                list_bg.append(Background(f'f1bg{i}'))
              return list_bg