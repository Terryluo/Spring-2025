from Localization_Program import localize

# test 1
colors = [['G', 'G', 'G'],
          ['G', 'R', 'G'],
          ['G', 'G', 'G']]
measurements = ['R']
motions = [[0,0]]
sensor_right = 1.0
p_move = 1.0
p = localize(colors,measurements,motions,sensor_right,p_move)
assert p == [[0.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 0.0]]

# test 2
colors = [['G', 'G', 'G'],
          ['G', 'R', 'R'],
          ['G', 'G', 'G']]
measurements = ['R']
motions = [[0,0]]
sensor_right = 1.0
p_move = 1.0
p = localize(colors,measurements,motions,sensor_right,p_move)
assert p == (
    [[0.0, 0.0, 0.0],
     [0.0, 0.5, 0.5],
     [0.0, 0.0, 0.0]])

# test 3
colors = [['G', 'G', 'G'],
          ['G', 'R', 'R'],
          ['G', 'G', 'G']]
measurements = ['R']
motions = [[0,0]]
sensor_right = 0.8
p_move = 1.0
p = localize(colors,measurements,motions,sensor_right,p_move)
assert p == (
    [[0.06666666666666667, 0.06666666666666667, 0.06666666666666667],
     [0.06666666666666667, 0.2666666666666667, 0.2666666666666667],
     [0.06666666666666667, 0.06666666666666667, 0.06666666666666667]])

# test 4
colors = [['G', 'G', 'G'],
          ['G', 'R', 'R'],
          ['G', 'G', 'G']]
measurements = ['R', 'R']
motions = [[0,0], [0,1]]
sensor_right = 0.8
p_move = 1.0
p = localize(colors,measurements,motions,sensor_right,p_move)
assert p == (
    [[0.03333333333333333, 0.03333333333333333, 0.03333333333333333],
     [0.13333333333333333, 0.13333333333333336, 0.5333333333333334],
     [0.03333333333333333, 0.03333333333333333, 0.03333333333333333]])

# test 5
colors = [['G', 'G', 'G'],
          ['G', 'R', 'R'],
          ['G', 'G', 'G']]
measurements = ['R', 'R']
motions = [[0,0], [0,1]]
sensor_right = 1.0
p_move = 1.0
p = localize(colors,measurements,motions,sensor_right,p_move)
assert p == (
    [[0.0, 0.0, 0.0],
     [0.0, 0.0, 1.0],
     [0.0, 0.0, 0.0]])

# test 6
colors = [['G', 'G', 'G'],
          ['G', 'R', 'R'],
          ['G', 'G', 'G']]
measurements = ['R', 'R']
motions = [[0,0], [0,1]]
sensor_right = 0.8
p_move = 0.5
p = localize(colors,measurements,motions,sensor_right,p_move)
assert p == (
    [[0.02898550724637681, 0.02898550724637681, 0.02898550724637681],
     [0.07246376811594203, 0.2898550724637682, 0.4637681159420291],
     [0.02898550724637681, 0.02898550724637681, 0.02898550724637681]])

# test 7
colors = [['G', 'G', 'G'],
          ['G', 'R', 'R'],
          ['G', 'G', 'G']]
measurements = ['R', 'R']
motions = [[0,0], [0,1]]
sensor_right = 1.0
p_move = 0.5
p = localize(colors,measurements,motions,sensor_right,p_move)
assert p == (
    [[0.0, 0.0, 0.0],
     [0.0, 0.3333333333333333, 0.6666666666666666],
     [0.0, 0.0, 0.0]])