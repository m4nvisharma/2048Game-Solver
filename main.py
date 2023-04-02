#Final Project
#ManviSharma
#Program should run 2048 and allow input from user. If user presses escape, the program ends pygame. If user presses space, the program allows user to play 2048 game. If user presses tab, the program lets AI automatically solve game to highest number achievable. 

#importing necessary modules
import numpy as np
import random
import time

#modules in original template
import pygame as py
import sys

#initializing pygame
py.init()

#setting border size for grid to be four
edge = 4

#creating a dictionary with the colour scheme from the original game 
colours = {'bg':(187, 173, 160),
0:(204, 192, 179),
2:(238, 228, 218),
4:(237, 224, 200),
8:(242, 177, 121),
16:(245, 149, 99),
32:(246, 124, 95),
64:(246, 94, 59),
128:(237, 207, 114),
256:(237, 204, 97),
512:(237, 200, 80),
1024:(237, 197, 63),
2048:(237, 194, 46),
'else':(0,0,0),
'gameOver':(238, 228, 218),
'dark':(119, 110, 101),
'light':(249, 246, 242),
'layout':(128,128,128) }
#creating the ideal grid that the grid aims to become as a numpy array
idealgrid =  np.array([[2,4,8,16],[32,64,128, 256],[512,1024,2048, 4096],[8192,16384,32768, 65536]])

#creating the class under which the game is played
class GameBoard:
  #initializing basics of the gameboard
  def __init__(self):  
    #setting a width for the board
    self.wid = 400
    #setting a height for the board
    self.hei = 500
    #setting the screen
    self.screen = py.display.set_mode([self.wid, self.hei])
    #initializing the grid to start off as a four by four grid of zeros
    self.grid = np.zeros((edge,edge), dtype = int)
    #intializing a time function
    self.time = py.time.Clock()
    #initializing the font used
    self.font = py.font.Font('freesansbold.ttf', 24)
    #starting the turns at -2 
    self.turn = -2
    #setting the score to 0
    self.score = 0
  def __str__(self):
    return str(self.grid)
  #function to add a tile at random
  def addtile(self):
    #finding all the 'open' positions in the gameboard; tiles that are zero, and assigning them to openpos as a list of coordinates [(x,y)] for each space
    openpos = list(zip(*np.where(self.grid == 0)))
    #picking a random position from these open positions
    for pos in random.sample(openpos, k=1):
      #using a 10% chance to assign this random spot to '4'
      if random.random() < 0.1:
        self.grid[pos] = 4
      #using a 90% chance to assign this random spot to a '2'
      else:
        self.grid[pos] = 2
      #adding a turn to the turn counter because if a tile has been added, then a move has been played 
      self.turn += 1
  #function to actually move tiles depending on user input
  def make_move(self, move):
    #considering the user wants to move right
    if move == 'r':
      #indicing the grid into each of the 4 rows 
      newrow1 = self.grid[0]
      newrow2 = self.grid[1]
      newrow3 = self.grid[2]
      newrow4 = self.grid[3]

      #moving all the zeros to the left in row1 so all numbers are moved right
      newrow1 = np.concatenate((newrow1[newrow1==0], newrow1[newrow1!=0]))
      #reversing list so it can be iterated through properly
      newrow1 = newrow1[::-1]
      #iterating through the numpy row with index and value of each tile
      for idx, x in enumerate(newrow1):
        #considering if the tile isnt at the edge of the board and if two like-tiles are together
        if idx != len(newrow1)-1 and newrow1[idx] == newrow1[idx+1]:
          #creating new tile to become double the original tile
          newrow1[idx] *= 2
          #assigning the merging tile to become empty (0)
          newrow1[idx+1] = 0
        else:
          #else, letting it stay the same
          newrow1[idx] = newrow1[idx]
      #reversing the list back 
      newrow1 = newrow1[::-1]
      #again moving all the zeros to the left so there are no gaps 
      newrow1 = np.concatenate((newrow1[newrow1==0], newrow1[newrow1!=0]))
      #repeating this for all four rows till the all tiles in the grid have successfully moved right
      newrow2 = np.concatenate((newrow2[newrow2==0], newrow2[newrow2!=0]))
      newrow2 = newrow2[::-1]
      for idx, x in enumerate(newrow2):
        if idx != len(newrow2)-1 and newrow2[idx] == newrow2[idx+1]:
          newrow2[idx] *= 2
          newrow2[idx+1] = 0
        else:
          newrow2[idx] = newrow2[idx]
      newrow2 = newrow2[::-1]
      newrow2 = np.concatenate((newrow2[newrow2==0], newrow2[newrow2!=0]))
      newrow3 = np.concatenate((newrow3[newrow3==0], newrow3[newrow3!=0]))
      newrow3 = newrow3[::-1]
      for idx, x in enumerate(newrow3):
        if idx != len(newrow3)-1 and newrow3[idx] == newrow3[idx+1]:
          newrow3[idx] *= 2
          newrow3[idx+1] = 0
        else:
          newrow3[idx] = newrow3[idx]
      newrow3 = newrow3[::-1]
      newrow3 = np.concatenate((newrow3[newrow3==0], newrow3[newrow3!=0]))
      newrow4 = np.concatenate((newrow4[newrow4==0], newrow4[newrow4!=0]))
      newrow4 = newrow4[::-1]
      for idx, x in enumerate(newrow4):
        if idx != len(newrow4)-1 and newrow4[idx] == newrow4[idx+1]:
          newrow4[idx] *= 2
          newrow4[idx+1] = 0
        else:
          newrow4[idx] = newrow4[idx]
      newrow4 = newrow4[::-1]
      newrow4 = np.concatenate((newrow4[newrow4==0], newrow4[newrow4!=0]))
      
      rightgrid = newrow1
      rightgrid = np.vstack([rightgrid, newrow2, newrow3, newrow4])

      self.grid = rightgrid
      
    #considering the user wants to move left
    elif move == 'l':
      #indicing the grid into each of the 4 rows
      newrow1 = self.grid[0]
      newrow2 = self.grid[1]
      newrow3 = self.grid[2]
      newrow4 = self.grid[3]
      #assigning all the zeros to the right so all numbers are pushed left
      newrow1 = np.concatenate((newrow1[newrow1!=0], newrow1[newrow1==0]))
      #iterating through row with index and value
      for idx, x in enumerate(newrow1):
        #considering its not the value at the edge of board and there are two like values beside each other
        if idx != len(newrow1)-1 and newrow1[idx] == newrow1[idx+1]:
          #creating new tile to become double the original tile
          newrow1[idx] *= 2
          #assigning the original merging tile to become empty (0)
          newrow1[idx+1] = 0
        else:
          #else, letting it be
          newrow1[idx] = newrow1[idx]
      #moving all zeros to the right once again
      newrow1 = np.concatenate((newrow1[newrow1!=0], newrow1[newrow1==0]))
      #repeating this for all four rows till the all tiles in the grid have successfully moved left
      newrow2 = np.concatenate((newrow2[newrow2!=0], newrow2[newrow2==0]))
      for idx, x in enumerate(newrow2):
        if idx != len(newrow2)-1 and newrow2[idx] == newrow2[idx+1]:
          newrow2[idx] *= 2
          newrow2[idx+1] = 0
        else:
          newrow2[idx] = newrow2[idx]
      newrow2 = np.concatenate((newrow2[newrow2!=0], newrow2[newrow2==0]))
      #modifying third row
      newrow3 = np.concatenate((newrow3[newrow3!=0], newrow3[newrow3==0]))
      for idx, x in enumerate(newrow3):
        if idx != len(newrow3)-1 and newrow3[idx] == newrow3[idx+1]:
          newrow3[idx] *= 2
          newrow3[idx+1] = 0
        else:
          newrow3[idx] = newrow3[idx]
      newrow3 = np.concatenate((newrow3[newrow3!=0], newrow3[newrow3==0]))
      #modifying fourth row
      newrow4 = np.concatenate((newrow4[newrow4!=0], newrow4[newrow4==0]))
      for idx, x in enumerate(newrow4):
        if idx != len(newrow4)-1 and newrow4[idx] == newrow4[idx+1]:
          newrow4[idx] *= 2
          newrow4[idx+1] = 0
        else:
          newrow4[idx] = newrow4[idx]
      newrow4 = np.concatenate((newrow4[newrow4!=0], newrow4[newrow4==0]))
      
      leftgrid = newrow1
      leftgrid = np.vstack([leftgrid, newrow2, newrow3, newrow4])
      self.grid = leftgrid

    #considering the user wants to move up
    elif move == 'u':
      #indicing the grid for each column, creating a row format
      newcol1 = self.grid[:,0]
      newcol2 = self.grid[:,1]
      newcol3 = self.grid[:,2]
      newcol4 = self.grid[:,3]
      #moving all the zeros to the right
      newcol1 = np.concatenate((newcol1[newcol1!=0], newcol1[newcol1==0]))
      #iterating through this row
      for idx, x in enumerate(newcol1):
        #considering its not the edge of the board and two like-tiles are beside each other
        if idx != len(newcol1)-1 and newcol1[idx] == newcol1[idx+1]:
          #making the new tile double the original
          newcol1[idx] *= 2
          #assigning the original tile to 0 (empty)
          newcol1[idx+1] = 0
        else:
          #else, letting it be
          newcol1[idx] = newcol1[idx]
      #moving all the empty tiles to right once again, and reshaping into a column
      newcol1 = np.concatenate((newcol1[newcol1!=0], newcol1[newcol1==0])).reshape(4,1)
      #repeating this for all four columns until all elements in board have successfully moved up
      newcol2 = np.concatenate((newcol2[newcol2!=0], newcol2[newcol2==0]))
      for idx, x in enumerate(newcol2):
        if idx != len(newcol2)-1 and newcol2[idx] == newcol2[idx+1]:
          newcol2[idx] *= 2
          newcol2[idx+1] = 0
        else:
          newcol2[idx] = newcol2[idx]
      newcol2 = np.concatenate((newcol2[newcol2!=0], newcol2[newcol2==0])).reshape(4,1)
      
      newcol3 = np.concatenate((newcol3[newcol3!=0], newcol3[newcol3==0]))
      
      for idx, x in enumerate(newcol3):
        if idx != len(newcol3)-1 and newcol3[idx] == newcol3[idx+1]:
          newcol3[idx] *= 2
          newcol3[idx+1] = 0
        else:
          newcol2[idx] = newcol2[idx]
      
      newcol3 = np.concatenate((newcol3[newcol3!=0], newcol3[newcol3==0])).reshape(4,1)
      
      newcol4 = np.concatenate((newcol4[newcol4!=0], newcol4[newcol4==0]))
      
      for idx, x in enumerate(newcol4):
        if idx != len(newcol4)-1 and newcol4[idx] == newcol4[idx+1]:
          newcol4[idx] *= 2
          newcol4[idx+1] = 0
        else:
          newcol4[idx] = newcol4[idx]
      
      newcol4 = np.concatenate((newcol4[newcol4!=0], newcol4[newcol4==0])).reshape(4,1)
      
      upgrid = newcol1
      upgrid = np.concatenate([upgrid,newcol2,newcol3,newcol4], axis = 1)
      
      self.grid = upgrid
   
    #considering the user wants to move down
    elif move == 'd':
      #indicing through the grid for each of the four columns, automatically converting t a row format
      newcol1 = self.grid[:,0]
      newcol2 = self.grid[:,1]
      newcol3 = self.grid[:,2]
      newcol4 = self.grid[:,3]
      #moving all empty spaces to the left, and all numbers to the right
      newcol1 = np.concatenate((newcol1[newcol1==0], newcol1[newcol1!=0]))
      #reversing list so it can be properly iterated
      newcol1 = newcol1[::-1]
      #iterating through the row
      for idx, x in enumerate(newcol1):
        #considering its not an edge tile and two like-tiles are beside each other
        if idx != len(newcol1)-1 and newcol1[idx] == newcol1[idx+1]:
          #assigning one to become double the original tile
          newcol1[idx] *= 2
          #assigning the merging tile to 0 (empty)
          newcol1[idx+1] = 0
        else:
          #else, letting it be
          newcol1[idx] = newcol1[idx]
      #reversing the list once again
      newcol1 = newcol1[::-1]
      #moving all the 0's to the left once again, while also reshaping into a column
      newcol1 = np.concatenate((newcol1[newcol1==0], newcol1[newcol1!=0])).reshape(4,1)
      #repeating this for all 4 columns in grid until all elements on board have successfully moved down
      newcol2 = np.concatenate((newcol2[newcol2==0], newcol2[newcol2!=0]))
      newcol2 = newcol2[::-1]
      for idx, x in enumerate(newcol2):
        if idx != len(newcol2)-1 and newcol2[idx] == newcol2[idx+1]:
          newcol2[idx] *= 2
          newcol2[idx+1] = 0
        else:
          newcol2[idx] = newcol2[idx]
      newcol2 = newcol2[::-1]
      newcol2 = np.concatenate((newcol2[newcol2==0], newcol2[newcol2!=0])).reshape(4,1)
      
      newcol3 = np.concatenate((newcol3[newcol3==0], newcol3[newcol3!=0]))
      newcol3 = newcol3[::-1]
      for idx, x in enumerate(newcol3):
        if idx != len(newcol3)-1 and newcol3[idx] == newcol3[idx+1]:
          newcol3[idx] *= 2
          newcol3[idx+1] = 0
        else:
          newcol2[idx] = newcol2[idx]
      newcol3 = newcol3[::-1]
      newcol3 = np.concatenate((newcol3[newcol3==0], newcol3[newcol3!=0])).reshape(4,1)
      
      newcol4 = np.concatenate((newcol4[newcol4==0], newcol4[newcol4!=0]))
      newcol4 = newcol4[::-1]
      for idx, x in enumerate(newcol4):
        if idx != len(newcol4)-1 and newcol4[idx] == newcol4[idx+1]:
          newcol4[idx] *= 2
          newcol4[idx+1] = 0
        else:
          newcol4[idx] = newcol4[idx]
      newcol4 = newcol4[::-1]
      newcol4 = np.concatenate((newcol4[newcol4==0], newcol4[newcol4!=0])).reshape(4,1)
    
      downgrid = newcol1
      downgrid = np.concatenate([downgrid,newcol2,newcol3,newcol4], axis = 1) 

      self.grid = downgrid
    #considering an else function in case of error
    else:
      #quitting program if the user doesn't choose to move any of the possible directions
      quit()
  #function to add visual component of game
  def draw_grid(self):
    #drawing a rectangle on screen to represent actual game play area of screen, on screen with background color and rounded edges
    py.draw.rect(self.screen, colours['bg'], [0, 0, 400, 400], 0, 10)
    #iterating through rows on grid
    for i in range(edge):
      #iterating through columns on grid
      for j in range(edge):
        #assigning 'val' to the specific value it represents at that specific row/column positioning
        val = self.grid[i][j]
        #considering the value is less than 2048
        if val <= 2048:
          #letting the colour be the colour represented by the number on tile from the colour dictionary
          colour = colours[val]
        else:
          #else setting the colour of tile to be black
          colour = colours['else']
        #drawing each square tile with rounded edges at intervals
        py.draw.rect(self.screen, colour, (j*95 + 20, i*95 + 20, 75, 75), 0, 5)
        #considering the value is greater than 4
        if val > 4:
          #assigning the colour of the text to be light text from colours dictionary
          val_col = colours['light']
        else:
          #else, assigning the colour of the text to be dark text from colours dictionary
          val_col = colours['dark']
        #getting the number of numbers in the value number 
        vallen = len(str(val))
        #considering the value isn't an empty space (0)
        if val>0:
          #initializing the font to get smaller depending on the length of the number so it fits the tile
          font = py.font.Font('freesansbold.ttf', 48 - (5*vallen))
          #rendering the number needed to be displated with its appropriate colour
          valtext = font.render(str(val), True, val_col) 
          #getting the location of the text to be the center of each square
          text = valtext.get_rect(center = (j*95 + 57, i*95 + 60))
          #displaying the number of tile on the tile on the screen with appropriate sizing and colouring
          self.screen.blit(valtext, text)
      pass

  #function getting input from user
  def keyinput(self):
    while True:
      #getting event 
      for event in py.event.get():
        #from original module, if it indicates quit then return 'q'
        if event.type == py.quit:
          return 'q'
        #assigning keys to key pressed
        keys = py.key.get_pressed() 
        #considering a key is pressed
        for key in keys:
          #considering escape is pressed, returning 'q'
          if keys[py.K_ESCAPE]:
            return 'q'
          #considering tab is pressed, returning 'start'
          if keys[py.K_TAB]:
            return 'start'
          if keys[py.K_SPACE]:
            return 'game'
          if keys[py.K_LEFT]:
            return 'l'
          if keys[py.K_RIGHT]:
            return 'r'
          if keys[py.K_DOWN]:
            return 'd'
          if keys[py.K_UP]:
            return 'u'
        
  #function determining if game is over
  def gameOver(self):
    #assigning list 'invalidmoves'
    invalidmoves = []
    #creating a copy of the original grid
    org_grid = self.grid.copy()
    #iterating through all possible moves; right, left, up, down
    for i in 'rlud':
      #making this each possible move
      self.make_move(i)
      #considering the grid has not changed after making that move, appending '1' to list 'move'
      if all((org_grid == self.grid).flatten()):
        invalidmoves.append(1)
    #assigning the grid back to original grid
    self.grid = org_grid
    #considering the length of 'invalidmoves' is 4; meaning all moves are invalid, returning gameOver as True
    if len(invalidmoves) == 4:
      return True
    #else, some move is still possible, so returning gameOver as false
    else:
      return False
      
  #function drawing gameOver screen
  def draw_gameOver(self):
    #creating a new surface the size of game board
    self.surf = py.Surface((400, 400)) 
    #setting alpha to be 128 (50% transparency)
    self.surf.set_alpha(186.15)
    #filling the surface to white (50% transparent)
    self.surf.fill(colours['gameOver'])
    #displaying this screen to the output
    self.screen.blit(self.surf, (0,0))
    #delaying for 0.3 mps
    time.sleep(0.3)
    #setting font for 'Game Over!' display
    fnt = py.font.Font('freesansbold.ttf', 48)
    #rendering 'Game over!' text with appropriate colour
    fonter = fnt.render('Game over!', True, colours['dark'])
    #placing the text to the center of the gameboard
    place = fonter.get_rect(center = (200,200))
    #displaying 'Game over!' in the right font, size, and place
    self.screen.blit(fonter, place)
    
  #function to find heuristic of board in comparison to ideal board
  def draw_graphics(self):
    #creating a new surface for the area on the screen excluding the game board to overlay over previous graphics
    self.graphics = py.surface.Surface((400, 100))
    #filling in screen the same colour as the layout backhground
    self.graphics.fill(colours['layout'])
    #blitzing this graphics to the screen
    self.screen.blit(self.graphics, (0,400))
    #rendering font for score and turn counter
    fnt = py.font.Font('freesansbold.ttf', 20)
    #rendering 'Score:' and the value for the score in the light text colour 
    score = fnt.render('Score: ', True, colours['light'])
    scoreval = fnt.render(str(self.score), True, colours['light'])
    #determining place for both score label and value 
    scorevlplace = scoreval.get_rect(center = (120, 460))
    splace = score.get_rect(center = (50,460))
    #blitzing both score label and value to screen with appropriate place for each
    self.screen.blit(score, splace)
    self.screen.blit(scoreval, scorevlplace)
    #rendering Turn label and value in the lighter text colour
    turn = fnt.render('Turn: ', True, colours['light'])
    turnval = fnt.render(str(self.turn), True, colours['light'])
    #determining place for both score label and value
    tplace = turn.get_rect(center = (50, 430))
    tvalpl = turnval.get_rect(center = (120, 430))
    #blitzing both score label and value to screen with appropriate place for each
    self.screen.blit(turn, tplace)
    self.screen.blit(turnval, tvalpl)
  
  def draw_instruct(self):
    #initiizing font with size 15 for instructions
    fnt = py.font.Font('freesansbold.ttf', 13)
    #rendering space, tab, and escape instructions in light font 
    inst = fnt.render('Press "space" to play, "tab" for solver or "escape" to exit.', True, colours['light'])
    #determining the place for instructions
    instplc = inst.get_rect(center = (200, 450))
    #blitzing to screen
    self.screen.blit(inst, instplc)
    
  def heuristic(self):
    #setting heuristic, h, to zero
    h = 0
    #iterating through the rows in the grid
    for i in range(edge):
      #iterating through the columns in the grid
      for j in range(edge):
        #multiplying each value on the grid with the corresponding value on the ideal grid and adding this value to the heuristic
        h += self.grid[i][j] * idealgrid[i][j]
    #returning final heuristic value of board
    return h
  
  #function to get heuristic value of board depending on move 
  def values1(self, cmd):
    values = []
    #making a copy of original grid
    org_grid = self.grid.copy()
    #making whichever move is later referenced
    self.make_move(cmd)
    if all((self.grid == org_grid).flatten()):
      values.append(0)
      return values
    #finding all open positions on grid and returning as (x,y) coordinates in list to openpos
    openpos = list(zip(*np.where(self.grid == 0)))
    #creating empty list 'values'
    
    #iterating through all open positions on grid
    for x in openpos:
      #placing a 2 anywhere on grid
      self.grid[x] = 2
      #determining heuristic value with this new grid
      val = self.heuristic()
      #appending this heuristic value to the 'values' list
      values.append(val)
      #assigning grid back to original grid
      self.grid = org_grid
    #returning list 'values', which includes all heuristic values of grid considering move was made and a random tile was placed on the board
    avg = 0
    if len(values) != 0:
      avg = sum(values)/len(values)
      
    return avg

  #function to get best move
  def getmove2(self):
    #creating empty list 'vals'
    vals = []
    #creating a copy of original grid
    old_grid = self.grid.copy()
    #assigning values command to 'r' (move right) and returning with an average of all heuristic values considering move was playing and a random tile was placed somewhere on the grid
    right = self.values1('r')
    #considering there are no heuristic 
    vals.append(right)

    #setting grid back to original grid
    #repeating this for all moves (left, up, down) until the average heuristic of each move is appended to list 'vals'
    self.grid = old_grid
    left = self.values1('l')
    
    vals.append(left)

    self.grid = old_grid
    up = self.values1('u')
    
    vals.append(up)

    self.grid = old_grid
    down = self.values1('d')
    
    vals.append(down)

    #setting the grid back to the original grid
    self.grid = old_grid
    #assigning move to the highest value of the averaged heuristic values of each move by finding max in list 'vals'
    move = max(vals)

    #determining which move this value corresponds to, and, assigning 'move' to that move
    if move == right:
      move = 'r'
    if move == left:
      move = 'l'
    if move == up:
      move = 'u'
    if move == down:
      move = 'd'

    #making 'best move'
    self.make_move(move)
    #checking if the grid remains the same after making the best move, in the case that it believes that it has reached the ideal grid even if it hasn't reached 2048
    if all((old_grid == self.grid).flatten()):
      #setting it back to the original grid
      self.grid = old_grid
      #choosing a move at random to keep the play going and assigning that move to 'move'
      move = random.choice('rlud')
    #setting the grid back to the original grid
    self.grid = old_grid
    #returning this best move
    return move
    
  
  #function to actually play the game
  def Play(self):
    #starting off with adding two tiles at random using previously defined 'addtile' function
    self.addtile()
    self.addtile()
    #filling the screen to the background colour
    self.screen.fill(colours['layout'])
    #setting the caption to '2048'
    py.display.set_caption('2048')
    #drawing the playing board
    self.draw_grid()
    #updating the board
    py.display.flip()
    self.draw_instruct()
    py.display.flip()
    #setting running and game to false so the game doesn't start right away
    running = False
    game = False
    #setting won to false
    won = False
    #getting input from the user
    start = self.keyinput()
    #considering the user pressed 'tab', start would return 'start'; so setting running to true in this case
    if start == 'start':
      running = True
    #considering the user pressed 'escape', ending pygame
    elif start == 'q':
      py.quit()
      sys.exit()
    elif start == 'game':
      game = True
    #setting a contiuous loops given user wants AI to solve the game
    while running:
      #drawing the board
      self.draw_grid()
      #updating the board
      py.display.flip()
      #checking if any are '2048', and, if so, printing 'Game Won!' and ending game loop
      #using the won variable to make sure that Game Won! is printed only once
      if not won and np.any(self.grid == 2048):
        print("Game Won!")
        won = True
      #checking if game is over using the previously defined gameOver function
      if self.gameOver():
        #printing 'Game Over' to console
        print("Game Over.")
        #delaying by 0.5 mps before drawing the game over screen onto the output
        time.sleep(0.5)
        self.draw_gameOver()
        #updating screen
        py.display.flip()
        #ending game loop
        running = False
      #creating a copy of the grid
      old_grid = self.grid.copy()
      #setting 'move' to the best move using the previously defined getmove2 function
      move = self.getmove2()
      #making this best move
      self.make_move(move)
      #checking if the max value of new grid is different from old grid -considering a new higher merge has been made-, and, adding this value to the score
      if np.max(old_grid) != np.max(self.grid):
        self.score += np.max(self.grid)
      #considering the grid remains the same after the move and it's past the first turn, continuing
      if all((old_grid == self.grid).flatten()):
        continue
      #else, adding a new tile to the board at random
      else:
        self.addtile()
      #updating the playing board
      py.display.flip()
      self.draw_graphics()
      py.display.flip()
    #setting a continous loop given user wants to play the game
    while game:
      #drawing the board
      self.draw_grid()
      #updating the board
      py.display.flip()
      #considering the game is won, displaying "Game Won" and continuing the game
      if not won and np.any(self.grid == 2048):
        print("Game Won!")
        won = True
      #considering game is lost
      if self.gameOver():
        #printing Game Over. to console
        print("Game over.")
        #drawing game over screen
        self.draw_gameOver()
        #updating screen
        py.display.flip()
        #exiting game loop
        game = False
        break
      #getting input from user
      move = self.keyinput()
      #considering user presses escape, exiting the pygame
      if move == 'q':
        py.quit()
        sys.exit()
      #creating a copy of the board
      old_grid = self.grid.copy()
      #making move user chose
      self.make_move(move)
      #adding to score if the move allowed for another higher number on the board
      if np.max(old_grid) != np.max(self.grid):
        self.score += np.max(self.grid)
      #considering the move didn't change any aspect of board
      if all((old_grid == self.grid).flatten()):
        continue
      #else, adding a tile at random to board
      else:
        self.addtile()
      #updating screen
      py.display.flip()
      self.draw_graphics()
      py.display.flip

#setting the function to actually run the class
if __name__ ==  '__main__': 
  #assigning play to class GameBoard
  play = GameBoard()
  #playing the game
  play.Play()
  



