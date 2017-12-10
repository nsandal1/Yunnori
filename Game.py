import Player
import Coordinates
import random
        
foo=input("starting...")


class Game():                               #need to generalized to N players

    def __init__(self, number=2):
        self.noPlayers=number
        self.players=[]
        self.names=[]
        
        for i in range(number):
            self.players.append(Player.Player(input("\n\nPlayer {0} name: ".format(i+1)),input("Player {0} color: ".format(i+1)),i+1))
            
        for i in self.players:
            self.names.append(i.retName())


        
##        self.player1=player1
##        self.player2=player2
##        self.players=[self.player1,self.player2]
        self.coords=Coordinates.Coordinates(self.players)
    
    def winCondition(self):
        for i in self.players:
            if i.retPromoted() == 4:
                print("\n\n [[[[   ",i.retName(),"has WON!!!   ]]]]")
                return 1
            else:
                return 0 #return int(input("termination condition: (0 or 1): "))                #naively: check dictionary for "y" for all player pieces
                                                                           #         may be too computationally intensive though

    def roll(self):
        seq=[-1,1,2,3,4,5,6]
        return random.choice(seq)

    
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
        
        ##print(self.winCondition(),"hi")
            
        while not self.winCondition():
            print("\n\n[[[[ It is Player {0}'s turn ]]]] \n\n".format(turn+1))
            self.whereAre(self.retPlayerN(turn).retName())
            
            #roll = self.roll() #taking out randomness for debugging
            roll = int(input("\nroll: "))
            print("You rolled a {0}!\n".format(roll))
            piece = self.retPlayerN(turn).retPieceN(int(input("Select a Valid Piece to Move: ")))
            piece.move(tuple(input("Input a Valid Coordinate: "))) ###THIS IS NOT GOING TO WORK

            #branching decisions should go here
            
            if self.validateMove(piece) == "continue":
                self.coords.updatePos(piece)

            elif self.validateMove(piece) == "eat":
                eaten = self.coords.whoIsThere(piece.getPosition())
                self.coords.updatePos(piece)
                player=self.players[self.names.index(eaten[0])]
                piece=player.retPieceN(eaten[1])
                piece.eat()
                self.coords.updatePos(piece)#needs to take in piece for player eaten
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
            
            

            #elf.whereAre(self.retPlayerN(turn).retName())
            

            
            

            
            
            turn = (turn + 1) % self.noPlayers

        
            
'''    
    while self.winCondition():

        print(turn)

        turn = (turn + 1) % self.getNo()  #
'''        

def main():
    
    game1=Game(int(input("How many players? ")))     #could be implemented better
    game1.development()
    #plyr=game1.retPlayerN(1)
    #game1.whereAre()
    #print(game1.retPlayerN(1).retColor())
    if not(input("restart?... ").lower() == "n"):
        main()
    


if __name__== "__main__":
    main()


#print(plyr.retColor())
#print(plyr.retOrder())
#print(plyr.retName())

