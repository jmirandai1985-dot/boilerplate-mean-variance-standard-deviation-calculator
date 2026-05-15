import numpy as np

def calculate(list):
    # 1. Validar que la lista tenga exactamente 9 elementos
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    # 2. Convertir la lista en una matriz NumPy de 3x3
    matrix = np.array(list).reshape(3, 3)
    
    # 3. Realizar los cálculos usando los ejes de NumPy (axis 0 = columnas, axis 1 = filas)
    calculations = {
        'mean': [matrix.mean(axis=0).tolist(), matrix.mean(axis=1).tolist(), matrix.flatten().mean().tolist()],
        'variance': [matrix.var(axis=0).tolist(), matrix.var(axis=1).tolist(), matrix.flatten().var().tolist()],
        'standard deviation': [matrix.std(axis=0).tolist(), matrix.std(axis=1).tolist(), matrix.flatten().std().tolist()],
        'max': [matrix.max(axis=0).tolist(), matrix.max(axis=1).tolist(), matrix.flatten().max().tolist()],
        'min': [matrix.min(axis=0).tolist(), matrix.min(axis=1).tolist(), matrix.flatten().min().tolist()],
        'sum': [matrix.sum(axis=0).tolist(), matrix.sum(axis=1).tolist(), matrix.flatten().sum().tolist()]
    }
    
    return calculations
