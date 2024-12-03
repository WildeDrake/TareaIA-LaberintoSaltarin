import pygame


def dibujar_partida(screen, partida):
    WIDTH, HEIGHT = screen.get_width(), screen.get_height()
    m, n = partida.laberinto.m, partida.laberinto.n
    font = pygame.font.Font(None, WIDTH // min(m, n) // 2)
    screen.fill((200, 200, 200))
    for i in range(n):
        for j in range(m):
            # Casillas
            if (i + j) % 2 == 0:
                pygame.draw.rect(screen, (150, 150, 150), (i * WIDTH // n, j * HEIGHT // m, WIDTH // n, HEIGHT // m))
            # Casilla ganadora
            if i == partida.laberinto.end_y and j == partida.laberinto.end_x:
                pygame.draw.rect(screen, (164, 247, 131), (i * WIDTH // n, j * HEIGHT // m, WIDTH // n, HEIGHT // m))
            # Jugador
            if i == partida.pos_y and j == partida.pos_x:
                pygame.draw.rect(screen, (131, 238, 247), (i * WIDTH // n, j * HEIGHT // m, WIDTH // n, HEIGHT // m))
            # Posibles movimientos
            if partida.pos_x - partida.laberinto.matriz[partida.pos_x][partida.pos_y] == j and partida.pos_y == i:
                pygame.draw.circle(screen, (250, 250, 250), (i * WIDTH // n + WIDTH // (2 * n), j * HEIGHT // m + HEIGHT // (2 * m)), WIDTH // min(m, n) // 4)
            if partida.pos_x + partida.laberinto.matriz[partida.pos_x][partida.pos_y] == j and partida.pos_y == i:
                pygame.draw.circle(screen, (250, 250, 250), (i * WIDTH // n + WIDTH // (2 * n), j * HEIGHT // m + HEIGHT // (2 * m)), WIDTH // min(m, n) // 4)
            if partida.pos_x == j and partida.pos_y - partida.laberinto.matriz[partida.pos_x][partida.pos_y] == i:
                pygame.draw.circle(screen, (250, 250, 250), (i * WIDTH // n + WIDTH // (2 * n), j * HEIGHT // m + HEIGHT // (2 * m)), WIDTH // min(m, n) // 4)
            if partida.pos_x == j and partida.pos_y + partida.laberinto.matriz[partida.pos_x][partida.pos_y] == i:
                pygame.draw.circle(screen, (250, 250, 250), (i * WIDTH // n + WIDTH // (2 * n), j * HEIGHT // m + HEIGHT // (2 * m)), WIDTH // min(m, n) // 4)
            # Números
            text = font.render(str(partida.laberinto.matriz[j][i]), True, (25, 25, 25))
            text_rect = text.get_rect(center=(i * WIDTH // n + WIDTH // (2 * n), j * HEIGHT // m + HEIGHT // (2 * m)))
            screen.blit(text, text_rect)
            # Marco de las casillas
            pygame.draw.rect(screen, (100, 100, 100), (i * WIDTH // n, j * HEIGHT // m, WIDTH // n, HEIGHT // m), 3)

def dibujar_victoria(screen, partida):
    WIDTH, HEIGHT = screen.get_width(), screen.get_height()
    screen.fill((200, 200, 200))
    font = pygame.font.Font(None, WIDTH // 10)
    text = font.render("¡Victoria!", True, (25, 25, 25))
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text, text_rect)
    text2 = font.render(f"movimientos: {partida.movimientos}", True, (25, 25, 25))
    text_rect2 = text2.get_rect(center=(WIDTH // 2, HEIGHT // 2 + HEIGHT // 10))
    screen.blit(text2, text_rect2)