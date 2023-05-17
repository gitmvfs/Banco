import sqlite3

#Variavel que cria o banco de dados
bancoDados = sqlite3.connect('ianes.db')

#Variavel que faz as ações entre o banco de dados
cursor = bancoDados.cursor()


##Teste de dados

dadosTabela = [('Marcos','123',100),
               ('Atila','321',150),
               ('Julia','1234',200)]


cursor.execute('''
        create table cliente (
            nome text,
            senha text,
            saldo real
        )
''')

cursor.executemany('''
        insert into cliente(nome, senha, saldo)
        values(? , ? , ?)
''',(dadosTabela))

bancoDados.commit()

cursor.execute("select * from cliente")

for i in range(3):

    resultado = cursor.fetchone()
    print(resultado)
    print(resultado[0], resultado[1],resultado[2])

    if 'Atila' in resultado:
        break

cursor.close()
bancoDados.close()