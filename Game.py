import Player
import Coordinates
import random
        
foo=input("starting...")


class Game():                               #need to generalized to N players

    def __init__(self, number=2):
        self.noPlayers=number
        self.players=[]
        self.names=[]
        self.pieces[]
        
        for i in range(number):
            self.players.append(Player.Player(input("\n\nPlayer {0} name: ".format(i+1)),input("Player {0} color: ".format(i+1)),i+1))
        
            
        for i in self.players:
            self.names.append(i.retName())


        self.coords=Coordinates.Coordinates(self.players)
    
    def winCondition(self):
        for i in self.players:
                if i.retWin() == 4:
                        return True
        return False
                    
            
        ''''
        for i in self.players:
            if i.retPromoted() == 4:
                print("\n\n [[[[   ",i.retName(),"has WON!!!   ]]]]")
                return 1
            else:
                return 0 #return int(input("termination condition: (0 or 1): "))                #naively: check dictionary for "y" for all player pieces
        '''' 
         
         
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
    
    def validateMove(self,piece):                 #decides if branching conditions are met
        coord=piece.getPosition() 
        if coord == (0,"y"):                    #just migrated!!!
            return "promote"
        elif self.coords.checkIfEmpty(coord):
            return "continue"
        elif self.coords.whoIsThere(coord)[0] == piece.getPiece()[0]:
            return "combine"
        else:
            return "eat"
            

    
    #Defining a bunch of helper functions that may not be necessary outside of Troubleshooting
    def getNo(self):
        return self.noPlayers
    
    def retPlayers(self):
        print(self.players)

    def retPlayerN(self,n):
        return self.players[n]

    def getDict(self):
        return self.coords.getDict()

    def whereAre(self,player=0):
        if player == 0:
            for a,b in self.getDict().items():
                print("{0}'s Piece #{1} is at Position {2}".format(a[0],a[1],b))
        else:
            for a,b in self.getDict().items():
                if a[0] == player:
                    print("{0}'s Piece #{1} is at Position {2}".format(a[0],a[1],b))

    #Game develops from here

    def development(self):
        turn=0
        roll= None
        piece = None
            
        while not self.winCondition():
            
            print("\n\n[[[[ It is Player {0}'s turn ]]]] \n\n".format(turn+1))
            self.whereAre(self.retPlayerN(turn).retName())
            
            roll = self.roll() #taking out randomness for debugging
            #roll = int(input("\nroll: "))
            print("You rolled a {0}!\n".format(roll))
            piece = self.retPlayerN(turn).retPieceN(int(input("Select a Valid Piece to Move: ")))
            piece.move(tuple(input("Input a Valid Coordinate: "))) 

            #branching decisions should go here
            
            if self.validateMove(piece) == "continue":
                self.coords.updatePos(piece)
                print(piece.retLastPos(),"---->",piece.getPosition())

            elif self.validateMove(piece) == "eat":
                eaten = self.coords.whoIsThere(piece.getPosition())
                self.coords.updatePos(piece)
                print(piece.retLastPos(),"---->",piece.getPosition())
                player=self.players[self.names.index(eaten[0])]
                piece=player.retPieceN(eaten[1])
                piece.eat()
                self.coords.updatePos(piece)
                                                        #need to uncombine
                self.whereAre()
                print("\n\n",self.retPlayerN(turn).retName(), "ate one of ", player.retName(),"'s pieces!")

            elif self.validateMove(piece) == "promote":
                self.coords.updatePos(piece)
                self.retPlayerN(turn).incPromoted()

                print("\n\n !!!!!  Player {0} has {1} Point(s)    !!!!".format(self.names[(turn)],self.retPlayerN(turn).retPromoted()))
                

            elif self.validateMove(piece) == "combine":
            
                piece.combine()

            else: print("You should never get here")
            
    
            
            
            turn = (turn + 1) % self.noPlayers



def main():
    
    game1=Game(int(input("How many players? ")))    
    game1.development()
  
    if not(input("restart?... ").lower() == "n"):
        main()
    


if __name__== "__main__":
    main()




