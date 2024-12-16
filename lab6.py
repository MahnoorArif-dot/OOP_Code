from random import randint

class Batsman:
    def __init__(self, name, country, matches=0):
        self.setN(name)
        self.setC(country)
        if matches == 0:
            self.matches = randint(1, 95)
        else:
            self.matches = matches
        
        self.__randomScores()
        
    def setN(self, name):
        self.__name = name
        
    def getN(self):
        return self.__name
    
    def setC(self, country):
        self.__country = country
    
    def getC(self):
        return self.__country
    
    def __randomScores(self):
        scores = []
        for i in range(self.matches - 1):
            scores.append(randint(0, 180))
        z = randint(1, 5)
        for i in range(z):
            x = randint(0, self.matches - 2)
            scores[x] = randint(180, 500)
        self.__s = scores
            
    def getS(self):
        return self.__s 
             
    def calcTotal(self):
        total = 0
        for i in range(len(self.getS())):
            total = total + self.getS()[i]
        return total
    
    def calcAverage(self):
        l = self.matches
        avr = self.calcTotal() / l
        return avr
    
    def findMaxScore(self):
        max = self.getS()[0]
        for i in range(1, self.matches - 1):
            if max < self.getS()[i]:
                max = self.getS()[i]
        return max
            
    def count50s(self):
        c = 0
        for i in range(self.matches - 1):
            if self.getS()[i] >= 50:
                c = c + 1
        return c
    
    def count100s(self):
        c = 0
        for i in range(self.matches - 1):
            if self.getS()[i] >= 100:
                c = c + 1
        return c
        
    def show(self):
        print(f"Name : {self.getN()}\nCountry : {self.getC()}\nNo of matches : {self.matches}\nScores : {self.getS()}\nTotal Scores :{self.calcTotal()}\nAverage of scores :{self.calcAverage()}\nHighest scores of batsmen :{self.findMaxScore()}\n50's of batsmen : {self.count50s()}\n100's of batsmen : {self.count100s()} ")
        
def main():
    b = Batsman("Lubaba ", "Pakistan", 10)
    b.show()
    print("\n")
    b1 = Batsman("Mahnoor", "Bangladesh")
    b1.show()
    print("\n")
    b2 = Batsman("Rabbiya", "India", 9)
    b2.show()
    
main()

