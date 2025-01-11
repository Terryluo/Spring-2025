colors = [['G', 'G', 'G'],
          ['G', 'R', 'R'],
          ['G', 'G', 'G']]
measurements = ['R']
motions = [[0, 0]]

sensor_right = 0.8
p_move = 1.0
p = [[1.0 for col in range(len(colors[0]))] for row in range(len(colors))]

def localize(colors, measurements, motions, sensor_right, p_move):
    for i in range(len(motions)):
        pos = move(p, motions[i])
        pos = sense(p, colors, measurements[i])
    return pos

def sense(p, colors, measurement):
    """
    :param p: The posterior probability
    :param Z: The single measurement
    :return: The posterior probability after single measurement
    """
    aux = [[0.0 for col in range(len(p[0]))] for row in range(len(p))]

    s = 0.0
    for i in range(len(p)):
        for j in range(len(p[i])):
            hit = (measurement == colors[i][j])  # 1 or 0
            aux[i][j] = p[i][j] * (hit * sensor_right + (1 - hit) * (1 - sensor_right))
            s += aux[i][j]
    for i in range(len(aux)):
        for j in range(len(p[i])):
            aux[i][j] /= s
    return aux



def move(p, motion):
    """
    :param p: the posterior probability before move
    :param U: steps that moves to the right
    :return: The new posterior probability after move
    """
    aux = [[0.0 for col in range(len(p[0]))] for row in range(len(p))]
    for i in range(len(p)):
        for j in range(len(p[i])):
            aux[i][j] = (p_move * p[(i - motion[0]) % len(p)][(j - motion[1]) % len(p[i])]
                         + (1 - p_move) * p[(i - motion[0]) % len(p)][(j - motion[1]) % len(p[i])])
    return aux


print(localize(colors, measurements, motions, sensor_right, p_move))