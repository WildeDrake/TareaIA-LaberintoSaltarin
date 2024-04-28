import Agentes
import Partida
import Dibujar
import Controles

import pygame
import argparse


def main(filename, m, n, modo):
    partida = Partida.Partida(filename, n, m)
    pygame.init()
    running = True
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption('Laberinto saltarín')

    if modo == 1:
        movs, costo = Agentes.Agente_DFS(partida.laberinto)
        print("Búsqueda DFS")
    if modo == 2:
        print("Búsqueda BFS")
        movs, costo = Agentes.Agente_BFS(partida.laberinto)
    if modo == 1 or modo == 2:
        if movs is not None:
            print("Camino mas corto: " + str(movs) + "\n" + "Largo del camino: " + str(len(movs)) + "\n" + "Casillas visitadas: " + str(costo))
        else:
            print("No hay solución")
            running = False
    if modo == 3:
        movs1, costo1 = Agentes.Agente_DFS(partida.laberinto)
        movs2, costo2 = Agentes.Agente_BFS(partida.laberinto)
        if movs1 is not None:
            print("Largo del camino: "+str(len(movs1))+"\n"+"Casillas visitadas por DFS: "+str(costo1)+"\n"+"Casillas visitadas por BFS: "+str(costo2))
        else:
            print("No hay solución")
        running = False

    while running is True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if partida.win() is False:
            Dibujar.dibujar_partida(screen, partida)
            if modo == 0:
                partida.mover(Controles.controles())
            else:
                pygame.time.wait(1000)
                partida.mover(movs.pop(0))
        else:
            Dibujar.dibujar_victoria(screen, partida)
        pygame.time.Clock().tick(60)
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Procesa algunos argumentos.')
    parser.add_argument('--filename', type=str, help='Un string para el argumento filename')
    parser.add_argument('--n', type=int, help='Un entero para el argumento n')
    parser.add_argument('--m', type=int, help='Un entero para el argumento m')
    parser.add_argument('--modo', type=int, help='Un entero para el argumento modo')
    args = parser.parse_args()
    main(args.filename, args.n, args.m, args.modo)