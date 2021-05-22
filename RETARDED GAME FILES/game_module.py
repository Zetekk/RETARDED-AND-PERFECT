import pygame, os
SIZESCREEN = WIDTH, HEIGHT = 1366, 740

LIGHTBLUE = pygame.color.THECOLORS['lightblue']
screen = pygame.display.set_mode(SIZESCREEN)

#print(pygame.color.THECOLORS)
path = os.path.join(os.pardir, 'images')
file_names = sorted(os.listdir(path))
file_names.remove('background.png')
BACKGROUND = pygame.image.load(os.path.join(path, 'background.png')).convert()
for file_name in file_names:
    image_name = file_name[:-4].upper()
    globals().__setitem__(image_name,
                          pygame.image.load(os.path.join(path, file_name)).convert_alpha(BACKGROUND))

#grafika postaci


#grafika platforma
