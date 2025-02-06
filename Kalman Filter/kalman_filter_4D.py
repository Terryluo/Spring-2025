from matrix import *

measurements = [[5., 10.]]#, [6., 8.], [7., 6.], [8., 4.], [9., 2.], [10., 0]]
initial_xy = [5., 10.]
dt = 0.1

x = matrix([[initial_xy[0]], [initial_xy[1]], [0.], [0.]]) # initial state (Location and velocity) -> estimate
u = matrix([[0.], [0.], [0.], [0.]]) # external motion (now we are ignoring it) -> motion vector
P = matrix([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1000., 0], [0, 0, 0, 1000.]]) # initial uncertainty -> uncertainty covariance
F = matrix([[1., 0, dt, 0], [0, 1., 0, dt], [0, 0, 1., 0], [0, 0, 0, 1.]]) # next state function -> state transition matrix
H = matrix([[1., 0, 0, 0], [0, 1., 0, 0]]) # measurement function -> measurement function
R = matrix([[.1, 0], [0, .1]]) # measurement uncertainty -> measurement noise
I = matrix([[1., 0, 0, 0], [0, 1., 0, 0], [0, 0, 1., 0], [0, 0, 0, 1.]]) # identity matrix


def kalman_filter(x, P):
    for i in range(len(measurements)):
        # prediction
        x = (F * x) + u  # x' = Fx + u(or 'v') in normal distribution, u ~ N(0, Q)
        P = F * P * F.transpose()  # P' = F * P * F ^ T + Q

        # measurement update
        Z = matrix([measurements[i]]) # 1
        y = Z.transpose() - (H * x) # 1.0
        S = H * P * H.transpose() + R # 1001
        K = P * H.transpose() * S.inverse() # Kalman gain
        x = x + (K * y) # back to my next prediction -> x' = x + K * y

        P = (I - (K * H)) * P # my measurement update -> P' = (I - K * H) * P



    print('x = ')
    x.show()
    print('P = ')
    P.show()

    #return [x, P]


kalman_filter(x, P)