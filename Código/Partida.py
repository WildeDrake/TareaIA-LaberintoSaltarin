import Laberinto


class Partida:
    def __init__(self, filename, n, m):
        self.laberinto = Laberinto.Laberinto(filename, n, m)
        self.pos_x = self.laberinto.start_x
        self.pos_y = self.laberinto.start_y
        self.movimientos = 0

    def mover(self, direccion):
        if direccion == "arriba":
            if self.pos_x - self.laberinto.matriz[self.pos_x][self.pos_y] >= 0:
                self.pos_x -= self.laberinto.matriz[self.pos_x][self.pos_y]
                self.movimientos += 1
        elif direccion == "abajo":
            if self.pos_x + self.laberinto.matriz[self.pos_x][self.pos_y] < self.laberinto.m:
                self.pos_x += self.laberinto.matriz[self.pos_x][self.pos_y]
                self.movimientos += 1
        elif direccion == "izquierda":
            if self.pos_y - self.laberinto.matriz[self.pos_x][self.pos_y] >= 0:
                self.pos_y -= self.laberinto.matriz[self.pos_x][self.pos_y]
                self.movimientos += 1
        elif direccion == "derecha":
            if self.pos_y + self.laberinto.matriz[self.pos_x][self.pos_y] < self.laberinto.n:
                self.pos_y += self.laberinto.matriz[self.pos_x][self.pos_y]
                self.movimientos += 1
        return False

    def win(self):
        if self.pos_x == self.laberinto.end_x and self.pos_y == self.laberinto.end_y:
            return True
        return False