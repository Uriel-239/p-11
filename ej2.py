def imprimir_arreglo(arreglo, indice=0):
    if indice == len(arreglo):
        return
    
    print(arreglo[indice])
    
    imprimir_arreglo(arreglo, indice + 1)

mi_lista = [10, 20, 30, 40, 50]
imprimir_arreglo(mi_lista)
