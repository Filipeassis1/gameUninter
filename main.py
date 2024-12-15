import pygame

print('Start Setup')
pygame.init()
window = pygame.display.set_mode(size=(600, 480))
print('End Setup')

print('Loop Start')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('Quitting..')
            pygame.quit()  #close
            quit()  #end
