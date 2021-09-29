def merge(contSeguidores):

    if len(contSeguidores) > 1:# Condição de parada da recursão

        meio = len(contSeguidores) // 2
        left = contSeguidores[:meio]
        right = contSeguidores[meio:]

        merge(left)
        merge(right)
        
        cursorLeft = 0
        cursorRight = 0
        cursorlista = 0

        # Enquanto o cursor left e right não chegarem ao fim (None), continua no laço acrescentado na lista o menor valor.
        while cursorLeft < len(left) and cursorRight < len(right):
    
            if left[cursorLeft][1] >= right[cursorRight][1]:
                contSeguidores[cursorlista] = (right[cursorRight])
                cursorlista += 1
                cursorRight += 1

            elif left[cursorLeft][1] <= right[cursorRight][1]:
                contSeguidores[cursorlista] = left[cursorLeft]
                cursorlista += 1
                cursorLeft += 1
            
        #Enquanto o cursor esquerdo não chegar no fim, continua avançando e acrescentando o elemento na lista.
        while cursorLeft < len(left):
            contSeguidores[cursorlista] = left[cursorLeft]
            cursorlista += 1
            cursorLeft += 1

        #Enquanto o cursor esquerdo não chegar no fim, continua avançando e acrescentando o elemento na lista.
        while cursorRight < len(right):
            contSeguidores[cursorlista] = right[cursorRight]
            cursorlista += 1
            cursorRight += 1

    return contSeguidores[::-1]

def bubleSort(lista):
    
    for i in range(len(lista)-1):
        for j in range(len(lista)-1 -i):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

    return lista  

