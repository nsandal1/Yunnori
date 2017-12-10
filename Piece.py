class Piece():

    def __init__(self,name, num):
        self.position = (0,"x")     # x means out of game, y signifies a promoted piece
        self.num = num
        self.name = name
        self.lastPos = None
    
    def getPosition(self):
        return self.position

    def getPiece(self):
        return (self.name, self.num)

    def retLastPos(self):
        return self.lastPos

    def promote(self):
        pass

    def combine(self):
        pass

    def uncombine(self):
        pass

    def eat(self):
        self.position = (0,"x")
        

    def move(self,coord):
        if type(coord) is tuple:
            self.lastPos = self.position            #need it to undo a bad move
            self.position = int(coord[0]),coord[1]
            #print(self.getPosition()) #debugging
    

        else: print("coordinate is not tuple")
        

