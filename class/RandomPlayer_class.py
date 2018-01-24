import random

class  RandomPlayer:
   def __init__(self,p=0.5):
       self.p_defect =p
   def move(self,game):
       return random.uniform(0,1)<self.p_defect
   def record(self,game):
       pass