class Periferico:
    def __init__(self, marca, modelo, tipo_conexao):
        self.marca = marca
        self.modelo = modelo
        self.tipo_conexao = tipo_conexao

    def exibir_detalhes(self):
        print(f'[DISPOSITIVO]: {self.marca} {self.modelo} via {self.tipo_conexao}')


class TecladoMecanico(Periferico):
    def __init__(self, marca, modelo, tipo_conexao, tipo_switch):
        super().__init__(marca, modelo, tipo_conexao)
        self.tipo_switch = tipo_switch

    def exibir_detalhes(self):
        super().exibir_detalhes()
        print(f'Switch {self.tipo_switch} detectado. Ideal para codificação rápida')

class MouseGamer(Periferico):
    def __init__(self, marca, modelo, tipo_conexao, dpi_maximo):
        super().__init__(marca, modelo, tipo_conexao)
        self.dpi_maximo = dpi_maximo

    def exibir_detalhes(self):
        super().exibir_detalhes()
        print(f'[PRECISÃO] Sensor de {self.dpi_maximo} DPI ativo para análise forense')

teclado1 = TecladoMecanico('REDDRAGON', 'RED895', 'Tipo C', 'Vermelho')
mouse1 = MouseGamer('REDDD','Blue892', 'Bluetooth','100')
periferico1 = Periferico('TCN', 'Basico', 'usb')

inventario_ti = [teclado1, mouse1, periferico1]
for inventario in inventario_ti:
    inventario.exibir_detalhes()