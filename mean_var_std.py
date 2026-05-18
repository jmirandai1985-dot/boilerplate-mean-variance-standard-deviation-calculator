import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    matriz = np.array(list).reshape(3, 3)
    
    calculos = {
        'mean': [matriz.mean(axis=0).tolist(), matriz.mean(axis=1).tolist(), matriz.flatten().mean().tolist()],
        'variance': [matriz.var(axis=0).tolist(), matriz.var(axis=1).tolist(), matriz.flatten().var().tolist()],
        'standard deviation': [matriz.std(axis=0).tolist(), matriz.std(axis=1).tolist(), matriz.flatten().std().tolist()],
        'max': [matriz.max(axis=0).tolist(), matriz.max(axis=1).tolist(), matriz.flatten().max().tolist()],
        'min': [matriz.min(axis=0).tolist(), matriz.min(axis=1).tolist(), matriz.flatten().min().tolist()],
        'sum': [matriz.sum(axis=0).tolist(), matriz.sum(axis=1).tolist(), matriz.flatten().sum().tolist()]
    }
    
    return calculos
