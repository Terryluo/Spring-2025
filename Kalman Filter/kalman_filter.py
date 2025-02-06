from matrix import *

measurements = [1, 2, 3]

x = matrix([[0.], [0.]]) # initial state (Location and velocity) -> estimate
P = matrix([[1000., 0.], [0., 1000.]]) # initial uncertainty -> uncertainty covariance
u = matrix([[0.], [0.]]) # external motion (now we are ignoring it) -> motion vector
F = matrix([[1., 1.],[0, 1.]]) # next state function -> state transition matrix
H = matrix([[1., 0]]) # measurement function -> measurement function
R = matrix([[1.]]) # measurement uncertainty -> measurement noise
I = matrix([[1., 0], [0, 1.]]) # identity matrix


def kalman_filter(x, P):
    for i in range(len(measurements)):
        # measurement update
        Z = matrix([[measurements[i]]]) # 1
        y = Z - (H * x) # 1.0
        S = H * P * H.transpose() + R # 1001
        K = P * H.transpose() * S.inverse() # Kalman gain
        x = x + (K * y) # back to my next prediction -> x' = x + K * y

        P = (I - (K * H)) * P # my measurement update -> P' = (I - K * H) * P

        # prediction
        x = (F * x) + u # x' = Fx + u
        P = F * P * F.transpose() # P' = F * P * F ^ T

        print('x = ')
        x.show()
        print('P = ')
        P.show()

    return [x, P]


print(kalman_filter(x, P))