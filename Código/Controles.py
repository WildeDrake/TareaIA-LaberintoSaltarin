import pygame


lastkey = None
def controles():
    global lastkey
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and lastkey != pygame.K_UP:
        lastkey = pygame.K_UP
        return "arriba"
    if keys[pygame.K_w] and lastkey != pygame.K_w:
        lastkey = pygame.K_w
        return "arriba"

    if keys[pygame.K_DOWN] and lastkey != pygame.K_DOWN:
        lastkey = pygame.K_DOWN
        return "abajo"
    if keys[pygame.K_s] and lastkey != pygame.K_s:
        lastkey = pygame.K_s
        return "abajo"

    if keys[pygame.K_LEFT] and lastkey != pygame.K_LEFT:
        lastkey = pygame.K_LEFT
        return "izquierda"
    if keys[pygame.K_a] and lastkey != pygame.K_a:
        lastkey = pygame.K_a
        return "izquierda"

    if keys[pygame.K_RIGHT] and lastkey != pygame.K_RIGHT:
        lastkey = pygame.K_RIGHT
        return "derecha"
    if keys[pygame.K_d] and lastkey != pygame.K_d:
        lastkey = pygame.K_d
        return "derecha"

    if not any(keys):
        lastkey = None

    return None