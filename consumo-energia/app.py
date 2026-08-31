# DONE: Pedir o nome do aparelho
# DONE: Pedir a potência do aparelho em watts (W) 
# DONE: Pedir o tempo médio de uso diário em horas
# DONE: Calcular o consumo mensal em kWh, usando a formula consumoMensal = (potencia * horasDia * 30) / 1000
# DONE: Mostrar na tela o resultado formatado

from rich import print

class ConsumoEnergia:
    """
    A classe permite calcular o consumo mensal estimado (em kWh) e o impacto financeiro aproximado gerado por qualquer aparelho eletrodoméstico ou equipamento eletrônico, a partir de dados básicos de entrada.
    """

    def __init__(self, aparelho=None, consumo_horas=None, potencia=None):
        self.aparelho = input("Digite o nome do aparelho: ")
        self.consumo_horas = float(input("Digite o tempo médio de uso diário em horas: "))
        self.potencia = float(input("Digite a potência do aparelho em watts (W): "))
        self.consumo_mensal = 0
        self.preco_kwh = 0.75

    def calcular_mensal(self):
        self.consumo_mensal = (self.potencia * self.consumo_horas * 30) / 1000
        self.preco_kwh *= self.consumo_mensal


    def mostrar_resultado(self):
        print(f"Aparelho: {self.aparelho}")
        print(f"Potência nominal: {self.potencia:.2f}W")
        print(f"Consumo mensal: [bold blue on white] {self.consumo_mensal:.2f} [/]KWh/mês")
        print(f"Custo estimado: [bold white on red] R${self.preco_kwh:.2f} [/] por mês")
        
eletro1 = ConsumoEnergia()
eletro1.calcular_mensal()
eletro1.mostrar_resultado()
print("---------------------------------------------------------------------------------")

while continuar := input("Deseja calcular o consumo de energia de outro aparelho? (s/n): ").lower() == 's':
    print("---------------------------------------------------------------------------------")
    eletro2 = ConsumoEnergia()
    eletro2.calcular_mensal()
    eletro2.mostrar_resultado()

if not continuar:
    print("---------------------------------------------------------------------------------")
    print("[bold blue on white]Obrigado! Lembre-se de economizar energia sempre![/]")