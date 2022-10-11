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
        self.pos = [0, 0]
    
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
            self.pos[1]+=1
        elif(k==1):
            self.pos[0]+=1
        elif(k==2):
            self.pos[1]-=1
        else:
            self.pos[0]-=1
        

        #atualizar o array de probabilidade
        for k, v in enumerate(self.p_array):
            if k == dir:
                self.p_array[k] = 0.25 + self.alpha
            ##direcao oposta
            elif (k + 2)%4:
                self.p_array[k] = 0.25 - self.alpha
            else:
                self.p_array[k] = 0.25
        self.time+=1
    #  retorna o array [x, y, tempo]
    def simulate(self):

        f = open("walk.txt", "w")
        
        #escreve a posição inicial no arquivo
        f.write(str(self.pos[0]) + "\t" + str(self.pos[1]) + "\n")
        while (abs(self.pos[0]) != self.size and abs(self.pos[1]) != self.size):
            self.walk()
            #escreve a posição de Walker a cada iteração
            f.write(str(self.pos[0]) + "\t" + str(self.pos[1]) + "\n")
        f.close()
        
        return [self.pos[0], self.pos[1], self.time]


a1 = Walker(0.25, 10)
print(a1.simulate())