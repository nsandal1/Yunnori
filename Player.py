import Piece

class Player():

    def __init__(self,name="olivia", color="purple",order=1):
        self.name=name
        self.color=color
        self.pieces=(Piece.Piece(name,1),Piece.Piece(name,2),Piece.Piece(name,3),Piece.Piece(name,4))   #piece should contain player name
        self.order=order
        self.promoted=0
        self.win = 0

    def retPieceN(self,n):
        return self.pieces[n-1]

    def retOrder(self):
        return self.order

    def retColor(self):
        return self.color

    def retName(self):
        return self.name

    def retPromoted(self):
        return self.promoted

    def incPromoted(self,n=1):
        self.promoted+=n
    
