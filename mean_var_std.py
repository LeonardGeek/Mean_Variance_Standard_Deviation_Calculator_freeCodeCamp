import numpy as np

def calculate(list):
    if((len(list)) != 9):
        raise ValueError('List must contain nine numbers.')
    arr = np.array(list).reshape(3,3)
    mean_list = [arr.mean(axis=0).tolist(), arr.mean(axis=1).tolist(),  arr.mean()]
    variance_list = [arr.var(axis=0).tolist(), arr.var(axis=1).tolist(), arr.var()]
    standard_deviation_list = [arr.std(axis=0).tolist(), arr.std(axis=1).tolist(), arr.std()]
    max_list = [arr.max(axis=0).tolist(), arr.max(axis=1).tolist(), arr.max()]
    min_list = [arr.min(axis=0).tolist(), arr.min(axis=1).tolist(), arr.min()]
    sum_list = [arr.sum(axis=0).tolist(), arr.sum(axis=1).tolist(), arr.sum()]
    
    calculations = {'mean' : mean_list,
            'variance' : variance_list,
            'standard deviation' : standard_deviation_list,
            'max' : max_list,
            'min' : min_list,
            'sum' : sum_list
            }
    return calculations