class Funcionario:
    def __init__(self, nome, cargo):
        self.nome = nome
        self.cargo = cargo

    def bater_ponto(self):
        print(f'O funcionario {self.nome} registrou a entrada à 08:00')

class Seguranca(Funcionario):
    def __init__(self,nome, cargo, lista_ronda):
        super().__init__(nome, cargo)
        self.setores_permitidos = lista_ronda

    def checar_setor(self, setor_destino):
        if setor_destino in self.setores_permitidos:
            print(f'Acesso autorizado para o segurança {self.nome} a {setor_destino}')
        else:
            print(f'ACESSO NEGADO! O setor {setor_destino} não faz parte da sua ronda')

user_hanes = Seguranca('Hanes', 'Chefe de segurança', ['TI', 'Almoxerifado', 'cofre'])
user_andre = Seguranca('Andre', 'Vigia', ['Recepção', 'Portaria'])

user_hanes.checar_setor('Portaria')
user_andre.checar_setor('Recepção')