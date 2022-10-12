import random

# classe da particula
class Walker:
    #alpha é alpha
    #size é o L
    def __init__(self, alpha, size):
        self.alpha = alpha
        self.size = size
        #array das probabilidades
        #p_array[0] = cima
        #p_array[1] = direita
        #p_array[2] = baixo
        #p_array[3] = esquerda
        self.p_array = [0.25, 0.25, 0.25, 0.25]
        #variavel que controla o tempo
        self.time = 0
        self.x = 0
        self.y = 0
    
    def walk(self):
        rand_num = random.random()
        dir = 0
        #acumulativa
        cum = 0
        for k, v in enumerate(self.p_array):
            cum += v
            if rand_num <= cum:
                dir = k
                break
        # atualiza posicao
        if(k == 0):
            self.y +=1
        elif(k==1):
            self.x+=1
        elif(k==2):
            self.y-=1
        else:
            self.x-=1
        
        
        #atualizar o array de probabilidade
        for k, v in enumerate(self.p_array):
            if k == dir:
                self.p_array[k] = 0.25 + self.alpha
            ##direcao oposta
            elif k == (dir + 2)%4:
                self.p_array[k] = 0.25 - self.alpha
            else:
                self.p_array[k] = 0.25
        
        
        self.time+=1
    #  retorna o array [x, y, tempo]
    def reset(self):
        self.x = 0
        self.y = 0
        self.time = 0
        return


    def simulate(self):
        #arrays de posição de Walker para cada iteração
        while (abs(self.x) != self.size and abs(self.y) != self.size):
            self.walk()
        #retorna os arrays e o tempo decorrido
        x = self.x
        y = self.y
        time = self.time
        self.reset()
        return [x, y, time]
