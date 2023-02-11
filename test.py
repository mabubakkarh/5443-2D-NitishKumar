# # import package pygame
# import pygame
 
# # initialize pygame
# pygame.init()
 
# # Form screen
# screen = pygame.display.set_mode()
# screen.fill((255, 255, 255))
 
# # get the default size
# x, y = screen.get_size()
 
# # quit pygame
# pygame.display.quit()
 
# # view size (width x height)
# print(x, y)

# # --------------------------------------------

# # import pygame, sys
# # from pygame.locals import *
# # import random

# # pygame.init()

# # # predefined colours
# # BLUE  = (0, 0, 255)
# # RED   = (255, 0, 0)
# # GREEN = (0, 255, 0)
# # BLACK = (0, 0, 0)
# # WHITE = (255, 255, 255)

# # # screen information


# # rect_Y = 0
# # SCREEN_MARGIN = 5
# # RECT_WIDTH = 50
# # RECT_HEIGHT = 50

# # # x, y = screen.get_size()
# # DISPLAYSURF = pygame.display.set_mode((250,250))
# # DISPLAYSURF.fill(WHITE)

# # rows, cols = (5, 5)
# # grid = [[0 for i in range(cols)] for j in range(rows)]


# # # for col in range(550,800,50):
# # #     for row in range(300,550,50):

# # for col in range(0,250,50):
# #     for row in range(0,250,50):
# #         object1 = pygame.Rect((col , row ,50, 50))
# #         pygame.draw.rect(DISPLAYSURF,BLACK,object1,4)
# # # for col in range(569,300,50):
# # #     for row in range(569,300,50):
# # #         object1 = pygame.Rect((col , row ,50, 50))
# # #         pygame.draw.rect(DISPLAYSURF,BLACK,object1,4)
    

# # while True: 
# #     for event in pygame.event.get():
# #         if event.type == QUIT:
# #             pygame.quit()
# #             sys.exit()
# #         pygame.display.update()
# #         if event.type == pygame.MOUSEBUTTONDOWN:
# #             pos = pygame.mouse.get_pos()
          
# #             row = pos[1] // (RECT_WIDTH + SCREEN_MARGIN)
# #             col = pos[0] // (RECT_WIDTH + SCREEN_MARGIN) 
# #             print(row)
# #             print(col) 
# #             # if((row,col)>(5,5)):
# #             #     break
# #             object2 = pygame.Rect(((col*50) , (row*50) ,50, 50))
# #             pygame.draw.rect(DISPLAYSURF,GREEN,object2)
# #     pygame.display.flip()

# # pygame.quit()
# # =========================================================
# import pygame, sys
# from pygame.locals import *

# pygame.init()

# # predefined colours
# BLUE  = (0, 0, 255)
# RED   = (255, 0, 0)
# GREEN = (0, 255, 0)
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)

# font1 = pygame.font.SysFont("comicsans",40)
# font2 = pygame.font.SysFont("comicsans",20)
# screen = pygame.display.set_mode((500,600))

# pygame.display.set_caption("Test Wordle")
# img = pygame.image.load("Enemy.png")
# pygame.display.set_icon(img)

# x=0
# y=0
# dif = 500/9
# val = 0

# grid =[
#         [7, 8, 0, 4, 0, 0, 1, 2, 0],
#         [6, 0, 0, 0, 7, 5, 0, 0, 9],
#         [0, 0, 0, 6, 0, 1, 0, 7, 8],
#         [0, 0, 7, 0, 4, 0, 2, 6, 0],
#         [0, 0, 1, 0, 5, 0, 9, 3, 0],
#         [9, 0, 4, 0, 6, 0, 0, 0, 5],
#         [0, 7, 0, 3, 0, 0, 0, 1, 2],
#         [1, 2, 0, 0, 0, 7, 4, 0, 0],
#         [0, 4, 9, 2, 0, 6, 0, 0, 7]
#     ]


# def get_cord(pos):
#     global x
#     x=pos[0]//dif
#     global y
#     y=pos[1]//dif


# def draw():
#     for i in range(9):
#         for j in range(9):
#             if grid[i][j] != 0:
#                 # Fill blue color in already numbered grid
#                 pygame.draw.rect(screen, (0, 153, 153), (i * dif, j * dif, dif + 1, dif + 1))
 
#                 # Fill grid with default numbers specified
#                 text1 = font1.render(str(grid[i][j]), 1, (0, 0, 0))
#                 screen.blit(text1, (i * dif + 15, j * dif + 15))
    
#     for i in range(10):
#         if i%3 == 0:
#             thick = 7
#         else:
#             thick = 1
#         pygame.draw.line(screen, (0, 0, 0), (0, i * dif), (500, i * dif), thick)
#         pygame.draw.line(screen, (0, 0, 0), (i * dif, 0), (i * dif, 500), thick) 

# def draw_val(val):
#     text1 = font1.render(str(val),1,(0,0,0))
#     screen.blit(text1,(x * dif + 15, y * dif + 15))      

# def raise_error1():
#     text1 = font1.render("wrong!!!",1,(0,0,0))
#     screen.blit(text1,(20,570))  

# def draw_box():
#     for i in range(2):
#         pygame.draw.line(screen, (255, 0, 0), (x * dif-3, (y + i)*dif), (x * dif + dif + 3, (y + i)*dif), 7)
#         pygame.draw.line(screen, (255, 0, 0), ( (x + i)* dif, y * dif ), ((x + i) * dif, y * dif + dif), 7)  


# while True: 
#     screen.fill((255, 255, 255))
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#             sys.exit()
#     if event.type == pygame.MOUSEBUTTONDOWN:
#         pos = pygame.mouse.get_pos()
#         get_cord(pos)

#     draw_box()
#      # Get the number to be inserted if key pressed   
#     if event.type == pygame.KEYDOWN:
#         x-=1
#         if event.key == pygame.K_RIGHT:
#             x+= 1
            
#         if event.key == pygame.K_UP:
#             y-= 1
                
#         if event.key == pygame.K_DOWN:
#             y+= 1
                
#         if event.key == pygame.K_1:
#             val = 1
#         if event.key == pygame.K_2:
#             val = 2   
#         if event.key == pygame.K_3:
#             val = 3
#         if event.key == pygame.K_4:
#             val = 4
#         if event.key == pygame.K_5:
#             val = 5
#         if event.key == pygame.K_6:
#             val = 6
#         if event.key == pygame.K_7:
#             val = 7
#         if event.key == pygame.K_8:
#             val = 8
#         if event.key == pygame.K_9:
#             val = 9    
#     draw_val(val)
#     draw()
#     pygame.display.update()

# guessWord = {
#     1:'Abroad', 2:'Accept',3:'Access',4:'Across',5:'Acting',6:'Action',7:'Active',8:'Actual',9:'Advice',10:'Advise',11:'Affect',12:'Afford',13:'Afraid',14:'Agency',15:'Agenda',
#     16:'Almost',17:'Always',18:'Amount',19:'Animal',20:'Annual',21:'Answer',22:'Anyone',23:'Anyway',24:'Appeal',25:'Appear',26:'Beyond',27:'Bishop',28:'Border',29:'Bottle',
#     30:'Bottom',31:'Bought',32:'Branch',33:'Breath',34:'Bridge',35:'Bright',36:'Casual',37:'Caught',38:'Center',39:'Centre',40:'Chance',41:'Change',42:'Charge',43:'Choice',
#     44:'Choose',45:'Chosen',46:'Church',47:'Circle',48:'Client',49:'Closed',50:'Closer',51:'Coffee',52:'Column',53:'Combat',54:'Coming',55:'Common',56:'Comply',57:'Copper',58:'Corner',
#     59:'Costly',60:'County',61:'Budget',62:'Burden',63:'Bureau',64:'Button',65:'Camera',66:'Cancer',67:'Cannot',68:'Carbon',69:'Career',70:'Castle',71:'Around',72:'Arrive',
#     73:'Artist',74:'Aspect',75:'Assess',76:'Assist',77:'Assume',78:'Attack',79:'Attend',80:'August',81:'Author',82:'Avenue',83:'Backed',84:'Barely',85:'Battle',86:'Beauty',
#     87:'Became',88:'Become',89:'Before',90:'Behalf',91:'Behind',92:'Belief',93:'Belong',94:'Bestie',95:'Better',96:'During',97:'Easily',98:'Eating',99:'Editor',100:'Effect',
#     101:'Effort',102:'Eighth',103:'Either',104:'Eleven',105:'Emerge',106:'Couple',107:'Course',108:'Covers',109:'Create',110:'Credit',111:'Crisis',112:'Custom',113:'Damage',
#     114:'Danger',115:'Dealer',116:'Debate',117:'Decade',118:'Decide',119:'Defeat',120:'Defend',121:'Define',122:'Degree',123:'Demand',124:'Depend',125:'Deputy',126:'Desert',
#     127:'Design',128:'Desire',129:'Detail',130:'Detect',131:'Device',132:'Differ',133:'Dinner',134:'Direct',135:'Doctor',136:'Dollar',137:'Domain',138:'Double',139:'Driven',
#     140:'Driver'
# }

import csv
# my_dict = {
#     1:'Abroad', 2:'Accept',3:'Access',4:'Across',5:'Acting',6:'Action',7:'Active',8:'Actual',9:'Advice',10:'Advise',11:'Affect',12:'Afford',13:'Afraid',14:'Agency',15:'Agenda',
#     16:'Almost',17:'Always',18:'Amount',19:'Animal',20:'Annual',21:'Answer',22:'Anyone',23:'Anyway',24:'Appeal',25:'Appear',26:'Beyond',27:'Bishop',28:'Border',29:'Bottle',
#     30:'Bottom',31:'Bought',32:'Branch',33:'Breath',34:'Bridge',35:'Bright',36:'Casual',37:'Caught',38:'Center',39:'Centre',40:'Chance',41:'Change',42:'Charge',43:'Choice',
#     44:'Choose',45:'Chosen',46:'Church',47:'Circle',48:'Client',49:'Closed',50:'Closer',51:'Coffee',52:'Column',53:'Combat',54:'Coming',55:'Common',56:'Comply',57:'Copper',58:'Corner',
#     59:'Costly',60:'County',61:'Budget',62:'Burden',63:'Bureau',64:'Button',65:'Camera',66:'Cancer',67:'Cannot',68:'Carbon',69:'Career',70:'Castle',71:'Around',72:'Arrive',
#     73:'Artist',74:'Aspect',75:'Assess',76:'Assist',77:'Assume',78:'Attack',79:'Attend',80:'August',81:'Author',82:'Avenue',83:'Backed',84:'Barely',85:'Battle',86:'Beauty',
#     87:'Became',88:'Become',89:'Before',90:'Behalf',91:'Behind',92:'Belief',93:'Belong',94:'Bestie',95:'Better',96:'During',97:'Easily',98:'Eating',99:'Editor',100:'Effect',
#     101:'Effort',102:'Eighth',103:'Either',104:'Eleven',105:'Emerge',106:'Couple',107:'Course',108:'Covers',109:'Create',110:'Credit',111:'Crisis',112:'Custom',113:'Damage',
#     114:'Danger',115:'Dealer',116:'Debate',117:'Decade',118:'Decide',119:'Defeat',120:'Defend',121:'Define',122:'Degree',123:'Demand',124:'Depend',125:'Deputy',126:'Desert',
#     127:'Design',128:'Desire',129:'Detail',130:'Detect',131:'Device',132:'Differ',133:'Dinner',134:'Direct',135:'Doctor',136:'Dollar',137:'Domain',138:'Double',139:'Driven',
#     140:'Driver'
# }
# with open('words.csv', 'w') as f:
#     for key in my_dict.keys():
#         f.write("%s,%s\n"%(key,my_dict[key]))

filename="words.csv"

with open('words.csv', mode='r') as infile:
    reader = csv.reader(infile)
    mydict = {int(rows[0]):rows[1] for rows in reader}
print(mydict)


