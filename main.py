class Fila():
    def __init__(self, C, K, in_ut, out_ut, max_randoms, seed) -> None:
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
        self.seed = seed
        self.perdidos = 0

    def chegada(self, new_time: float):
        self.tempo_estados[self.fila] += new_time - self.tempo
        self.tempo = new_time
        if self.fila < self.K:
            self.fila += 1
            if self.fila <= self.C:
                self.agendar('saida')
        else:
            self.perdidos += 1

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
        A = 8121
        C = 978
        M = 134456
        self.seed = (((self.seed * A) + C) % M)

        self.randoms += 1
        aleatorio = self.seed / M
        return (b - a) * aleatorio + a

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

    def start(self, time: float):
        self.run(time)
        while not self.end:
            self.run(self.tempo)


if __name__ == '__main__':
    seeds = [12345, 1212, 127, 66235, 45]

    total1 = 0
    perdas1 = 0
    medias1 = [0, 0, 0, 0, 0, 0]

    total2 = 0
    perdas2 = 0
    medias2 = [0, 0, 0, 0, 0, 0]

    for seed in seeds:
        fila1 = Fila(1, 5, (2, 4), (3, 5), 1000, seed)
        fila1.start(3.0)
        medias1 = list(map(lambda a, b: a+b, fila1.tempo_estados, medias1))
        perdas1 += fila1.perdidos
        total1 += fila1.tempo

        fila2 = Fila(2, 5, (2, 4), (3, 5), 1000, seed)
        fila2.start(3.0)
        medias2 = list(map(lambda a, b: a+b, fila2.tempo_estados, medias2))
        perdas2 += fila2.perdidos
        total2 += fila2.tempo

        print("\n", fila2.tempo_estados)
        print(medias2)
        print(total2)

    print('*****************************************************************************************************')
    print(' Queue: Q1 (G/G/1/5)')
    print(' Arrival: 2 ... 4')
    print(' Service: 3 ... 5')
    print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
    i = 0
    for media in medias1:
        print(f"{i} :  {(media/total1)*100}")
        i += 1

    print("\nPerdas:", perdas1)

    print('*****************************************************************************************************')
    print(' Queue: Q2 (G/G/2/5)')
    print(' Arrival: 2 ... 4')
    print(' Service: 3 ... 5')
    print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
    i = 0
    for media in medias2:
        print(f"{i} :  {(media/total2)*100}")
        i += 1

    print("\nPerdas:", perdas2)
