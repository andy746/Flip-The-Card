import pygame as pyg, sys
from random import randint as rr
from Card import Card

class GUI():
    pyg.init()

    # setup game window
    w = pyg.display.set_mode((1000, 800))

    # get rectangle that represents game window
    wr = w.get_rect()
    
    pyg.display.set_caption('Hide n Seek')

    # load spritesheet
    sheet = pyg.transform.scale(pyg.image.load("cards.png"), (400, 800))
    
    # variable to store the width and height of each individual sprite
    ss = [400//2, 800//4]

    # set a variable to get access to fonts
    fonts = pyg.font.get_fonts()
    
    # takes a row from the spritesheet and breaks it
    # into multiple sprites (each sprite is a rectangle object) 
    # that are stored in a list variable which is returned
    def break_row(self, row_num, frames):
        anim = []
        for i in range(frames):
            anim.append(pyg.Rect(self.ss[0] * i, self.ss[1] * row_num, self.ss[0], self.ss[1]))
        return anim
    

class Game(GUI):
    def __init__(self):
        # types of cards
        feather = self.break_row(0, 2)
        mush = self.break_row(1, 2)
        star = self.break_row(2, 2)
        flower = self.break_row(3, 2)
        
        # declare Card objects and randomize the positions of them
        self.cards = []

        self.cards.append(Card(feather, "feather"))
        self.cards.append(Card(flower, "flower"))
        self.cards.append(Card(star, "star"))
        self.cards.append(Card(mush, "mushroom"))
       
        self.randomize_pos()

        # player prediction
        self.predict = ""

        # Store in a string that denotes the objective to be found
        self.goal = self.randomize_objective()

        # denotes when player has clicked on a card
        self.has_clicked = False

    # Randomizes the position of each card
    def randomize_pos(self):
        random = [(150, 100), (650, 100), (150, 500), (650, 500)]
        for card in self.cards:
            num = rr(1, len(random)) - 1
            card.change_pos(random[num])
            random.remove(random[num])

    # Returns a string that denotes the objective to be found
    def randomize_objective(self):
        num = rr(1, 4)
        if num == 1:
            return "feather"
        elif num == 2:
            return "flower"
        elif num == 3:
            return "star"
        else:
            return "mushroom"

    # draw instructions/feedback
    def draw_instruct(self, surface):
        font = pyg.font.SysFont(self.fonts[0], 50, True, True)
        colors = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        # instructions
        if self.has_clicked == False:
            text = font.render("Find the " + self.goal, True, colors[1])
        else:
            # feedback
            if self.predict == self.goal:
                text = font.render("Correct!", True, colors[1])
            else:
                text = font.render("Try Again!", True, colors[1])

        # draw the text
        surface.blit(text, text.get_rect(center = self.wr.center))

    # game loop
    def gameloop(self):
        while True:
            self.w.fill("lightblue")

            # event loop
            for event in pyg.event.get():
                if event.type == pyg.QUIT:
                    pyg.quit()
                    sys.exit()

            # variable for storing mouse input
            pos = pyg.mouse.get_pos()
            
            self.draw_instruct(self.w)

            # loop to iterate through each of the cards
            for i in range(len(self.cards)):
                self.cards[i].draw(self.w, self.sheet)

                # check mouseover and clicked conditions
                if self.cards[i].get_rect().collidepoint(pos):
                    if pyg.mouse.get_pressed()[0] == 1 and not self.has_clicked:
                        self.cards[i].set_clicked(True)
                        self.predict = self.cards[i].get_name()
                        self.has_clicked = True      

            pyg.display.update()
            pyg.time.delay(33)
            pyg.event.pump()

game = Game()
game.gameloop()
