# Em andamento...

## Diagrama de Classes

```mermaid
classDiagram

  class Cliente <<abstract>> {
    +endereco: string
    +contas: Conta[]
    {abstract} +realizarTransacao(conta: Conta, transacao: Transacao): void
    {abstract} +adicionarConta(conta: Conta): void
  }

  class PessoaFisica {
    +nome: string
    +dataNascimento: string
    +cpf: string
  }

  class PessoaJuridica {
    +razaoSocial: string
    +cnpj: string
  }

  class Conta <<abstract>> {
    +saldo: float
    +numero: string
    +agencia: string
    +cliente: Cliente
    +historico: Historico
    {abstract} +sacar(valor: float): bool
    {abstract} +depositar(valor: float): bool
  }

  class ContaCorrente {
    +limite: float
    +limiteSaques: int
  }

  class ContaPoupanca {
    +juros: float
  }

  class Historico {
    +transacoes: Transacao[]
    +adicionarTransacao(transacao: Transacao): void
  }

  class Transacao <<abstract>> {
    {abstract} +valor: float
    {abstract} registrar(conta: Conta): void
  }

  class Saque {
  }

  class Deposito {
  }

  Cliente <|-- PessoaFisica
  Cliente <|-- PessoaJuridica
  Conta *--|> ContaCorrente
  Conta *--|> ContaPoupanca
  Conta *--|> Historico
  Transacao <|-- Saque
  Transacao <|-- Deposito
```