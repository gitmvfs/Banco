from db_INAES import *

class main():

    def __init__(self) -> None:
        self.bancoDeDados = bancoDeDados()
        self.bancoDeDados.retornarBanco()

        self.logado = False
        self.contaLogada_nome:str
        self.contaLogada_saldo:float

        self.menuInicial()

    def menuInicial(self):
        print('1 - Logar')
        print('2 - Criar Conta')
        print('3 - Sair')
      
        opcao = float(input('Digite uma opção: '))
            
        if opcao == 1:
            self.logar()
        elif opcao == 2:
            self.cadastrar()
        elif opcao == 3:
            print('Obrigado por utilizar!!!')
        else:
            print('Opção inválida')
            self.menuInicial()
        
    def logar(self,nome:str = ''):
            
            if nome == '': # Compara se ela foi chamada vazia, no caso pelo menu. Se foi pelo cadastrar ele já vai logar com os dados que o usuário acabou de cadastrar
            
                nome = input('Digite seu usuário: ')
                senha = input('Digite sua senha: ')
                
                if nome == self.bancoDeDados.retornarCadastro(nome)[0] and senha == self.bancoDeDados.retornarCadastro(nome)[1]: #Compara se o usuário e senha estão certos
                    
                    self.logado = True
                    self.contaLogada_nome = nome
                    self.contaLogada_saldo = self.bancoDeDados.retornarCadastro(nome)[2]
                    print(f'Bem vindo, senhor(a) {nome}')

                else:
                    print('Usuário ou senha inválidos.')

            else: #Caso tenha sido chamado pelo cadastro, o usuário vai logar direto, já que acabou de cadastrar

                self.logado = True
                self.contaLogada_nome = nome
                self.contaLogada_saldo = self.bancoDeDados.retornarCadastro(nome)[2]
                print(f'Bem vindo(a), senhor(a) {nome}')
            
            if self.logado == True:
                self.menuPrincipal()
            
    def cadastrar(self):
        
        nome = input('Digite seu usuário: ')
        senha = input('Digite sua senha: ')
        saldo = float(input('Digite seu saldo: '))
      

        if self.bancoDeDados.cadastro(nome,senha,saldo) == True:
            self.logar(nome)
        else:
            self.cadastrar()

    def menuPrincipal(self):
        print('1 - Transferir')
        print('2 - Depositar')
        print('3 - Sacar')
        print('4 - Consultar Dados')
        print('5 - Deslogar')
        print('6 - Sair')

        opcao = float(input('Digite uma opção: '))

        if opcao ==1:
            self.transferir()
        elif opcao == 2:
            self.depositar()
        elif opcao ==3:
            self.sacar()
        elif opcao ==4:
           dados = self.bancoDeDados.retornarCadastro(self.contaLogada_nome)
           print(f'Display: Usuario:{self.contaLogada_nome} Senha:???*sem acesso saldo:{self.contaLogada_saldo}  ')
           print(f'BD: Usuario:{dados[0]} Senha: {dados[1]} Saldo: {dados[2]} ')
           self.menuPrincipal()
        elif opcao == 5:
            self.deslogar()
        elif opcao == 6:
            print('Obrigado por utilizar!!')


    def transferir(self):
        contaTranferencia = input('Digite o nome da conta para transferência: ')
        valorTransferencia = float(input('Digite o valor para transferencia: '))

        if valorTransferencia > self.contaLogada_saldo:
            print('Valor inválido, consultar saldo disponivel.')
            self.menuPrincipal()
        else:
           
            varSaldoBD =  self.contaLogada_saldo - valorTransferencia # Essa variavel é a que vai mandar o saldo para o Banco de Dados
            self.contaLogada_saldo -= valorTransferencia #Atualiza o display
            self.bancoDeDados.atualizarSaldo(varSaldoBD,self.contaLogada_nome) # Atualiza o valor da conta logada no banco de dados
            

            saldoContaTransferencia = self.bancoDeDados.retornarCadastro(contaTranferencia)[2]    #Consulta no banco de dados qual o saldo da conta que irá receber a transferencia
            valorTransferencia += saldoContaTransferencia #Soma o valor da transferencia com o saldo da conta 
            self.bancoDeDados.atualizarSaldo(valorTransferencia,contaTranferencia) #Atualiza o banco de dados com o novo valor recebido

            self.menuPrincipal()

    def depositar(self):
        while True:

            saldoDepositado = float(input('Digite um valor para depósito: '))
            varSaldoBD = saldoDepositado + self.contaLogada_saldo # Essa variavel é a que vai mandar o saldo para o Banco de Dados


            #Atualiza o saldo do 'display'
            self.contaLogada_saldo += saldoDepositado
            try:
                self.bancoDeDados.atualizarSaldo(varSaldoBD,self.contaLogada_nome)
                break
            except:
                print('Algo deu errado, tente novamente. ')

        self.menuPrincipal()

    def sacar(self):
        while True:

            saldoSacado = float(input('Digite um valor para depósito: '))

            if saldoSacado > self.contaLogada_saldo:
                print('Valor inválido, consultar saldo disponivel.')
            else:
                varSaldoBD = self.contaLogada_saldo - saldoSacado # Essa variavel é a que vai mandar o saldo para o Banco de Dados

                #Atualiza o saldo do 'display'
                self.contaLogada_saldo -= saldoSacado
                try:
                    self.bancoDeDados.atualizarSaldo(varSaldoBD,self.contaLogada_nome)
                    break
                except:
                    print('Algo deu errado, tente novamente. ')

        self.menuPrincipal()
    
    def deslogar(self):
        self.logado = False
        self.contaLogada_nome = str
        self.contaLogada_saldo = float
        print('Obrigado por utilizar!!!')
        self.menuInicial()


main()