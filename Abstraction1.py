class player:
    def plays(self):
        print("Players plays games")
class footballplayer(player):
    def plays(self):
        print("Football players plays football")
class cricketplayer(player):
    def plays(self):
        print("cricket players plays cricket")
class tennisplayer(player):
    def plays(self):
        print("Tennis players plays tennis")
class playground:
  def players(self,ref):
    ref.plays()
p=playground()
p.players(footballplayer())
p.players(cricketplayer())
p.players(tennisplayer())
main()


        
        
        

        
        
        
