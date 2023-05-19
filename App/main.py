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
                    self.contaLogada_nome = {nome}
                    self.contaLogada_saldo = self.bancoDeDados.retornarCadastro(nome)[2]
                    print(f'Bem vindo, senhor(a) {nome}')

                else:
                    print('Usuário ou senha inválidos.')

            else: #Caso tenha sido chamado pelo cadastro, o usuário vai logar direto, já que acabou de cadastrar

                self.logado = True
                self.contaLogada_nome = {nome}
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



main()