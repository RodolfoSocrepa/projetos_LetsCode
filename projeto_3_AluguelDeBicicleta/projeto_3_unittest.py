import unittest
from Projeto3_AluguelBicicletas import Loja, Bicicleta, Cliente
from datetime import datetime

# Teste dos métodos - mostrarEstoque, alugar (Class - Loja)
# Teste do método - calcularValorAluguel (Class - Bicicleta)
# Teste do método - salvarDados (Clas - Cliente)
# Quantidade de bicicletas alugadas 2.
# Período total do aluguel 10 horas.
class Testes(unittest.TestCase): 
    def setUp(self):
        horaInicio = datetime(2021, 8, 25, 10, 00, 00)
        self.bicicleta = Bicicleta(100, 2, horaInicio , 'hora')
        self.cliente = Cliente('Rodolfo', 31483684873, self.bicicleta.estoqueBicicleta, self.bicicleta.quantidade, self.bicicleta.horaInicio, self.bicicleta.tipoAluguel)

    def testeMostrarQtdEstoque(self):
        print('\nTeste para MOSTRAR a quantidade em estoque.')
        self.assertEqual(self.bicicleta.mostraQtdEstoque(), (98))
    
    def testeMostrarQtdEstoqueComEstoqueLetra(self):
        horaInicio = datetime(2021, 8, 25, 10, 00, 00)
        self.bicicleta = Bicicleta('a', 2, horaInicio , 'hora')
        print('\nTeste para MOSTRAR a quantidade em estoque recebendo como parâmetro uma letra.')
        self.assertEqual(self.bicicleta.mostraQtdEstoque(), (0))

    def testeMostrarQtdEstoqueComEstoqueNegativo(self):
        horaInicio = datetime(2021, 8, 25, 10, 00, 00)
        self.bicicleta = Bicicleta(-1, 2, horaInicio , 'hora')
        print('\nTeste para MOSTRAR a quantidade em estoque recebendo como parâmetro número negativo.')
        self.assertEqual(self.bicicleta.mostraQtdEstoque(), (0))

    def testeAlugarBicicleta(self):
        print('\nTeste ALUGAR bicicleta')
        self.assertEqual(self.bicicleta.alugar(2), (98))

    def testeAlugarBicicletaValueError(self):
        print('\nTeste ALUGAR bicicleta com valor negativo')
        self.assertEqual(self.bicicleta.alugar(-1), (0))
    
    def testeAlugarBicicletaComValorMaiorQueEstoque(self):
        print('\nTeste ALUGAR bicicleta com quantidade maior do que quantidade em estoque.')
        self.assertEqual(self.bicicleta.alugar(101), (0))
    
    def testeAlugarBicicletaComQtdLetra(self):
        print('\nTeste ALUGAR bicicleta com quantidade recebendo uma letra.') 
        self.assertEqual(self.bicicleta.alugar('a'), (0))
    
    def testesCalcularValorAluguelHora(self):
        print('\nTeste para CALCULAR o valor do aluguel por hora.')
        self.assertEqual(self.bicicleta.calcularValorAluguel(), (100))

    def testesCalcularValorAluguelDia(self):
        horaInicio = datetime(2021, 8, 22, 10, 00, 00)
        self.bicicleta = Bicicleta(100, 2, horaInicio , 'dia')
        self.cliente = Cliente('Rodolfo', 31483684873,self.bicicleta.estoqueBicicleta, self.bicicleta.quantidade, self.bicicleta.horaInicio, self.bicicleta.tipoAluguel)
        print('\nTeste para CALCULAR o valor do aluguel por DIA.')
        self.assertEqual(self.bicicleta.calcularValorAluguel(), (200))

    def testesCalcularValorAluguelSemana(self):
        horaInicio = datetime(2021, 8, 10, 10, 00, 00)
        self.bicicleta = Bicicleta(100, 2, horaInicio , 'semana')
        self.cliente = Cliente('Rodolfo', 31483684873,self.bicicleta.estoqueBicicleta, self.bicicleta.quantidade, self.bicicleta.horaInicio, self.bicicleta.tipoAluguel)
        print('\nTeste para CALCULAR o valor do aluguel por SEMANA.')
        self.assertEqual(self.bicicleta.calcularValorAluguel(), (600))

    def testesCalcularValorAluguelTipoDeAluguelInvalido(self):
        horaInicio = datetime(2021, 8, 10, 10, 00, 00)
        self.bicicleta = Bicicleta(100, 2, horaInicio , 'mes')
        self.cliente = Cliente('Rodolfo', 31483684873, self.bicicleta.estoqueBicicleta, self.bicicleta.quantidade, self.bicicleta.horaInicio, self.bicicleta.tipoAluguel)
        print('\nTeste para CALCULAR o valor do aluguel com o parâmetro tipo de aluguel inválido.')
        self.assertEqual(self.bicicleta.calcularValorAluguel(), (0))

    def testeCalcularValorAluguelDesconto(self):
        horaInicio = datetime(2021, 8, 25, 10, 00, 00)
        self.bicicleta = Bicicleta(100, 5, horaInicio , 'hora')
        print('\nTeste para CALCULAR o valor do aluguel com desconto de 30%.')
        self.assertEqual(self.bicicleta.calcularValorAluguel(), (175))

    def testeSalvarDados(self):
        print('\nTeste para SALVAR os dados do cliente no banco de dados')
        self.assertEqual(self.cliente.salvarDados(), ('Rodolfo 31483684873 2 2021-08-25 10:00:00 hora '))

# Teste do método - fecharConta (Class - Loja)
# Quantidade de bicicletas alugadas 2.
# Período total do aluguel 10 horas.
# Cálculo do aluguel por HORA
class TestesFecharContaHora(unittest.TestCase):
    def setUp(self):
        horaInicio = datetime(2021, 8, 25, 10, 00, 00)
        self.bicicleta = Bicicleta(100, 2, horaInicio , 'hora')
        self.cliente = Cliente('Rodolfo', 31483684873, self.bicicleta.estoqueBicicleta, self.bicicleta.quantidade, self.bicicleta.horaInicio, self.bicicleta.tipoAluguel)

    def testeFecharContaPorHora(self):
        print('\nTeste para FECHAR a conta, cálculo por hora.') 
        self.assertEqual(self.bicicleta.fecharConta(100, self.bicicleta.calcularValorAluguel()), (0))
    
    def testeFecharContaComValorPagoMenorQueConta(self):
        print('\nTeste para FECHAR a conta com valor pago menor que valor conta.')
        self.assertEqual(self.bicicleta.fecharConta(10, self.bicicleta.calcularValorAluguel()),(90))

    def testeFecharContaComValorNegativo(self):
        print('\nTeste para FECHAR a conta com valor negativo.')
        self.assertEqual(self.bicicleta.fecharConta(-1, self.bicicleta.calcularValorAluguel()) ,(100))

    def testeFecharContaComValorInvalido(self):
        print('\nTeste para FECHAR a conta com valor pago recebendo uma letra.')
        self.assertEqual(self.bicicleta.fecharConta('a', self.bicicleta.calcularValorAluguel()),(100))

    def testeFecharContaPorHoraTempoAluguelMaisDeUmDia(self): # 2 dias e 10 horas = 58 horas
        horaInicio = datetime(2021, 8, 23, 10, 00, 00)
        self.bicicleta = Bicicleta(100, 2, horaInicio , 'hora')
        print('\nTeste para FECHAR a conta com quantidade de horas mais que um dia.')
        self.assertEqual(self.bicicleta.fecharConta(580, self.bicicleta.calcularValorAluguel()) ,(0))
   

# Teste do método - fecharConta (Class - Loja)
# Quantidade de bicicletas alugadas 2.
# Período total do aluguel 3 DIAS.
# Cálculo do aluguel por DIA.
class TestesFecharContaDia(unittest.TestCase):
    def setUp(self):
        horaInicio = datetime(2021, 8, 23, 10, 00, 00)
        self.bicicleta = Bicicleta(100, 2, horaInicio , 'dia')
        self.cliente = Cliente('Rodolfo', 31483684873, self.bicicleta.estoqueBicicleta, self.bicicleta.quantidade, self.bicicleta.horaInicio, self.bicicleta.tipoAluguel)

    def testandoFecharContaPorDia(self):
        print('\nTeste para FECHAR a conta, cálculo por DIA.') 
        self.assertEqual(self.bicicleta.fecharConta(150, self.bicicleta.calcularValorAluguel()) ,(0))

    def testeFecharContaComValorPagoMenorQueContaPorDia(self):
        print('\nTeste para FECHAR a conta com valor pago menor que valor conta.(POR DIA)')
        self.assertEqual(self.bicicleta.fecharConta(10, self.bicicleta.calcularValorAluguel()),(140))


# Teste do método - fecharConta (Class - Loja)
# Quantidade de bicicletas alugadas 2.
# Período total do aluguel 2 semas.
# Cálculo do aluguel por semana.
class TestesFecharContaSemana(unittest.TestCase):
    def setUp(self):
        horaInicio = datetime(2021, 8, 15, 10, 00, 00)
        self.bicicleta = Bicicleta(100, 2, horaInicio , 'semana')
        self.cliente = Cliente('Rodolfo', 31483684873, self.bicicleta.estoqueBicicleta, self.bicicleta.quantidade, self.bicicleta.horaInicio, self.bicicleta.tipoAluguel)

    def testandoFecharContaPorSemana(self):
        print('\nTeste para FECHAR a conta, cálculo por semana.') 
        self.assertEqual(self.bicicleta.fecharConta(400, self.bicicleta.calcularValorAluguel()) ,(0))

    def testeFecharContaComValorPagoMenorQueContaPorSemana(self):
        print('\nTeste para FECHAR a conta com valor pago menor que valor conta.(POR SEMANA)')
        self.assertEqual(self.bicicleta.fecharConta(100, self.bicicleta.calcularValorAluguel()),(300))

if __name__ == '__main__':
    unittest.main() 