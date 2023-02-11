import pygame, sys, random
from pygame.locals import *
import csv

pygame.init()
clock = pygame.time.Clock() 

global value 
global x_cord
global y_cord
global num
global var_i_val
global var_j_val
global global_time 
global_time = 0
value = 0
x = 0
y = 0
dif = 1000/10
var_i_val = 1
var_j_val = -1



# predefined colours
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ORANGE = (255,97,3)


font1 = pygame.font.SysFont("comicsans",40)
font2 = pygame.font.SysFont("comicsans",20)
screen = pygame.display.set_mode((1000,800))
screen.fill(WHITE)

pygame.display.set_caption("Wordle")
img = pygame.image.load("wordle_edit.png")
pygame.display.set_icon(img)

# Load image
image = pygame.image.load('wordle_edit.png')
  
# Set the size for the image
DEFAULT_IMAGE_SIZE = (700, 120)

# Set a default position
DEFAULT_IMAGE_POSITION = (140,0)
  
# Scale the image to your needed size
image = pygame.transform.scale(image, DEFAULT_IMAGE_SIZE)
screen.blit(image, DEFAULT_IMAGE_POSITION)

filename="words.csv"

with open('words.csv', mode='r') as infile:
    reader = csv.reader(infile)
    guessWord = {int(rows[0]):rows[1] for rows in reader}
    

num = random.randint(1,140)
# num = 32
print(guessWord[num])

grid = [
    [guessWord[num][0],guessWord[num][0],guessWord[num][0],guessWord[num][0],guessWord[num][0],guessWord[num][0]],
    [guessWord[num][1],guessWord[num][1],guessWord[num][1],guessWord[num][1],guessWord[num][1],guessWord[num][1]],
    [guessWord[num][2],guessWord[num][2],guessWord[num][2],guessWord[num][2],guessWord[num][2],guessWord[num][2]],
    [guessWord[num][3],guessWord[num][3],guessWord[num][3],guessWord[num][3],guessWord[num][3],guessWord[num][3]],
    [guessWord[num][4],guessWord[num][4],guessWord[num][4],guessWord[num][4],guessWord[num][4],guessWord[num][4]],
    [guessWord[num][5],guessWord[num][5],guessWord[num][5],guessWord[num][5],guessWord[num][5],guessWord[num][5]]
]

w, h = 6, 6
grid_data = [['' for x in range(w)] for y in range(h)] 
grid_color = [[0 for x in range(w)] for y in range(h)]

class pop_up:
    def draw_popup(self):
        
        # Load image
        self.image_wel = pygame.image.load('welcome_msg.png')
            
        # Set the size for the image
        self.DEFAULT_IMAGE_SIZE = (250, 100)

        # Set a default position
        self.DEFAULT_IMAGE_POSITION = (375,400)
            
        # Scale the image to your needed size
        self.image = pygame.transform.scale(self.image_wel, self.DEFAULT_IMAGE_SIZE)
        screen.blit(self.image, self.DEFAULT_IMAGE_POSITION)

def draw_box():
    for i in range(2):
        pygame.draw.line(screen, BLACK, (x * dif-3, (y + i)*dif), (x * dif + dif + 3, (y + i)*dif), 4)
        pygame.draw.line(screen, BLACK, ( (x + i)* dif, y * dif ), ((x + i) * dif, y * dif + dif), 4)  

def draw():
    for i in range(2,8):
        for j in range(var_j_val+3,8):
            pygame.draw.rect(screen,(0, 153, 153),(i*dif,j*dif,dif+1,dif+1))

            text1 = font1.render(str(grid_data[i-2][j-2]),1,RED)
            screen.blit(text1,((i)*dif+35 , (j)*dif+20))

    for i in range(2,9):
        thick = 2
        pygame.draw.line(screen,BLACK,(200,i*dif),(800,i*dif),thick)
        pygame.draw.line(screen,BLACK,(i*dif,200),(i*dif,800),thick)
    
        
def get_cord(pos):
    # print(pos)
    global x
    global y
    y = pos[1]//dif 
    x = pos[0]//dif
    # print(x) 
    # print(y) 

def draw_val(data):
    x_cord = int(x)
    y_cord = int(y)

    grid_data[x_cord-2][y_cord-2] = data
    
    text1 = font1.render(str(grid_data[x_cord-2][y_cord-2]),1,RED)
    screen.blit(text1,(x*dif+35 , y*dif+20))

def event_reset():
    pygame.event.clear(eventtype= pygame.KEYDOWN)

def validate():
    for i in range(2,8):
        for j in range(var_i_val,8):
            if grid_color[i-2][j-2] == 1:
                pygame.draw.rect(screen,GREEN,(i*dif,j*dif,dif+1,dif+1))
                text1 = font1.render(str(grid_data[i-2][j-2]),1,RED)
                screen.blit(text1,((i)*dif+35 , (j)*dif+20))
            elif grid_color[i-2][j-2] == 2:
                pygame.draw.rect(screen,ORANGE,(i*dif,j*dif,dif+1,dif+1))
                text1 = font1.render(str(grid_data[i-2][j-2]),1,RED)
                screen.blit(text1,((i)*dif+35 , (j)*dif+20))
            elif grid_color[i-2][j-2] == 3:
                pygame.draw.rect(screen,BLUE,(i*dif,j*dif,dif+1,dif+1))
                text1 = font1.render(str(grid_data[i-2][j-2]),1,RED)
                screen.blit(text1,((i)*dif+35 , (j)*dif+20))
    for i in range(2,9):
        thick = 2
        pygame.draw.line(screen,BLACK,(200,i*dif),(800,i*dif),thick)
        pygame.draw.line(screen,BLACK,(i*dif,200),(i*dif,800),thick)

timer_event = pygame.USEREVENT+1
pygame.time.set_timer(timer_event,1000)

p1 = pop_up()

run = True
flag1 = 0
flag2 = 0
t_flag = 0


while run:    
    for event in pygame.event.get():
        # Quit the game window
        if event.type == pygame.QUIT:
            run = False 
        if event.type == timer_event:
            if t_flag == 0:
                p1.draw_popup()
                t_flag += 1
            else:
                draw()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            get_cord(pos)
            flag1 = 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= 1
                flag1 = 1
            if event.key == pygame.K_RIGHT:
                x += 1
                flag1 = 1
            if event.key == pygame.K_UP:
                y -= 1
                flag1 = 1
            if event.key == pygame.K_DOWN:
                y += 1
                flag1 = 1
            if event.key == pygame.K_a:
                value = 'A'
            if event.key == pygame.K_b:
                value = 'B'
            if event.key == pygame.K_c:
                value = 'C'
            if event.key == pygame.K_d:
                value = 'D'
            if event.key == pygame.K_e:
                value = 'E'
            if event.key == pygame.K_f:
                value = 'F'
            if event.key == pygame.K_g:
                value = 'G'
            if event.key == pygame.K_h:
                value = 'H'
            if event.key == pygame.K_i:
                value = 'I'
            if event.key == pygame.K_j:
                value = 'J'
            if event.key == pygame.K_k:
                value = 'K'
            if event.key == pygame.K_l:
                value = 'L'
            if event.key == pygame.K_m:
                value = 'M'
            if event.key == pygame.K_n:
                value = 'N'
            if event.key == pygame.K_o:
                value = 'O'
            if event.key == pygame.K_p:
                value = 'P'
            if event.key == pygame.K_q:
                value = 'Q'
            if event.key == pygame.K_r:
                value = 'R'
            if event.key == pygame.K_s:
                value = 'S'
            if event.key == pygame.K_t:
                value = 'T'
            if event.key == pygame.K_u:
                value = 'U'
            if event.key == pygame.K_v:
                value = 'V'
            if event.key == pygame.K_w:
                value = 'W'
            if event.key == pygame.K_x:
                value = 'X'
            if event.key == pygame.K_y:
                value = 'Y'
            if event.key == pygame.K_z:
                value = 'Z'
            if event.key == pygame.K_BACKSPACE:
                value = ''
            if event.key==pygame.K_RETURN:
                if x_cord == 7:
                    flag2 = 1
                    var_i_val+=1
                    var_j_val+=1
            
    x_cord = int(x)
    y_cord = int(y)

    draw()

    if (x_cord >=2 and x_cord <=7) and ((y_cord >=2 and y_cord <=7)):
        # print(x_cord,' and ',y_cord)
        if flag1 == 1:
            draw_box()
        if value != 0:
            if (y_cord-2) >= var_j_val+1:
                draw_val(value)
                grid_data[x_cord-2][y_cord-2] = value
                flag1 = 0
                value = 0

    if flag2 == 1:
        for j in range(0,6):
            x_val = var_j_val
            # print("x_val is : ",x_val)
            if (guessWord[num].lower()).__contains__(grid_data[j][x_val].lower()):
                if grid[j][x_val].lower() == grid_data[j][x_val].lower() and grid_data[j][x_val] !=  '':
                    grid_color[j][x_val] = 1
                elif grid[j][x_val].lower() != grid_data[j][x_val].lower() and grid_data[j][x_val] !=  '':
                    grid_color[j][x_val] = 2 
            else:
                grid_color[j][x_val] = 3          
            validate()
    if x_cord != 7:
        flag2 = 0


    pygame.display.update()

pygame.quit()