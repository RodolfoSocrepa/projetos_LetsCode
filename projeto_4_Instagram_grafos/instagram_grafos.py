import csv
from mergesort_insta import merge, bubleSort


class Instagram():
    def __init__(self) -> None:
        self.matrizAdjacencia = {}

    #Le o arquivo CSV e adciona na matrizAdjacencia todos os usuários.
    def criaUser(self, arquivo):
        try:
            with open(arquivo) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                for cont, userName in enumerate(csv_reader):
                    self.matrizAdjacencia[userName[1]] = {} 

            print(f'{cont + 1} Usuários adcionados com sucesso!')
            return cont + 1

        except:
            print('Não foi possível carregar o arquivo')
            return 0

    #Le o arquivo CSV e faz a conexão dos usuários na matriz.
    def conect(self, arquivo):
        try:
            with open(arquivo) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                for usuario in csv_reader:
                    self.matrizAdjacencia[usuario[0]][usuario[1]] = usuario[2]

            print(f'Usuários conectados com sucesso!')
            return (1)

        except:
            print('Não foi possível carregar o arquivo')
            return 0

    #Retorna a quantidade de seguidores do usuário passado com parâmetno(cont=0 serve para não printar toda vez que chamo esse metódo). 
    def exibirQtdSeguidores(self, usuario, cont=0):
        
        try:
            if usuario not in self.matrizAdjacencia.keys():
                raise ValueError

            contSeguidores = sum([list(user).count(usuario) for user in self.matrizAdjacencia.values()])
            if cont == 0:
                print(f'Usuário {usuario} tem {contSeguidores} seguidores.')

            return contSeguidores
        
        except ValueError:
            print(f'Usuário {usuario} não esta cadastrado.')
            return (0)
        
    #Retorna a quantidade de usuários que são seguidos pelo usuário passado com parâmetno.
    def exibirQtdSeguidos(self, usuario):
        try:
            if usuario not in self.matrizAdjacencia.keys():
                raise ValueError

            contSeguidos = len(self.matrizAdjacencia[usuario])
            print(f'Usuário {usuario} está seguindo {contSeguidos} pessoas.')
            return contSeguidos
        
        except ValueError:
            print(f'Usuário {usuario} não esta cadastrado.')
            return (0)

    # Ordena por melhores amigos e por ordem alfabética o Stories do usuário passado como parâmetno.(bubble sort)
    def ordenaStories(self, usuario):
        listaStoriesMelhoresAmigos = []
        listaStoriesAmigos = []
      
        try:
            if usuario not in self.matrizAdjacencia.keys():
                raise ValueError

            for seguidos, flag_amigo in self.matrizAdjacencia[usuario].items():
                if flag_amigo == '2':
                    listaStoriesMelhoresAmigos.append(seguidos)
                else:
                    listaStoriesAmigos.append(seguidos)

            listaStoriesMelhoresAmigos = bubleSort(listaStoriesMelhoresAmigos)
            listaStoriesAmigos = bubleSort(listaStoriesAmigos)
            listaStoriesMelhoresAmigos.append(listaStoriesAmigos)

            print(f'Lista Stories dos amigos do usuário {usuario} : {(listaStoriesMelhoresAmigos)}')
            return listaStoriesMelhoresAmigos

        except ValueError:
            print(f'Usuário {usuario} não esta cadastrado.')
            return (0)

    # Retorna os Top Influencers (as pessoas mais seguidas). (merge sort)
    def topInfluencers(self, qtdTopInfluencers):
        contSeguidores = []
        try:
            if int(qtdTopInfluencers) < 0 or int(qtdTopInfluencers) > 100:
                raise ValueError

            for user in self.matrizAdjacencia.keys():
                contSeguidores.append([user, self.exibirQtdSeguidores(user, 1)])
            contSeguidores = merge(contSeguidores)
            #contSeguidores.sort(key=lambda x : x[1], reverse=True)
            print(f'Lista dos {qtdTopInfluencers} top Influencers: {contSeguidores[:qtdTopInfluencers]}') 
            return contSeguidores[:qtdTopInfluencers]
        
        except ValueError:
            print(f'Comando inválido! : {qtdTopInfluencers}')
            return (0)

    # Retorna o caminho entre um usuário(origem)e outro usuário (destino) passados como parâmetno.
    def encontraCaminho(self, origem, destino):
        fila = [origem]
        visitados = []
        predecessor = {origem:None}

        try:
            if origem and destino not in self.matrizAdjacencia.keys():
                raise SystemError

            while len(fila) > 0:
                primeiroElemento = fila[0]
                fila = fila[1:]
                visitados.append(primeiroElemento)
                for seguidos in self.matrizAdjacencia[primeiroElemento].keys():
                    if seguidos == destino:
                        pred = primeiroElemento
                        caminhoInvertido = [destino]
                        while pred is not None:
                            caminhoInvertido.append(pred)
                            pred = predecessor[pred]

                        print(f'O caminho do usuário {origem} até o usuário {destino} é: {caminhoInvertido[::-1]}')
                        return caminhoInvertido[::-1]

                    if seguidos not in visitados and seguidos not in fila:
                        predecessor[seguidos] = primeiroElemento
                        fila.append(seguidos)
        
        except:
            print(f'O caminho do usuário {origem} até o usuário {destino} é: NÃO EXISTE CONEXÃO') 
            return False




