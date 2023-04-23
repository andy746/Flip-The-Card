import pygame as pyg
 
class Card():
    # INPUT:
    # images refer to a list of rectangles taken from the spritesheet
    # name refer to the type of card
    def __init__(self, images, name):
        self.images = images
        
        # cur_image refers to the rectangle taken from the spritesheet
        # that will be drawn onscreen
        self.cur_image = images[0]
        
        self.name = name

        # clicked refers to if the card object onscreen was mouse-clicked on
        self.clicked = False

    # INPUT:
    # index refers to the number used to access a particular element of
    # self.images (a list)
    # Returns the rectangle taken from the spritesheet that will be
    # drawn onscreen 
    def change_image(self, index):
        self.cur_image = self.images[index]

    # INPUT:
    # pos refers to a tuple of x and y coordinate values
    # which will be used to construct the rectangle that represents
    # the card onscreen
    def change_pos(self, pos):
        x, y = pos
        self.rect = pyg.Rect(x, y, 200, 200)
    
    # GETTER METHODS

    # Returns the rectangle that will represent the card onscreen
    def get_rect(self):
        return self.rect

    # Returns the type of the card
    def get_name(self):
        return self.name

    # Returns if the card object onscreen was mouse-clicked on
    def get_clicked(self):
        return self.clicked

    # SETTER METHOD

    # INPUT:
    # value refers to a Boolean value that will be stored within
    # self.clicked
    def set_clicked(self, value):
        self.clicked = value
    
    # INPUT:
    # surface refers to the game window used to draw the card object on
    # sheet refers to the spritesheet
    def draw(self, surface, sheet):
        # reveals the card onscreen
        if self.clicked == True:
            self.change_image(1)
            
	#draw card on screen
        surface.blit(sheet, (self.rect.x, self.rect.y), self.cur_image)

		



