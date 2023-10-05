class Player:
 def play(self):
   print("The Player Is Playing Cricket")

class Batsman(Player):
 def play(self):
   print("The Batsman Is Batting")

class Bowler(Player):
 def play(self):
   print("The Bowler Is Bowling")

# Create objects of Batsman and Bowler classes
batsman = Batsman()
bowler = Bowler()

# Call the play() method for each object
batsman.play()
bowler.play()
