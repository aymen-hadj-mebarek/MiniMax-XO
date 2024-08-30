import pygame

# initializing the game
pygame.init()

# initializing the window
WIN_HEIGHT = 340
WIN_WIDTH = 310
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("XO GAME BY AYMEN")

# intializing the squares and lines
class square():
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 100, 100)
        self.x = x
        self.y = y
        self.value = "empty"
        self.played = False
    def draw(self):
        if self.value == "empty":
            pygame.draw.rect(screen,(255,255,255),(self.x,self.y,100,100))
        elif self.value == "X":
            pygame.draw.line(screen,(255,0,0),(self.x+10,self.y+10),(self.x+90,self.y+90),5)
            pygame.draw.line(screen,(255,0,0),(self.x+90,self.y+10),(self.x+10,self.y+90),5)
        elif self.value == "O":
            pygame.draw.circle(screen,(0,0,255),((self.x+100/2),(self.y+100/2)),40,5)
    
    def player(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] and not self.played:
                self.played = True
                self.value = "X"
                global turn
                turn = "ai"
    def ai(self):
        self.value = "O"
        self.played = True
        global turn
        turn = "player"
                
class button():
    def __init__(self,x,y,text):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x,y,60,30)
        self.text = text
    def draw(self,screen):
        pygame.draw.rect(screen,(0,0,0),self.rect,1)
        screen.blit(font.render(self.text,1,(0,0,0)),(self.x+1,self.y+1))
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]:
                print("clicked")
                return True
        return False
        
squares = [ square1 := square(0,0),
            square2 := square(105,0),
            square3 := square(210,0),
            square4 := square(0,105),
            square5 := square(105,105),
            square6 := square(210,105),
            square7 := square(0,210),
            square8 := square(105,210),
            square9 := square(210,210)]

font = pygame.font.SysFont("Arial",20)

# main loop
run = True
game = True
turn = "player"
restart_btn = button(200,310,"Restart")
def minimax(tab,depth,isMaximizing):
    global turn
    if check_win(tab) == 2:
        score = 1
    elif check_win(tab) == 1:
        score = -1
    elif check_win(tab) == -1:
        score = 0
    else:
        if isMaximizing:
            # print("max")
            # draw(tab)
            best_sc = 2
            for i in tab:
                if i.value == "empty":
                    i.value  = "X"
                    score = minimax(tab,depth+1,False)
                    i.value = "empty"
                    best_sc = min(score, best_sc)
            return best_sc
        else:
            best_sc = -2
            # print("min")
            # draw(tab)
            for i in tab:
                if i.value == "empty":
                    i.value = "O"
                    score = minimax(tab,depth+1,True)
                    i.value = "empty"    
                    best_sc = max(score, best_sc)
            return best_sc
            
    return score

def check_win(tab):
    wins = [(0,1,2),
            (3,4,5),
            (6,7,8),
            (0,3,6),
            (1,4,7),
            (2,5,8),
            (2,4,6),
            (0,4,8)
            ]
    for x,y,z in wins:
        if tab[x].value == tab[y].value and tab[x].value == tab[z].value and tab[y].value == "X":
            return 1
        elif tab[x].value == tab[y].value and tab[x].value == tab[z].value and tab[y].value == "O":
            return 2
    else:
        for i in tab:
            if i.value == "empty":
                return 0
        return -1

while run:
    screen.fill((255,255,255))
    pygame.draw.line(screen,(0,0,0),(0,101),(WIN_HEIGHT,101),4)
    pygame.draw.line(screen,(0,0,0),(0,206),(WIN_HEIGHT,206),4)
    pygame.draw.line(screen,(0,0,0),(101,0),(101,WIN_HEIGHT-40),4)
    pygame.draw.line(screen,(0,0,0),(206,0),(206,WIN_HEIGHT-40),4)
    if check_win(squares) == 0:
        count = 0
        screen.blit(font.render("it is "+turn+"'s turn",1,(0,0,0)),(80,310))
        for square in squares:
            square.draw()
            if turn == "player":
                square.player()
            
        if check_win(squares) == 0:
            if turn == "ai":
                best_score = -100
                best_move = -1
                for i in squares:
                    if i.value == "empty":
                        i.value = "O"
                        score = minimax(squares,0,True)
                        i.value = "empty"
                        
                        if score > best_score:
                            best_score = score
                            best_move = squares.index(i)
                squares[best_move].ai()
    else:
        for square in squares:
            square.draw()
            
        if restart_btn.draw(screen):
            for i in squares:
                i.played = False
                i.value = "empty"
            for square in squares:
                square.draw()
            pygame.display.update()
            # game = False
        if check_win(squares) == -1:
            screen.blit(font.render("it is a TIE!",1,(0,0,0)),(40,310))
        if check_win(squares) == 1:
            screen.blit(font.render("X is winner!",1,(0,0,0)),(40,310))
        if check_win(squares) == 2:
            screen.blit(font.render("O is winner!",1,(0,0,0)),(40,310))
            
            
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    pygame.display.update()

pygame.quit()
