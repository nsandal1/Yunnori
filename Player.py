import random

class Piece():
    
    def __init__(self, name, num, color):
        self.position = (0,"x")
        self.num = num
        self.name = name
        self.color = color
        self.status = 'queued'
#        self.stuck = false
        # if we initialize stuckTo as None, we don't need "stuck"
        self.stuckTo = None
    
    def getPosition(self):
        return self.position

    def getPiece(self):
        return (self.name, self.num, self.color)
    
    def getStatus(self):
        return self.status
    
    def playPiece(self):
        self.status = 'inPlay'
        
    def completePiece(self)
        self.status = 'completed'
    
    def movePiece(self, dieRoll):
        self.position += dieRoll
        
    def stickToPiece(self, piece):
#        self.stuck = true
        self.stuckTo = piece

class Player():

    def __init__(self,name="olivia", color="purple",order=1):
        self.name=name
        self.color=color
        self.pieces=(Piece(name,1),Piece(name,2),Piece(name,3),Piece(name,4))   #piece should contain player name
        self.order=order

    def retPieceN(self,n):
        return self.pieces[n]

    def retOrder(self):
        return self.order

    def retColor(self):
        return self.color

    def retName(self):
        return self.name
    
        
foo=input("starting...")



class Coordinates():

    def __init__(self,players):
        #self.grid= pass
        self.locations= {}
        for i in range(len(players)):
            for j in range(4):
                self.locations[(players[i].retName(), j+1 )] = players[i].retPieceN(j).getPosition()
            
    def getDict(self):
        return self.locations

    def piece2grid(self):
        pass

    def updatePos(self,piece,position):
        self.location[piece.getPiece()]=position

    def checkIfEmpty(self,position):
        return position in self.locations.values()

    def validateMove(self):
        pass



class Game():

    def __init__(self, player1=Player(), player2=Player("luis","green",2)):
        self.player1 = player1
        self.player2 = player2
        self.players = (self.player1,self.player2)
        self.coords = Coordinates(self.players)
        self.turn = 1
        self.contGame = true

    def retPlayers(self):
        print(self.players)

    def retPlayerN(self,n):
        return self.players[n-1]

    def getDict(self):
        return self.coords.getDict()
    
    def canBranch(self, piece):
        if piece.position == corner:
            return true
        else return false
    
    def shortcut(self, piece):
        if game.canBranch:
            piece.movePiece() #shortcut
    
    def roll(self):
        num = random.randint(0,15)
        if (num > 9):
            return 2
        elif (num > 5):
            return 1
        elif (num > 2):
            return 3
        elif (num > 1):
            return 4
        elif (num > 0):
            return 5
        else return -1
    
    def turn(self):
        
        
    def contGame(self):
        for x in range(0,3):
            



        Turn(S) [whose turn is it?]\ (2-4 player game)
        Turn(M) [check for extra turns,update whose turn]\
        Respawn(M)\.  [Coord(X), Coord(Y), Coord(Z) = Coord(Origin), Coord(Origin), Coor(Origin)] ?
        Taking(M) [Gives you an extra turn]\
        Kill(M)\
        Shortcut(M) [Normal Move v. Special Move]\
        Continue(S) [Has someone won?]\
    
    

game1=Game()
plyr=game1.retPlayerN(1)
print(game1.getDict())
print(plyr.retColor())
print(plyr.retOrder())
print(plyr.retName())

