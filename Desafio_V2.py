from datetime import datetime
from colorama import init, Fore, Style, Back
import time

# Inicializa o colorama
init(autoreset=True)

class ContaBancaria:
    def __init__(self):
        self.numero_conta = None
        self.saldo = 0
        self.historico = []
        self.saques_diarios = 0
        self.ultima_data_saque = None

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.registrar_transacao("Depósito", valor)
            print(f"\n{Fore.GREEN}Depósito de R$ {valor:.2f} realizado com sucesso.{Style.RESET_ALL}")
        else:
            print(f"\n{Fore.RED}Valor inválido para depósito.{Style.RESET_ALL}")

    def sacar(self, valor):
        if self.pode_realizar_saque():
            if 0 < valor <= self.saldo:
                self.saldo -= valor
                self.registrar_transacao("Saque", valor)
                self.saques_diarios += 1
                self.ultima_data_saque = datetime.now().strftime("%d-%m-%Y")
                print(f"\n{Fore.GREEN}Saque de R$ {valor:.2f} realizado com sucesso.{Style.RESET_ALL}")
            else:
                print(f"\n{Fore.RED}Valor inválido para saque ou saldo insuficiente.{Style.RESET_ALL}")
        else:
            print(f"\n{Fore.YELLOW}Limite diário de saques atingido. Tente novamente amanhã.{Style.RESET_ALL}")

    def pode_realizar_saque(self):
        hoje = datetime.now().strftime("%d-%m-%Y")
        return self.ultima_data_saque != hoje or self.saques_diarios < 3

    def registrar_transacao(self, tipo, valor):
        data_transacao = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        self.historico.append({"tipo": tipo, "valor": valor, "data": data_transacao})

    def exibir_extrato(self):
        print("\nExtrato Bancário:")
        for transacao in self.historico:
            tipo = transacao['tipo']
            valor = transacao['valor']
            data = transacao['data']
            
            if tipo == 'Depósito':
                print(f"{data} - {Fore.BLUE}{tipo}{Style.RESET_ALL}: R$ {valor:.2f}")
            elif tipo == 'Saque':
                print(f"{data} - {Fore.YELLOW}{tipo}{Style.RESET_ALL}: R$ {valor:.2f}")
            else:
                print(f"{data} - {tipo}: R$ {valor:.2f}")

        saldo_formatado = f"Saldo Atual: R$ {self.saldo:.2f}"

        if self.saldo == 0:
            print(f"{Fore.RED}{Back.BLACK}{Style.BRIGHT}{saldo_formatado}{Style.RESET_ALL}", end="\r", flush=True)
            time.sleep(0.5)
        elif self.saldo < 10:
            print(f"{Fore.RED}{saldo_formatado}{Style.RESET_ALL}", end="\r", flush=True)
        elif 10 <= self.saldo <= 500:
            print(f"{Fore.YELLOW}{saldo_formatado}{Style.RESET_ALL}", end="\r", flush=True)
        else:
            print(f"{Fore.GREEN}{saldo_formatado}{Style.RESET_ALL}", end="\r", flush=True)


def menu():
    print("\n=============== MENU ===============")
    print(f"  [{Fore.CYAN}D{Style.RESET_ALL}] {Fore.CYAN}Depositar{Style.RESET_ALL}")
    print(f"  [{Fore.CYAN}S{Style.RESET_ALL}] {Fore.CYAN}Sacar{Style.RESET_ALL}")
    print(f"  [{Fore.CYAN}E{Style.RESET_ALL}] {Fore.CYAN}Extrato{Style.RESET_ALL}")
    print(f"  [{Fore.CYAN}Q{Style.RESET_ALL}] {Fore.CYAN}Sair{Style.RESET_ALL}")
    return input(f"{Fore.YELLOW}Escolha uma opção (D/S/E/Q): {Style.RESET_ALL}").upper()


def main():
    conta = ContaBancaria()

    while True:
        escolha = menu()

        if escolha == "D":
            valor_deposito = float(input("\nDigite o valor a ser depositado: "))
            conta.depositar(valor_deposito)

        elif escolha == "S":
            valor_saque = float(input("\nDigite o valor a ser sacado: "))
            conta.sacar(valor_saque)

        elif escolha == "E":
            conta.exibir_extrato()

        elif escolha == "Q":
            print(f"\n{Fore.YELLOW}Sessão encerrada. Obrigado!{Style.RESET_ALL}")
            break

        else:
            print(f"\n{Fore.RED}Opção inválida. Tente novamente.{Style.RESET_ALL}")


if __name__ == "__main__":
    main()
