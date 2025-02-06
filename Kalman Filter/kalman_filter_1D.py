measurements = [5., 6., 7., 9., 10.]
motion = [1., 1., 2., 1., 1.]
measurement_sig = 4. #sigma for measurement
motion_sig = 2. # sigma for motion
mu = 0. #initial mu
sig = 0.000001 # initial sigma

def kalman_filter_1D(mu, sig):
    for i in range(len(motion)):
        [mu, sig] = update(mu, sig, measurements[i], measurement_sig)
        print('Update: ', [mu, sig])
        [mu, sig] = predict(mu, sig, motion[i], motion_sig)
        print('Predict: ', [mu, sig])
    return [mu, sig]


def update(mean1, var1, mean2, var2):
    '''
    update new mean and new variance given the mean and variance of the prior belief and
    the mean and variance of the measurement
    :param var1: variance of the prior belief
    :param mean2:

    :param mean2:
    :param var2:
    :return:
    '''
    new_mean = (mean1 * var2 + mean2 * var1) / (var1 + var2)
    new_var = 1 / (1 / var1 + 1 / var2)
    return [new_mean, new_var]

def predict(mean1, var1, mean2, var2):
    '''
    predict new mean and new variance given the mean and variance of the prior belief and
    the mean and variance of the motion
    :param mean1: mean of the prior belief
    :param var1: variance of the prior belief
    :param mean2: mean of the motion
    :param var2: variance of the motion
    :return:
    '''
    new_mean = mean1 + mean2
    new_var = var1 + var2
    return [new_mean, new_var]

#[mu, sig] = kalman_filter_1D(0, 1000.)
[mu, sig] = kalman_filter_1D(5, 0.000001)