def Transformar(camino):
    movimientos = []
    if camino is None:
        return None
    else:
        for i in range(0, len(camino)-1):
            if camino[i+1][0] - camino[i][0] < 0:
                movimientos.append("arriba")
            elif camino[i+1][0] - camino[i][0] > 0:
                movimientos.append("abajo")
            elif camino[i+1][1] - camino[i][1] > 0:
                movimientos.append("derecha")
            elif camino[i+1][1] - camino[i][1] < 0:
                movimientos.append("izquierda")
        return movimientos

def Agente_DFS(laberinto):
    costo = 0
    stack = []
    visitados = []
    camino_corto = None
    stack.append((laberinto.start_x, laberinto.start_y, []))
    while len(stack) > 0:
        xpos, ypos, camino = stack.pop()
        costo += 1
        if xpos == laberinto.end_x and ypos == laberinto.end_y:
            if camino_corto is None or len(camino + [(xpos, ypos)]) < len(camino_corto):
                camino_corto = camino + [(xpos, ypos)]
        if (xpos, ypos) not in visitados:
            visitados.append((xpos, ypos))
            # Sentido Horario
            if xpos - laberinto.matriz[xpos][ypos] >= 0:
                stack.append((xpos - laberinto.matriz[xpos][ypos], ypos, camino + [(xpos, ypos)]))
            if ypos + laberinto.matriz[xpos][ypos] < laberinto.n:
                stack.append((xpos, ypos + laberinto.matriz[xpos][ypos], camino + [(xpos, ypos)]))
            if xpos + laberinto.matriz[xpos][ypos] < laberinto.m:
                stack.append((xpos + laberinto.matriz[xpos][ypos], ypos, camino + [(xpos, ypos)]))
            if ypos - laberinto.matriz[xpos][ypos] >= 0:
                stack.append((xpos, ypos - laberinto.matriz[xpos][ypos], camino + [(xpos, ypos)]))
    return Transformar(camino_corto), costo

def Agente_BFS(laberinto):
    costo = 0
    queue = []
    visitados = []
    queue.append((laberinto.start_x, laberinto.start_y, []))
    while len(queue) > 0:
        xpos, ypos, camino = queue.pop(0)
        costo += 1
        if xpos == laberinto.end_x and ypos == laberinto.end_y:
            return Transformar(camino + [(xpos, ypos)]), costo
        if (xpos, ypos) not in visitados:
            visitados.append((xpos, ypos))
            # Sentido Horario
            if xpos - laberinto.matriz[xpos][ypos] >= 0:
                queue.append((xpos - laberinto.matriz[xpos][ypos], ypos, camino + [(xpos, ypos)]))
            if ypos + laberinto.matriz[xpos][ypos] < laberinto.n:
                queue.append((xpos, ypos + laberinto.matriz[xpos][ypos], camino + [(xpos, ypos)]))
            if xpos + laberinto.matriz[xpos][ypos] < laberinto.m:
                queue.append((xpos + laberinto.matriz[xpos][ypos], ypos, camino + [(xpos, ypos)]))
            if ypos - laberinto.matriz[xpos][ypos] >= 0:
                queue.append((xpos, ypos - laberinto.matriz[xpos][ypos], camino + [(xpos, ypos)]))
    return None, costo