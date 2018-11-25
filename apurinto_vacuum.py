#ok now what
import copy
import random
from vacuum import VacuumAgent
rg = 60 #room finder square
drop = 79 #value of points we are alowed to lase at a time
l = 'Left'
r = 'Right'
u = 'Up'
d = 'Down'
s = 'Suck'
n = 'NoOp'
    #shorthand ^
    
''' 
    notes:
        use map to find location
        O is unexplored
        X is wall
        E is empty
        note: will always suck dirt when come acrossed
'''
class ApurintoVacuumAgent(VacuumAgent):

    #initialize object
    def __init__(self):
        super().__init__()
        self.mapo = [['O' for x in range(rg)] for x in range(rg)] #map of what i've learned
        self.xco=int(rg/2) # curentlocation
        self.yco=int(rg/2) # curentlocation
        self.lastMove = u # what i did do
        self.numMaxP = 0
        self.numCurP = 0
    
    # if bumped populate the wall
    #reset position
    def logic(self):
        if self.lastMove == u:
            self.mapo[self.xco][self.yco] = 'X'
            self.xco += 1 
            self.mapo[self.xco][self.yco] = 'E'
        elif self.lastMove == l:
            self.mapo[self.xco][self.yco] = 'X'
            self.yco += 1
            self.mapo[self.xco][self.yco] = 'E'
        elif self.lastMove == r:
            self.mapo[self.xco][self.yco] = 'X'
            self.yco -= 1
            self.mapo[self.xco][self.yco] = 'E'
        elif self.lastMove == d:
            self.mapo[self.xco][self.yco] = 'X'
            self.xco -= 1
            self.mapo[self.xco][self.yco] = 'E'
            
    #checks if a spot is clear
    def clear(self):
        if self.mapo[self.xco - 1][self.yco] == 'O':
            #print ("up", self.mapo[self.xco - 1][self.yco])
            self.lastMove = u
            self.xco -= 1 
            return u
        elif self.mapo[self.xco][self.yco - 1] == 'O':
            #print ("left" ,self.mapo[self.xco][self.yco - 1])
            self.lastMove = l
            self.yco -= 1
            return l
        elif self.mapo[self.xco][self.yco + 1] == 'O':
            #print("right", self.mapo[self.xco][self.yco + 1])
            self.yco += 1
            self.lastMove = r
            return r
        elif self.mapo[self.xco + 1][self.yco] == 'O':
            #print ("down", self.mapo[self.xco + 1][self.yco])
            self.lastMove = d
            self.xco += 1
            return d
        return n
    
    #determine next move based on random and map?
    def nexM(self):
        self.numCurP -= 1
        pls = self.clear()
        if pls != n:
            #print("going in ", pls)
            return pls
        else:
            #print("rano time!")
            return self.rano()
  
    
    #fill in map IF AND ONLY IF WE ARE IN RANDOM MODE
    def corn(self):
        #up and right || right and down || down and left || left and up
        if (self.mapo[self.xco -1][self.yco] == 'X' and self.mapo[self.xco][self.yco+1] == 'X') or (self.mapo[self.xco][self.yco+1] == 'X' and self.mapo[self.xco+1][self.yco] == 'X') or (self.mapo[self.xco +1][self.yco] == 'X' and self.mapo[self.xco][self.yco-1] == 'X') or (self.mapo[self.xco -1][self.yco] == 'X' and self.mapo[self.xco][self.yco-1] == 'X'):
            self.mapo[self.xco][self.yco] = 'X' # might as well block it off
            #print("kill it")
   
         
    #if i traped myself gotta go back one move oops
    def full(self):
        if self.mapo[self.xco -1][self.yco] == 'X' and self.mapo[self.xco+1][self.yco] == 'X' and self.mapo[self.xco][self.yco-1] == 'X' and self.mapo[self.xco][self.yco+1] == 'X':
            if self.lastMove == l:
                return r
            elif self.lastMove == r:
                return l
            elif self.lastMove == u:
                return d
            elif self.lastMove == d:
                return u
        return n
    
    
    #blocked on three sides? only one way to go    
    def blkchk(self):
        self.corn()#even if it isnt a 3block (meaning corner) we should block it off
        
        wait = self.full()#the off case where i block myself in
        if wait != n:
            return wait
        #open right
        if self.mapo[self.xco -1][self.yco] == 'X' and self.mapo[self.xco+1][self.yco] == 'X' and self.mapo[self.xco][self.yco-1] == 'X':
            return r
        #open left
        elif self.mapo[self.xco -1][self.yco] == 'X' and self.mapo[self.xco+1][self.yco] == 'X' and self.mapo[self.xco][self.yco+1] == 'X':
            return l
        #open down    
        elif self.mapo[self.xco -1][self.yco] == 'X' and self.mapo[self.xco][self.yco+1] == 'X' and self.mapo[self.xco][self.yco-1] == 'X':
            return d
        #open up
        elif self.mapo[self.xco +1][self.yco] == 'X' and self.mapo[self.xco][self.yco+1] == 'X' and self.mapo[self.xco][self.yco-1] == 'X':        
            return u
        else:
            return n
            
    #picks a random direction in worst case
    def rano(self):
        '''
        1 = LEFT
        2 = UP
        3 = RIGHT
        4 = DOWN
        '''
        
        # Look for a three way :/ hole
        choice = self.blkchk()
        if choice != n:#if there is an escape route
            if choice == l:
                self.lastMove = l
                self.yco -= 1
            elif choice == r:
                self.lastMove = r
                self.yco += 1
            elif choice == u:
                self.lastMove = u
                self.xco -= 1
            elif choice == d:
                self.lastMove = d
                self.xco += 1
            return choice
        
        tes = random.randint(1,10)
        
        if tes == 1:
            if  self.mapo[self.xco][self.yco - 1] == 'X' or self.lastMove == r:
                #dont walk into walls
                #dont go backwards
                return self.rano()
            self.lastMove = l
            self.yco -= 1
            return l
        elif tes == 2:
            if  self.mapo[self.xco - 1][self.yco] == 'X' or self.lastMove == d: #dont walk into walls
                return self.rano()
            self.lastMove = u
            self.xco -= 1 
            return u
        elif tes == 3 or tes == 7 or tes == 8 or tes == 9:
            if  self.mapo[self.xco][self.yco + 1] == 'X' or self.lastMove == l: #dont walk into walls
                return self.rano()
            self.lastMove = r
            self.yco += 1
            return r
        elif tes == 4 or tes == 5 or tes == 6 or tes == 10:
            if  self.mapo[self.xco + 1][self.yco] == 'X' or self.lastMove == u: #dont walk into walls
                return self.rano()
            self.lastMove = d
            self.xco += 1
            return d
        
        
    # check score
    def update(self):
        
        """
        print("LINE BREAK")
        for i in range(len(self.mapo)):
            for j in range(len(self.mapo[i])):
                print(self.mapo[i][j], end=' ')
            print()
            #"""
            
        if self.numCurP > self.numMaxP:
            self.numMaxP = copy.copy(self.numCurP)
            
            
    #main
    def program(self, percept):
        self.update()
        self.mapo[self.xco][self.yco] = 'E'
        if percept[0] == "Dirty":
            self.numCurP += 48
            #self.mapo[self.xco][self.yco] = 'E'
            #note:  Do not populate moves with suck -- that is only for movement
            return s
        #THIS IS GOOD ^ E        
        #above is not movement -- it shows empty squares
            
        if percept[1] == "Bump": #FIGURE OUT BUMPING
            self.logic()
        
        if self.numMaxP - self.numCurP > drop:
            return n
            #somecode = "wasteOfSpace"
        return self.nexM()