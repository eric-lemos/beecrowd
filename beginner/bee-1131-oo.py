# https://www.beecrowd.com.br/judge/pt/problems/view/1131

class Bee_1131:
    def __init__(self):
        self.running = True
        self.new_match = 1
        self.wins = [0, 0]
        self.matchs = 0
        self.draws = 0
        
    def loop(self):
        while(self.running):
            if(self.new_match == 1):
                match = list(map(int, input().strip().split()))
                self.addMatchResult(match)
            elif(self.new_match == 2): break
            else:
                print('Novo grenal (1-sim 2-nao)', end=' ')
                self.new_match = int(input())
        self.checkWinner()

    def addMatchResult(self, match):
        inter, gremio = match
        
        if(inter > gremio):
            self.wins[0] += 1
            
        elif(gremio > inter):
            self.wins[1] += 1
            
        else: self.draws += 1
        
        self.new_match = 0
        self.matchs += 1

    def checkWinner(self):
        inter, gremio = self.wins
        
        print(f'{self.matchs} grenais')
        print(f'Inter: {self.wins[0]}')
        print(f'Gremio: {self.wins[1]}')
        print(f'Empates: {self.draws}')
        
        if(inter > gremio):
            print('Inter venceu mais')
            
        elif(gremio > inter):
            print('Gremio venceu mais')
        
        else:
            print('Nao houve vencedor')

if(__name__ == '__main__'):
    bee = Bee_1131()
    bee.loop()