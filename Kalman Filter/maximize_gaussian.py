from math import *

def f(mu, sigma2, x):
    return (1 / sqrt(2 * pi * sigma2)) * exp(-0.5 * (x - mu) ** 2 / sigma2)

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

#print(f(10., 4., 10.))
print(update(10.,8.,13.,2.))