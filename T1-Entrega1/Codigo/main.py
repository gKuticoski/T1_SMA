ref=0

class Fila():
    def __init__(self, C, K, in_ut, out_ut, max_randoms) -> None:
        self.C = C
        self.K = K
        self.in_ut = in_ut
        self.out_ut = out_ut
        self.max_randoms = max_randoms
        self.tempo = 0
        self.fila = 0
        self.tempo_estados = [0] * (self.K+1)
        self.agenda = {}
        self.randoms = 0
        self.end = False
        self.loss = 0

    def chegada(self, new_time: float):
        self.tempo_estados[self.fila] += new_time - self.tempo
        self.tempo = new_time
        if self.fila < self.K:
            self.fila += 1
            if self.fila <= self.C:
                self.agendar('saida')
        else:
            self.loss+=1
            
        self.agendar('chegada')

    def saida(self, new_time: float):
        self.tempo_estados[self.fila] += new_time - self.tempo
        self.tempo = new_time
        self.fila -= 1
        if self.fila >= self.C:
            self.agendar('saida')

    def agendar(self, funcao: str):
        a, b = self.in_ut
        if funcao == 'saida':
            a, b = self.out_ut

        if self.randoms == self.max_randoms:
            self.agenda = {}
            self.end = True
        else:
            new_time = self.random_time(a, b)
            self.agenda[self.tempo + new_time] = funcao

    def random_time(self, a: int, b: int):
        self.randoms += 1
        global ref
        r = (b - a) * cl[ref] + a
        ref+=1
        return r

    def aaa(self):
        if len(self.agenda) == 0:
            self.chegada(self.tempo)
        else:
            next_function_time = min(self.agenda)
            next_function = self.agenda.pop(next_function_time)

            if next_function == 'saida':
                self.saida(next_function_time)
            elif next_function == 'chegada':
                self.chegada(next_function_time)

    def run(self, time: float):
        if len(self.agenda) == 0:
            self.chegada(time)
        else:
            next_function_time = min(self.agenda)
            next_function = self.agenda.pop(next_function_time)

            if next_function == 'saida':
                self.saida(next_function_time)
            elif next_function == 'chegada':
                self.chegada(next_function_time)
                
        while not self.end:
            self.aaa()

if __name__ == '__main__':
    
    x0 = 133.47
    a = 137.88
    c = 979.96
    m = 1536
    n = 1000000
    cl={}
    
    cl[0]=x0
    for i in range (n):
        if i != 0:
            cl[i] = (((cl[i - 1] * a) + c) % m)
    for i in range (n):
        cl[i] = cl[i]/m  
    #for i in range (n):
    #    print(cl[i], ' ')
    
    lista1 = []
    lista2 = []
    for i in range(5):
        fila1 = Fila(1, 5, (2, 4), (3, 5), 100000)
        fila1.run(3.0)
        lista1.append(fila1)
        fila2 = Fila(2, 5, (2, 4), (3, 5), 100000)
        fila2.run(3.0)
        lista2.append(fila2)
    
    med0=med1=med2=med3=med4=med5=medl=0
    for i in range(5):
        med0+=lista1[i].tempo_estados[0]
        med1+=lista1[i].tempo_estados[1]
        med2+=lista1[i].tempo_estados[2]
        med3+=lista1[i].tempo_estados[3]
        med4+=lista1[i].tempo_estados[4]
        med5+=lista1[i].tempo_estados[5]
        medl+=lista1[i].loss
    med0=med0/5
    med1=med1/5
    med2=med2/5
    med3=med3/5
    med4=med4/5
    med5=med5/5
    medl=medl/5
    l1=[med0,med1,med2,med3,med4,med5,medl]
    t1=med0+med1+med2+med3+med4+med5
    
    print('*****************************************************************************************************')
    print(' Queue: Q1 (G/G/1/5)')
    print(' Arrival: 2 ... 4')
    print(' Service: 3 ... 5')
    print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
    print(' State:        Probability:        Time:')
    
    for i in range(6):
        p1=round(100 * (l1[i]/t1),3)
        if p1<10:
            p1='0'+str(p1)
        while len(str(p1)) < 6:
            p1=str(p1)+'0'
        print('  ',i,'           ',p1,'%           ', round(l1[i],3))

    print('\n Tempo total: ', round(t1,2))
    print(' Number of losses: ',medl)
    
    med0=med1=med2=med3=med4=med5=medl=0
    for i in range(5):
        med0+=lista2[i].tempo_estados[0]
        med1+=lista2[i].tempo_estados[1]
        med2+=lista2[i].tempo_estados[2]
        med3+=lista2[i].tempo_estados[3]
        med4+=lista2[i].tempo_estados[4]
        med5+=lista2[i].tempo_estados[5]
        medl+=lista2[i].loss
    med0=med0/5
    med1=med1/5
    med2=med2/5
    med3=med3/5
    med4=med4/5
    med5=med5/5
    medl=medl/5
    l2=[med0,med1,med2,med3,med4,med5,medl]
    t2=med0+med1+med2+med3+med4+med5
    
    print('*****************************************************************************************************')
    print(' Queue: Q2 (G/G/2/5)')
    print(' Arrival: 2 ... 4')
    print(' Service: 3 ... 5')
    print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
    print(' State:        Probability:        Time:')

    for i in range(6):
        p1=round(100 * (l2[i]/t2),3)
        if p1<10:
            p1='0'+str(p1)
        while len(str(p1)) < 6:
            p1=str(p1)+'0'
        print('  ',i,'           ',p1,'%           ', round(l2[i],3))
    
    print('\n Tempo total: ', round(t2,2))
    print(' Number of losses: ',medl)
    print('*****************************************************************************************************')