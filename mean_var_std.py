import numpy as np

def calcular(lista):
    if len(lista) != 9:
        raise ValueError("La lista debe contener nueve números.")
    
    matriz = np.array(lista).reshape(3, 3)
    
    calculos = {
        'media': [
            matriz.mean(axis=0).tolist(), 
            matriz.mean(axis=1).tolist(), 
            matriz.flatten().mean().tolist()
        ],
        'varianza': [
            matriz.var(axis=0).tolist(), 
            matriz.var(axis=1).tolist(), 
            matriz.flatten().var().tolist()
        ],
        'desviacion estandar': [
            matriz.std(axis=0).tolist(), 
            matriz.std(axis=1).tolist(), 
            matriz.flatten().std().tolist()
        ],
        'maximo': [
            matriz.max(axis=0).tolist(), 
            matriz.max(axis=1).tolist(), 
            matriz.flatten().max().tolist()
        ],
        'minimo': [
            matriz.min(axis=0).tolist(), 
            matriz.min(axis=1).tolist(), 
            matriz.flatten().min().tolist()
        ],
        'suma': [
            matriz.sum(axis=0).tolist(), 
            matriz.sum(axis=1).tolist(), 
            matriz.flatten().sum().tolist()
        ]
    }
    
    return calculos
