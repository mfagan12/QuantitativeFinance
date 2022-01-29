from importlib_metadata import operator
from scipy.stats import norm, lognorm, bernoulli
from numpy import append as np_append
from numpy import exp as np_exp
from itertools import accumulate
from operator import mul

def simple_random_walk(size=100, step=0.1, start_value=0, p=0.5):
    draws = 2*bernoulli.rvs(p=0.5, size=size-1) - 1
    process = [i for i in accumulate(np_append([start_value,], draws))]
    
    return process

def brownian_motion(size=100, drift=0, volatility=1, step=0.1, start_value=0):
    '''
    Simulate a 1-D Brownian motion.
    
    Arguments:
    size -- number of points to simulate
    drift -- mean of increments per time step
    volatility -- variance of increments per time step
    step -- step size of increments
    '''
    draws = norm.rvs(loc=step*drift, scale=step*volatility, size=size-1)
    process = [i for i in accumulate(np_append([start_value,], draws))]
    
    return process, draws

def geometric_brownian_motion(size=100,
                              drift=0,
                              volatility=1,
                              step=0.1,
                              start_value=1):
    '''
    Simulate a 1-D geometric Brownian motion.
    
    Arguments:
    size -- number of points to simulate
    drift -- mean of increments per time step
    volatility -- variance of increments per time step
    step -- step size of increments
    '''
    draws = lognorm.rvs(scale=np_exp(step*drift), s=step*volatility, size=size-1)
    process = [i for i in accumulate(np_append([start_value,], draws),
                                     func=operator.mul)]
    
    return process, draws

def white_noise(size=100, variance=1, step=0.1):
    process = norm.rvs(scale=step*variance, size=size)
    
    return process