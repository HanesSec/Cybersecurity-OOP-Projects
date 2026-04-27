class DispositivoSeguranca:
    def __init__(self, id_equipamentos, nivel_bateria):
        self.id_equipamentos = id_equipamentos
        self.nivel_bateria = nivel_bateria

        print(f'Dispositivos {self.id_equipamentos} com {self.nivel_bateria} % de carga')

class CofreDigital(DispositivoSeguranca):
    def __init__(self, id_equipamentos, nivel_bateria):
        super().__init__(id_equipamentos, nivel_bateria)
        self.senha_mestra = '1234'
        self.historico_tentativas = []

    def tentar_abrir(self, senha_digitada):
        erros = self.historico_tentativas.count('Falha')

        if erros >= 3:
            print('SISTEMA BLOQUEADO! Procure o administrador')
            return

        if senha_digitada == self.senha_mestra:
            self.historico_tentativas.append('sucesso')
            print('ACESSO LIBERADO! Cofre Aberto')

        else:
            self.historico_tentativas.append('Falha')
            print(f'ERRO! Senha incorreta. Alarme disparado!')

meu_cofre = CofreDigital('id=152633', '35')
meu_cofre.tentar_abrir('1235')
meu_cofre.tentar_abrir('1896')
meu_cofre.tentar_abrir('1893')
meu_cofre.tentar_abrir('1234')

print(meu_cofre.historico_tentativas)