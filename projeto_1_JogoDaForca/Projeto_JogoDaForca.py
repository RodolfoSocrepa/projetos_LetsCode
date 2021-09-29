import random # Biblioteca para usar o 'choice' para selecionar a palavra aleatória
import os #Biblioteca para ulitizar o comando cls para limpar o terminal

#Função para ilustrar a forca
#Imprime na tela o boneco conforme os erros
def forca(erro):
    os.system('cls')
    print('---------- JOGO DA FORCA ----------')
    if erro == 0:
        print('+---+')
        print('|   |')
        print('|')
        print('|')
        print('|')
     
    elif erro == 1:
        print('+---+')
        print('|   |        ', [l.upper() for l in letrasIncorretas])
        print('|   O')
        print('|')
        print('|')
     
    elif erro == 2:
        print('+---+')
        print('|   |        ', [l.upper() for l in letrasIncorretas])
        print('|   O')
        print('|   |')
        print('|')
      
    elif erro == 3:
        print('+---+')
        print('|   |        ', [l.upper() for l in letrasIncorretas])
        print('|   O')
        print('|  /|')
        print('|')
      
    elif erro == 4:
        print('+---+')
        print('|   |        ', [l.upper() for l in letrasIncorretas])
        print('|   O')
        print('|  /|\\')
        print('|')
    
    elif erro == 5:
        print('+---+')
        print('|   |        ', [l.upper() for l in letrasIncorretas])
        print('|   O')
        print('|  /|\\')
        print('|  / ')

    elif erro == 6:
        print('+---+')
        print('|   |        ', [l.upper() for l in letrasIncorretas])
        print('|   X')
        print('|          VOCÊ FOI ENFORCADO ! GAME OVER')
        print('|  /|\\     A PALAVRA ERA: ', ''.join(palavra).upper())       
        print('|  / \\')
    
# Função para validar as letras digitadas
def validacaoLetra(letra): 
    letra = str(input('Digite uma letra: ')).lower()
    while len(letra) != 1:# Valida se tem mais de uma letra ou apenas espaço
        if len(letra) == 0:
           letra = str(input('Digite uma letra: ')).lower()
        else:
            letra = str(input('Digite apenas UMA letra: ')).lower()
    
    while (letra in letrasIncorretas) or (letra in letrasCorretas):# Valida se a letra ja foi digitada
        letra = str(input('VOCÊ JA DIGITOU ESSA LETRA ! Digite OUTRA letra: ')).lower()
        while len(letra) != 1:
            if len(letra) == 0:
                letra = str(input('Digite uma letra: ')).lower()
            else:
                letra = str(input('Digite apenas UMA letra: ')).lower()

    while not 97 <= ord(letra) <= 122: # Valida se o caracter digitado é valido
        letra = str(input('\nCOMANDO INVALIDO! Digite uma letra: ')).lower()
        while len(letra) != 1:
            if len(letra) == 0:
                letra = str(input('Digite uma letra: ')).lower()
            else:
                letra = str(input('Digite apenas UMA letra: ')).lower()
        
    return letra

# Função para validar o palpite/chute
def palpite(opçao):
    while opçao != 's' and opçao != 'n':
            opçao = str(input('Digite uma opção valida! Você gostaria de chutar? [S/N]')).lower()
    if opçao == 's':
        chute = list(input('Digite o seu palpite: '))
        if chute == palavra:
            print('PARABENS VOCÊ GANHOU! A PALAVRA ERA :', ''.join(palavra).upper())
            return chute
        else:
            print('VOCÊ ERROU ! TENTE NOVAMENTE')   




listaPalavras = ['mesa''cadeira', 'banco','exceto','mister', 'vereda', 'apogeu', 'utopia', 'escopo','casual', 
                'pressa','alheio', 'nocivo', 'infame', 'hostil', 'idiota','legado', 'gentil', 'adorno','aferir', 'astuto',
                'difuso', 'formal', 'apreço', 'solene', 'limiar', 'ocioso', 'julgar', 'outrem', 'ensejo', 'eficaz','alento', 
                'escusa', 'dispor', 'embora', 'larica', 'safado', 'abster','perene', 'acento', 'isento', 'nuance', 'objeto',  
                'sisudo', 'acesso', 'receio', 'remoto', 'mazela', 'avidez', 'vulgar', 'axioma', 'buscar', 'ciente', 'desejo', 
                'alocar', 'asseio', 'anseio','eximir']

palavra = ''
erro = 0
letrasCorretas = []
letrasIncorretas = []
letra = ''
opçao = 'n'
chute = ''

palavra = random.choice(listaPalavras)

for i in range(0, len(palavra)): #cria uma lista com os "_" para posteriormente ser prenchida com as letras
    letrasCorretas.append('_')

os.system('cls')
forca(erro)
print(letrasCorretas)
print('\n')

while erro < 6:
    
    letra = validacaoLetra(letra)

    if letra not in palavra: 
        erro += 1
        letrasIncorretas.append(letra)
        os.system('cls')
        forca(erro)
        print([l.upper() for l in letrasCorretas])
        if erro < 6:
            print('VOCÊ ERROU ! TENTE NOVAMENTE')
        print('\n')

    else:
        for index in range(0, len(palavra)):
            if letra == palavra[index]:
                letrasCorretas[index] = letra
        os.system('cls')      
        forca(erro) 
        print([l.upper() for l in letrasCorretas])
        print('\n')
        if letrasCorretas == list(palavra):
            print('PARABENS VOCÊ GANHOU! A PALAVRA ERA :', ''.join(palavra).upper())
            break

        opçao = str(input('Você gostaria de chutar? [S/N]')).lower()
        chuteCerto = palpite(opçao)
        if chuteCerto == palavra:
            break
        
print('FIM')
