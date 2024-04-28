import random


class Laberinto:
    def __init__(self, filename=None, n=None, m=None):
        if filename:
            with open(filename, "r") as file:
                while True:
                    header = file.readline().strip()
                    if header == '0':
                        break
                    self.m, self.n, self.start_x, self.start_y, self.end_x, self.end_y = map(int, header.split())
                    self.matriz = []
                    for _ in range(self.m):
                        self.matriz.append(list(map(int, file.readline().strip().split())))
                    self.matriz[self.end_x][self.end_y] = 0
        elif m and n:
            self.m = m
            self.n = n
            self.start_x, self.start_y = random.randint(0, m-1), random.randint(0, n-1)
            self.end_x, self.end_y = random.randint(0, m-1), random.randint(0, n-1)
            while self.start_x == self.end_x and self.start_y == self.end_y:
                self.end_x, self.end_y = random.randint(0, m-1), random.randint(0, n-1)
            self.matriz = []
            p = min(n, m)
            for i in range(self.n):
                self.matriz.append([])
                for j in range(self.m):
                    self.matriz[i].append(random.randint(1, p-1))
            self.matriz[self.end_x][self.end_y] = 0
        else:
            raise ValueError("Proporcionar un archivo o las dimensiones del laberinto.")