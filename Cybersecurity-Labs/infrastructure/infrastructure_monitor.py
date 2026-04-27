class Sensor:
    def __init__(self, localizacao, leitura_atual):
        self.localizacao = localizacao
        self.leitura_atual = leitura_atual

class SensorTemperatura(Sensor):
    def checar(self):
        if self.leitura_atual > 28:
            print(f'[PERIGO]: Superaquecimento no {self.localizacao}: {self.leitura_atual} ºC')
        else:
            print(f'[OK]: Temperatura estável no {self.localizacao}')

class SensorUmidade(Sensor):
    def checar(self):
        if self.leitura_atual > 60:
            print(f'[ALERTA]: Umidada alta no {self.localizacao}: {self.leitura_atual} %!')

        else:
            print(f'[OK] Umidade controlada no {self.localizacao}')


central_monitoramento1 = SensorTemperatura('RACK A1', 25)
central_monitoramento2 = SensorTemperatura('RACK B1', 31)
central_monitoramento3 = SensorUmidade('Sala de No-Breaks', 45)
central_monitoramento4 = SensorUmidade('Entrada de Ar', 75)

monitoramento = [central_monitoramento1, central_monitoramento2, central_monitoramento3,central_monitoramento4]
for Sensor in monitoramento:
    Sensor.checar()