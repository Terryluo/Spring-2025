colors = [['G', 'G', 'G'],
          ['G', 'R', 'R'],
          ['G', 'G', 'G']]
measurements = ['R']
motions = [[0, 0]]

sensor_right = 1.0
p_move = 1.0






def localize(colors, measurements, motions, sensor_right, p_move):
    if len(measurements) != len(motions):
        raise ValueError("error in size of measurement/motion vector")

    pinit = 1.0 / (float(len(colors)) * float(len(colors[0])))
    p = [[pinit for col in range(len(colors[0]))] for row in range(len(colors))]

    for k in range(len(measurements)):
        p = move(p, motions[k], p_move)
        p = sense(p, colors, measurements[k], sensor_right)
    #show(p)
    return p

def sense(p, colors, measurement, sensor_right):
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



def move(p, motion, p_move):
    """
    :param p: the posterior probability before move
    :param U: steps that moves to the right
    :return: The new posterior probability after move
    """
    aux = [[0.0 for col in range(len(p[0]))] for row in range(len(p))]
    for i in range(len(p)):
        for j in range(len(p[i])):
            aux[i][j] = (p_move * p[(i - motion[0]) % len(p)][(j - motion[1]) % len(p[i])]
                         + (1 - p_move) * p[i][j])
    return aux

def show(p):
    '''
    :param p:
    :return:
    '''
    rows = ['[' + ','.join(map(lambda x: '{0: .5f}'.format(x), r)) + ']' for r in p]
    print('[' + ',\n '.join(rows) + ']')

localize(colors, measurements, motions, sensor_right, p_move)