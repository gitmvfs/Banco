import sqlite3

class bancoDeDados():
    
        def __init__(self):
                self.criarBd()
        
        
        def ligarBd(self):
                #Variavel que cria o banco de dados
                self.bancoDados = sqlite3.connect('ianes.db')

                #Variavel que faz as ações entre o banco de dados
                self.cursor = self.bancoDados.cursor()

        def atualizarBd(self):
                
                self.bancoDados.commit()
        
        def desligarBd(self):
               self.cursor.close()
               self.bancoDados.close()
               

        def criarBd(self):
                self.ligarBd()
        
                self.cursor.execute('''
                create table if not exists clientes (
                nome text PRIMARY KEY, 
                senha text,
                saldo real)''')
                self.desligarBd()
       

        def cadastro(self,nome:str,senha:str,saldo:float):
                self.ligarBd()
                
                try:
                        self.cursor.execute('''
                        insert into clientes(nome, senha, saldo)
                        values(? , ? , ?)
                        ''',(nome,senha,saldo))
                        self.atualizarBd()
                        self.desligarBd()
                        return True
                
                except sqlite3.IntegrityError :
                        print('O usuário ja está cadastrado, insira outro valor.')
                        self.desligarBd()
                        return False

                except TypeError as te:
                        print(te)

        def retornarBanco(self):
                self.ligarBd()
                for row in self.cursor.execute('SELECT * FROM clientes'):
                        print(row)
                self.desligarBd()
       
        def retornarCadastro(self,contaNome:str):
                """ Retorna uma tupla com os seguintes campos: Nome,Senha,Saldo [0] [1] [2] respectivamente"""
                
                self.ligarBd()

                for row in self.cursor.execute('SELECT * FROM clientes'): 
                        if contaNome in row:
                                return row
                        elif contaNome == None :
                                print('Conta não encontrada')
                        
                
                self.desligarBd()

        def atualizarSaldo(self,saldo:float,contaNome:str):

                self.ligarBd()
                
                self.cursor.execute(f'''UPDATE clientes SET saldo = {saldo} WHERE nome = '{contaNome}' ''')        
                self.atualizarBd()
                self.desligarBd()