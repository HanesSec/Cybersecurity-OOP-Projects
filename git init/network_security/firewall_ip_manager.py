class Dispositivos:
    def __init__(self, ip, nome_dispositivo):
        self.ip = ip
        self.nome_dispositivo = nome_dispositivo

        print(f'{self.nome_dispositivo} com IP {self.ip} está ONLINE')


class Firewall(Dispositivos):
    def __init__(self,ip, nome_dispositivo):
        super().__init__(ip, nome_dispositivo)
        self.lista_bloqueados = ['192.168.1.0', '10.0.0.5', '172.16.0.100']

    def verificar_acesso(self, ip_externo):
        if ip_externo in self.lista_bloqueados:
            print(f'ACESSO BLOQUEADO para o ip {ip_externo}')
        else:
            print('ACESSO PERMITIDO')

# --TESTANDO--
D1 = Firewall('192.168.1.50', 'Dispositivo_Alpha')

D1.verificar_acesso('192.168.1.50')
D1.verificar_acesso('192.168.1.0')

