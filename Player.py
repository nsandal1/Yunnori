class Piece():

    def __init__(self,name, num):
        self.position = (0,"x")
        self.num = num
        self.name = name
    
    def getPosition(self):
        return self.position

    def getPiece(self):
        return (self.name, self.num)

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
        self.player1=player1
        self.player2=player2
        self.players=(self.player1,self.player2)
        self.coords=Coordinates(self.players)

    def retPlayers(self):
        print(self.players)

    def retPlayerN(self,n):
        return self.players[n-1]

    def getDict(self):
        return self.coords.getDict()





game1=Game()
plyr=game1.retPlayerN(1)
print(game1.getDict())
print(plyr.retColor())
print(plyr.retOrder())
print(plyr.retName())

