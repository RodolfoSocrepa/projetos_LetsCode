from abc import ABC, abstractclassmethod
from datetime import datetime
import math

class Loja(ABC):
    def __init__(self, estoqueBicicleta, quantidade, horaInicio, tipoAluguel):
        self.estoqueBicicleta = estoqueBicicleta
        self.quantidade = quantidade
        self.horaInicio = horaInicio
        self.tipoAluguel = tipoAluguel
        self.caixa = 1000
        
    def mostraQtdEstoque(self):
        
        try:
            if type(self.estoqueBicicleta) != int or self.estoqueBicicleta <= 0:
                raise SystemError
            
            if self.estoqueBicicleta <= 0:
                raise ValueError

            self.estoqueBicicleta = self.estoqueBicicleta - self.quantidade
            print(f'Loja - Quantidade disponível em estoque = {self.estoqueBicicleta}')
            return self.estoqueBicicleta
        
        except SystemError:
            print(f'Loja - ERROR! Valor da quantidade em estoque inválido. Valor informado ({self.estoqueBicicleta}).')
            return 0

    def alugar(self, quantidade):

        try:
            
            if quantidade <= 0:
                raise ValueError ('Quantidade inválida!')

            if self.estoqueBicicleta < quantidade:
                raise SystemError ('Quantidade de bicicletas em estoque inferior a quantidade solicitada!')
                
            self.estoqueBicicleta -= quantidade
            print(f'Loja - Aluguel de {quantidade} bicicletas efetuado com sucesso. Hora de início {self.horaInicio.strftime("%d/%m/%Y %H:%M")}. Quantidade em estoque {self.estoqueBicicleta}.')
            return self.estoqueBicicleta

        except ValueError:
            print(f'Loja -ERROR! Aluguel de {quantidade} bicicletas não foi efetuado, quantidade inválida. Estoque {self.estoqueBicicleta}')
            return 0

        except SystemError:
            print(f'Loja -Aluguel de {quantidade} bicicletas não foi efetuado, quantidade solicitada maior do que o estoque. Estoque {self.estoqueBicicleta}')
            return 0

        except:
            print(f'Loja -ERROR! Aluguel de {quantidade} bicicletas não efetuado. Estoque {self.estoqueBicicleta}')
            return 0

    def fecharConta(self, valorPago, conta):

        try:
            if valorPago < conta and valorPago > 0:
                raise ValueError

            if valorPago < 0:
                raise SystemError 
             

            valorPago >= conta
            self.caixa += valorPago
            print(f'Loja - Valor do aluguel pago com sucesso. Toltal da conta R$ {conta}, valor do pagamento R$ {valorPago}. Caixa = R$ {self.caixa}')
            return 0

        except ValueError:
            print(f'Loja - A conta NÃO foi paga! Valor do pagamento R$ {valorPago} menor do que a conta R$ {conta}.')
            return conta - valorPago

        except SystemError:
            print(f'Loja - Valor inválido! A conta NÃO foi paga! Valor do pagamento ({valorPago}) menor do que a conta R$ {conta}.')
            return conta

        except:
            print(f'Loja - Valor inválido! A conta NÃO foi paga! Toltal da conta R$ {conta}. ')
            return conta

class Bicicleta(Loja):
    def __init__(self, estoqueBicicleta, quantidade, horaInicio, tipoAluguel):
        super().__init__(estoqueBicicleta, quantidade, horaInicio, tipoAluguel)
        self.totalTempo = 0
        self.conta = 0

    def calcularValorAluguel(self):
        
        self.horaFim = datetime(2021, 8, 25, 20, 00, 00) # Substituir pela hora atual.
        self.diferencaTempo = self.horaFim - self.horaInicio
        try:

            if self.tipoAluguel != 'hora' and  self.tipoAluguel != 'dia' and self.tipoAluguel != 'semana':
                raise SystemError

            if self.tipoAluguel == 'hora':
                self.totalTempo = math.ceil(self.diferencaTempo.seconds / 3600 ) + self.diferencaTempo.days * 24
                self.conta = (self.totalTempo * 5) * self.quantidade 

            if self.tipoAluguel == 'dia': 
                self.totalTempo = self.diferencaTempo.days + math.ceil(self.diferencaTempo.seconds / 3600 / 24)
                self.conta = (self.totalTempo * 25) * self.quantidade

            if self.tipoAluguel == 'semana':
                self.totalTempo = math.ceil(self.diferencaTempo.days / 7 + self.diferencaTempo.seconds / 3600 / 24 / 7)       
                self.conta = (self.totalTempo * 100) * self.quantidade

            if self.quantidade >= 3 <= 5:
                    self.conta = self.conta - self.conta * 0.3
                    print(f'Bicicleta - DESCONTO DE 30% - Tipo de aluguel por ({self.tipoAluguel}). Quantidade {self.quantidade}.Horário da retirada {self.horaInicio}. Devolução {self.horaFim}. Tempo total do aluguel {self.totalTempo} {self.tipoAluguel} (s) ')
                    return self.conta
            else:
                print(f'Bicicleta - Tipo de aluguel por ({self.tipoAluguel}). Quantidade {self.quantidade}.Horário da retirada {self.horaInicio}. Devolução {self.horaFim}. Tempo total do aluguel {self.totalTempo} {self.tipoAluguel} (s) ')
                return self.conta

        except SystemError:
            print(f'Bicicleta -ERROR! Tipo de aluguel inválido ({self.tipoAluguel}). ')
            return 0

class Cliente(Loja):
    def __init__(self, nome, cpf, estoqueBicicleta, quantidade, horaInicio, tipoAluguel):
        super().__init__(estoqueBicicleta, quantidade, horaInicio, tipoAluguel)
        self.nome = nome
        self.cpf = cpf
    
    def salvarDados(self):
        dados = []
        self.bancoDeDados = open("bancoDeDados.txt", 'a', encoding='utf-8')
        dados = self.nome, self.cpf, self.quantidade, self.horaInicio, self.tipoAluguel
        for atributo in dados: 
            self.bancoDeDados.write(str(atributo) + ' ')
        print(f'Cliente -Salvando os dados do cliente no banco de dados...{dados}')
        self.bancoDeDados.close()
        self.bancoDeDados = open("bancoDeDados.txt", 'r', encoding='utf-8')
        conteudo = self.bancoDeDados.read()
        print(f'Cliente - Dados salvos {conteudo}')
        self.bancoDeDados.close()
        return conteudo


    



