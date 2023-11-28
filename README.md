# Em andamento...

## Diagrama de Classes

```mermaid
classDiagram
    class Cliente {
        - endereco: String
        - contas: List<Conta>
        + realizarTransacao(conta: Conta, transacao: Transacao): void
        + adicionarConta(conta: Conta): void
    }

    class PessoaFisica {
        - nome: String
        - dataNascimento: String
        - cpf: String
    }

    class PessoaJuridica {
        - razaoSocial: String
        - cnpj: String
    }

    class Conta {
        - saldo: Float
        - numero: String
        - agencia: String
        - cliente: Cliente
        - historico: Historico
        + sacar(valor: Float): void
        + depositar(valor: Float): void
    }

    class ContaCorrente {
        - limite: Float
        - limiteSaques: Int
    }

    class ContaPoupanca {
        - juros: Float
    }

    class Historico {
        - transacoes: List<Transacao>
        + adicionarTransacao(transacao: Transacao): void
    }

    class Transacao {
        + valor: Float
        + registrar(conta: Conta): void
    }

    class Saque {
    }

    class Deposito {
    }

    Cliente --|> PessoaFisica
    Cliente --|> PessoaJuridica
    Conta *--|> ContaCorrente
    Conta *--|> ContaPoupanca
    Conta *--|> Historico
    Transacao <|-- Saque
    Transacao <|-- Deposito
```