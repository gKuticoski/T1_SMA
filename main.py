import random


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

    def chegada(self, new_time: float):
        self.tempo_estados[self.fila] += new_time - self.tempo
        self.tempo = new_time
        if self.fila < self.K:
            self.fila += 1
            if self.fila <= self.C:
                self.agendar('saida')

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
        return (b - a) * random.random() + a

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

        print(f'Tempo: {self.tempo} {self.tempo_estados}')
        if not self.end:
            self.run(self.tempo)


if __name__ == '__main__':
    fila = Fila(1, 3, (1, 2), (3, 6), 7)
    fila.run(2.0)
    print(fila.tempo)
