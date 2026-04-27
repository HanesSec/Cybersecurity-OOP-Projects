#classe Avô
class Equipamentos:
    def __init__(self, ip, fabricante):
        self.ip = ip
        self.fabricante = fabricante

        print(f'equipamentos {self.ip} online.')

#classes Pai (As Especialidades)
class DetectorIntruso(Equipamentos):
    def alerta_ameaca(self):
        print(f'ALERTA: Atividade suspeita detectada no IP {self.ip}')

class FiltroPacotes(Equipamentos):
    def bloquear_ip(self, ip_alvo):
        print(f'BLOQUEANDO: O tráfego do IP {ip_alvo} foi cortado.')

class FirewallAvancado(DetectorIntruso, FiltroPacotes):
    def __init__(self, ip, fabricante):
        super().__init__(ip, fabricante)

    def proteger_rede(self, ip_suspeito):
        self.alerta_ameaca()
        self.bloquear_ip(ip_suspeito)


meu_firewall = FirewallAvancado('192.168.1.1', 'Cisco')
meu_firewall.proteger_rede('10.0.0.50')


