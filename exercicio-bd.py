import sqlite3

conexao = sqlite3.connect('exercicio')
cursor = conexao.cursor()


##1.Crie uma tabela chamada "alunos" com os seguintes campos: id(inteiro), nome (texto), idade (inteiro) e curso (texto).
#cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR (30))')

##2. Insira pelo menos 5 registros de alunos na tabela que você criou noexercício anterior.
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) \
               VALUES (1, "Izabella", 29, "Farmácia"), \
                      (2, "Gabriel", 25, "Ciência da Computação"), \
                      (3, "Patricia", 18, "Engenharia"), \
                      (4, "Fernanda", 30, "Administração"), \
                      (5, "Pedro", 21, "Engenharia")')



#3a) Selecionar todos os registros da tabela "alunos".
cursor.execute('SELECT * from alunos')

##3b) Selecionar o nome e a idade dos alunos com mais de 20 anos.
cursor.execute('SELECT nome, idade FROM alunos WHERE idade > 20')

##3c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética.
cursor.execute("SELECT * FROM alunos WHERE curso = 'Engenharia' ORDER BY nome")

##3d) Contar o número total de alunos na tabela
cursor.execute('SELECT COUNT(*) AS total_alunos FROM alunos')

##4a) Atualize a idade de um aluno específico na tabela.
cursor.execute('UPDATE alunos SET idade = 30 WHERE id = 2');

##4b) Remova um aluno pelo seu ID.
cursor.execute('DELETE FROM alunos WHERE id = 4');

##5. Criar uma Tabela e Inserir Dados
cursor.execute('CREATE TABLE clientes (id INT, nome VARCHAR(100), idade INT, saldo FLOAT)')
cursor.execute("INSERT INTO clientes(id, nome, idade, saldo) VALUES (1, 'Maria', 35, 1500.50)"),
cursor.execute("INSERT INTO clientes(id, nome, idade, saldo) VALUES (2, 'Leonardo', 30, 2500.25)"),
cursor.execute("INSERT INTO clientes(id, nome, idade, saldo) VALUES (3, 'Natalia', 28, 1000.12)"),
cursor.execute("INSERT INTO clientes(id, nome, idade, saldo) VALUES (4, 'Leticia', 33, 800.60)");

##6a) Selecione o nome e a idade dos clientes com idade superior a30 anos.
cursor.execute('SELECT nome, idade FROM clientes WHERE idade > 30');

##6b) Calcule o saldo médio dos clientes.
cursor.execute('SELECT AVG(saldo) AS saldo_medio FROM clientes');

##6c) Encontre o cliente com o saldo máximo.
cursor.execute('SELECT * FROM clientes ORDER BY saldo DESC LIMIT 1');

##6d) Conte quantos clientes têm saldo acima de 1000.
cursor.execute('SELECT COUNT(*) AS clientes_acima_de_1000 FROM clientes WHERE saldo > 1000');

##7a) Atualize o saldo de um cliente específico.
cursor.execute('UPDATE clientes SET saldo = 1500 WHERE id = 3');

##7b)Remova um cliente pelo seu ID.
cursor.execute('DELETE FROM clientes WHERE id = 4');

##8.Junção de Tabelas
cursor.execute('CREATE TABLE compras (id INT PRIMARY KEY, cliente_id INT, produto VARCHAR(50), valor FLOAT, FOREIGN KEY (cliente_id) REFERENCES clientes(id))')
cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) \
               VALUES (1, 1, "Livro", 50.75), \
                      (2, 2, "Eletrônicos", 1200.00), \
                      (3, 3, "Roupas", 300.50), \
                      (4, 1, "Comida", 80.25)')

cursor.execute('SELECT c.id, cl.nome AS cliente_nome, c.produto, c.valor FROM compras c JOIN clientes cl ON c.cliente_id = cl.id');






conexao.commit()
conexao.close