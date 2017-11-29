class Piece: pass


class Player():

    def __init__(self,name="olivia", color="Purple",order=1):
        self.name=name
        self.color=color
        self.pieces=(Piece(),Piece(),Piece(),Piece())
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


class Game():

    def __init__(self, player1=Player(), player2=Player("luis","green",2)):
        self.player1=player1
        self.player2=player2
        self.players=(self.player1,self.player2)

    def retPlayers(self):
        print(self.players)

    def retPlayerN(self,n):
        return self.players[n-1]


game1=Game()
plyr=game1.retPlayerN(1)
print(plyr.retColor())
print(plyr.retOrder())
print(plyr.retName())

