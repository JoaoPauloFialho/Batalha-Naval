import MySQLdb

class Dashboard:
    def __init__(self, nome, vitoria=False):
        self.nome = nome
        if vitoria:
            self.vitoria = 1
        else:
            self.vitoria = 0

    def __conectar(self):
        self.conn = MySQLdb.connect(
            db='db_batalha_naval',
            host='localhost',
            user='usuario',
            password='senha',
        )
        self.cursor = self.conn.cursor()

    def __desconectar(self):
        if self.conn:
            self.conn.close()

    def mostrar(self):
        self.__conectar()
        self.cursor.execute('SELECT * FROM dashboard')
        dados = self.cursor.fetchall()  # vai transformar os valores selecionados ali em uma lista

        if len(dados) > 0:
            print('-' * 10)
            for dado in dados:
                print(f'ID : {dado[0]}')
                print(f'Nome : {dado[1]}')
                print(f'Jogos : {dado[2]}')
                print(f'Vitorias : {dado[3]}')

        self.__desconectar()

    def adicionar(self, nome):
        self.__conectar()
        self.cursor.execute(f"INSERT INTO dashboard(nome, qnt_jogos, qnt_vitorias) "
                            f"VALUES ('{self.nome.capitalize()}', 0, {self.vitoria})")
        self.conn.commit()

        self.__desconectar()

    def atualizar(self):
        self.__conectar()
        if self.vitoria:
            self.cursor.execute(f"UPDATE dashboard SET qnt_vitorias+=1, qnt_jogos+= 1 "
                                f"WHERE nome=='{self.nome}'")

            self.cursor.execute(f"UPDATE dashboard SET qnt_jogos+= 1 "
                                f"WHERE nome=='{self.nome}'")

        else:
            self.cursor.execute(f"UPDATE dashboard SET qnt_jogos+= 1, "
                                f"WHERE nome='{self.nome}'")

        self.cursor.commit()
        self.__desconectar()


