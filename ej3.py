def cadinv(arreglo, indice=0):
    if indice == len(arreglo):
        return
    
    cadinv(arreglo, indice + 1)
    
    print(arreglo[indice], end=" ")

mi_cadena = "Recursion"
cadinv(mi_cadena)
