import unittest
from instagram_grafos import Instagram
import csv

arquivoCsvUsuarios = r'C:\Users\Samsung\ProjetosPython\projetos_Curso_LetsCode\projeto_4_Instagram_grafos\usuarios.csv'
arquivoCsvConexoes = r'C:\Users\Samsung\ProjetosPython\projetos_Curso_LetsCode\projeto_4_Instagram_grafos\conexoes.csv'

class Testes(unittest.TestCase):
    def setUp(self) -> None:
        self.insta = Instagram()
        

    def testeCriarUser(self):
        print('\nTeste para CRIAR os usuários que estão no arquivo')
        self.assertEqual(self.insta.criaUser(arquivoCsvUsuarios), (100))

    def testeCriarUserArquivoNaoAbre(self):
        arquivoCsvUsuarios = r'C:\Users\Samsung\ProjetosPython\projetos_Curso_LetsCode\projeto_4_Instagram_grafos.csv'
        print('\nTeste para CRIAR os usuários, com caminho do arquivo inválido')
        self.assertEqual(self.insta.criaUser(arquivoCsvUsuarios), (0))

    def testeConectaUsuarios(self):
        print('\nTeste para CONECTAR os usuários que estão no arquivo')
        self.insta.criaUser(arquivoCsvUsuarios)
        self.assertEqual(self.insta.conect(arquivoCsvConexoes), (1))

    def testeConectarUserArquivoNaoAbre(self):
        arquivoCsvConexoes = r'C:\Users\Samsung\ProjetosPython\projetos_Curso_LetsCode\projeto_4_Instagram_grafos.csv'
        print('\nTeste para CONECTAR os usuários, com caminho do arquivo inválido')
        self.assertEqual(self.insta.criaUser(arquivoCsvConexoes), (0))

    def testeExibirQtdSeguidoresUsuarioInvalido(self):
        print('\nTeste para EXIBIR a quantidade dos seguidores passando um usuário inexistente.')
        self.insta.criaUser(arquivoCsvUsuarios)
        self.insta.conect(arquivoCsvConexoes)
        self.assertEqual(self.insta.exibirQtdSeguidores('rodolfo10'), (0))

    def testeExibirQtdSeguidoresUsuario(self):
        print('\nTeste para EXIBIR a quantidade dos seguidores de um usuário.')
        self.insta.criaUser(arquivoCsvUsuarios)
        self.insta.conect(arquivoCsvConexoes)
        self.assertEqual(self.insta.exibirQtdSeguidores('helena42'), (18))

    def testeExibirQtdSeguidosUsuarioInvalido(self):
        print('\nTeste para EXIBIR a quantidade de seguidos passando um usuário inexistente.')
        self.insta.criaUser(arquivoCsvUsuarios)
        self.insta.conect(arquivoCsvConexoes)
        self.assertEqual(self.insta.exibirQtdSeguidos('rodolfo10'), (0))

    def testeExibirQtdSeguidosUsuario(self):
        print('\nTeste para EXIBIR a quantidade dos seguidos de um usuário.')
        self.insta.criaUser(arquivoCsvUsuarios)
        self.insta.conect(arquivoCsvConexoes)
        self.assertEqual(self.insta.exibirQtdSeguidos('helena42'), (16))

    def testeOrdenaStoriesUsuarioInvalido(self):
        print('\nTeste para ORDENAR o Stories passando um usuário inválido.')
        self.insta.criaUser(arquivoCsvUsuarios)
        self.insta.conect(arquivoCsvConexoes)
        self.assertEqual(self.insta.ordenaStories('rodolfo10'), (0))

    def testeOrdenaStories(self):
        print('\nTeste para ORDENAR o Stories')
        self.insta.criaUser(arquivoCsvUsuarios)
        self.insta.conect(arquivoCsvConexoes)
        self.assertEqual(self.insta.ordenaStories('helena42'), (['ana_julia22', 'pietro33', ['alice43', 'ana_clara30', 'calebe49', 'caua11', 'davi48', 'gustavo16', 'heloisa37', 'lavinia36','mariana5', 'matheus6', 'melissa42', 'nicolas4', 'rafael38', 'sophia31']]))

    def testeTopInfluencersValorInvalido(self):
        print('\nTeste para verificar os top influencers passando um valor inválido')
        self.insta.criaUser(arquivoCsvUsuarios)
        self.insta.conect(arquivoCsvConexoes)
        self.assertEqual(self.insta.topInfluencers(-1), (0))

    def testeTopInfluencers(self):
        print('\nTeste para verificar os top influencers.')
        self.insta.criaUser(arquivoCsvUsuarios)
        self.insta.conect(arquivoCsvConexoes)
        self.assertEqual(self.insta.topInfluencers(6), ([['maria_alice19', 24], ['alice43', 22], ['isis3', 22], ['miguel1', 22], ['lorena21', 21], ['henrique12', 21]]))

    def testeEncontraCaminhoUsuariosSemConexao(self):
        print('\nTeste para verificar o camiho entre dois usuários que NÃO tem conexão.')
        self.insta.criaUser(arquivoCsvUsuarios)
        self.insta.conect(arquivoCsvConexoes)
        self.assertEqual(self.insta.encontraCaminho('helena42', 'rodolfo10'), (False))

    def testeEncontraCaminhoUsuarios(self):
        print('\nTeste para verificar o camiho entre dois usuários.')
        self.insta.criaUser(arquivoCsvUsuarios)
        self.insta.conect(arquivoCsvConexoes)
        self.assertEqual(self.insta.encontraCaminho('helena42', 'yasmin46'), (['helena42', 'caua11', 'yasmin46']))

if __name__ == '__main__':
    unittest.main() 