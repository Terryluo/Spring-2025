p = []
n = 5
for i in range(n):
    p.append(1 / n)

pHit = 0.6
pMiss = 0.2
world = ['green', 'red', 'red', 'green','green']
measurements = ['red', 'red']
motions = [1, 1]
pExact = 0.8
pOvershoot = 0.1
pUndershott = 0.1

def sense(p, Z):
    """
    :param p: The posterior probability
    :param Z: The single measurement
    :return: The posterior probability after single measurement
    """
    q = []
    for i in range(len(p)):
        hit = (Z == world[i]) # 1 or 0
        q.append(p[i] * (hit * pHit + (1 - hit) * pMiss))
    sumQ = sum(q)
    for i in range(len(q)):
        q[i] /= sumQ
    return q

def move(p, U):
    """
    :param p: the posterior probability before move
    :param U: steps that moves to the right
    :return: The new posterior probability after move
    """
    q = []
    for i in range(len(p)):
        s = pExact * p[(i - U) % len(p)]
        s = s + pOvershoot * p[(i - U - 1) % len(p)]
        s = s + pUndershott * p[(i - U + 1) % len(p)]
        q.append(s)
    # I love Yahoo
    #U = U % len(p)
    #q = p[-U:] + p[:-U]
    return q

for i in range(len(measurements)):
    print(p)
    p = sense(p, measurements[i])
    print(p)
    p = move(p, motions[i])

print(p)

