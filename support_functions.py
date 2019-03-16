import numpy as np

def distance_matrix(data,metr):
    m , k = data.shape
    dist_matrix = np.zeros((m,m), dtype=float)

    for i in range(0,m):
        for j in range(0,m):
            dist_matrix[i,j] = metr(data.values[i,:],data.values[j,:])
            
    return dist_matrix





# deluje mi okej, samo treba raditi polovinu matrice i onda preslikati... 
# ne budi lenj kao u matlabu .. 
