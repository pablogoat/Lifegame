import pygame
import random

pygame.init()
screen = pygame.display.set_mode((1080,1080))
pygame.display.set_caption("LifeGame")

dead = pygame.image.load(r"assets\dead.png")
live = pygame.image.load(r"assets\live.png")

run = True
start = False

class cell:
    def __init__(self, x):
        self.live = False
        self.neighbor = 0
        self.neighborold = 0
        self.imag = x

    def add(self, x):
        self.neighbor += x
            

cells = [[cell(dead) for i in range(27)] for j in range(27)]

"""
for i in range(1,26,1):
    for j in range(1,26,1):
        if random.randint(0,3) == 1:
            cells[i][j].imag = live
            cells[i][j].live = True
            for k in range(i-1,i+2,1):
                for m in range(j-1,j+2,1):
                    if (k >= 0 and k <= 27 and m >= 0 and m <= 27):
                        cells[k][m].add(1)
"""

while run:

    for i in range(27):
        for j in range(27):
            screen.blit(cells[i][j].imag, (i*40,j*40))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]

            if cells[int((x-(x%40))/40)][int((y-(y%40))/40)].live:
                cells[int((x-(x%40))/40)][int((y-(y%40))/40)].live = False
                cells[int((x-(x%40))/40)][int((y-(y%40))/40)].imag = dead
                cells[int((x-(x%40))/40)][int((y-(y%40))/40)].add(1)

                for i in range(int((x-(x%40))/40)-1,int((x-(x%40))/40)+2,1):
                    for j in range(int((y-(y%40))/40)-1,int((y-(y%40))/40)+2,1):
                        if (i >= 0 and i <= 27 and j >= 0 and j <= 27):
                            cells[i][j].add(-1)

            else:
                cells[int((x-(x%40))/40)][int((y-(y%40))/40)].live = True
                cells[int((x-(x%40))/40)][int((y-(y%40))/40)].imag = live
                cells[int((x-(x%40))/40)][int((y-(y%40))/40)].add(-1)

                for i in range(int((x-(x%40))/40)-1,int((x-(x%40))/40)+2,1):
                    for j in range(int((y-(y%40))/40)-1,int((y-(y%40))/40)+2,1):
                        if (i >= 0 and i <= 27 and j >= 0 and j <= 27):
                            cells[i][j].add(1)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                for i in range(27):
                    for j in range(27):
                        cells[j][i].imag = dead
                        cells[j][i].l = False
                for k in range(i-1,i+2,1):
                    for m in range(j-1,j+2,1):
                        if (k >= 0 and k <= 27 and m >= 0 and m <= 27):
                            cells[k][m].add(-1)
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_f:
                if start:
                    start = False
                else:
                    start = True
    
    """
    for i in range(27):
        for j in range(27):
            print(cells[i][j].neighbor, end=" ")
        print(end = "\n")
    print("|||||||||||||||")
    """

    if start:
        pygame.time.delay(50)

        for i in range(27):
            for j in range(27):
                cells[i][j].neighborold = cells[i][j].neighbor
        for i in range(27):
            for j in range(27):
                if cells[i][j].live:
                    if (cells[i][j].neighborold == 2 or cells[i][j].neighborold == 3):
                        pass
                    else:
                        cells[i][j].live = False
                        cells[i][j].imag = dead
                        cells[i][j].add(1)
                        for k in range(i-1,i+2,1):
                            for m in range(j-1,j+2,1):
                                if (k >= 0 and k <= 27 and m >= 0 and m <= 27):
                                    cells[k][m].add(-1)
                else:
                    if cells[i][j].neighborold == 3:
                        cells[i][j].live = True
                        cells[i][j].imag = live
                        cells[i][j].add(-1)
                        for k in range(i-1,i+2,1):
                            for m in range(j-1,j+2,1):
                                if (k >= 0 and k <= 27 and m >= 0 and m <= 27):
                                    cells[k][m].add(1)

    pygame.display.update()