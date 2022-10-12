import random
import matplotlib.pyplot as plt

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
        #arrays de posição de Walker para cada iteração
        x_pos = []
        y_pos = []
        
        #escreve a posição inicial no array
        x_pos.append(self.pos[0])
        y_pos.append(self.pos[1])
        while (abs(self.pos[0]) != self.size and abs(self.pos[1]) != self.size):
            self.walk()

            #escreve a posição de Walker a cada iteração
            x_pos.append(self.pos[0])
            y_pos.append(self.pos[1])
        
        #retorna os arrays e o tempo decorrido
        return x_pos, y_pos, self.time


#seeds usadas: 127, (OUTRAS AQUI)
#random.seed(127)

#cria um Walker com alpha e L definidos
a1 = Walker(0.1, 10)
x_range, y_range, runtime = a1.simulate()

#array[runtime] == posição final de a1
print("Final position: (", x_range[runtime], "," , y_range[runtime], ")", "Time: ", runtime)

#cria um gráfico para visualizar a caminhada de a1
fig, randwalk = plt.subplots()

#abaixo seta o título, faz o plot da caminhada e seta os limites do gráfico
plt.title("2D random walk")
randwalk.plot(x_range, y_range)
randwalk.set(xlim = (-11,11), ylim = (-11,11))
plt.show()