contasArray = [];
extratosArray = [];



class Contas:
    contador = 0
    saquesDiarios = 3;
    def __init__(self, nome, tipo, valor):
        self.nome = nome;
        self.tipo = tipo;
        self.valor = valor;
        Contas.contador +=1;

    def getNome(self):
        return self.nome;
    def getTipo(self):
        return self.tipo;
    def getValor(self):
        return self.valor;
    def setSacar(self, valor):
        self.valor -= valor
    def setDepositar(self, valor):
        self.valor += valor;

class extrato:
    def __init__(self, tipo, valor, conta):
        self.tipo = tipo;
        self.valor = valor;
        self.conta = conta;

    def getTipo(self):
        return self.tipo;
    def getValor(self):
        return self.valor;
    def getConta(self):
        return self.conta;

    def setTipo(self,tipo):
        self.tipo = tipo;
    def setValor(self,valor):
        self.valor = valor;
    def setConta(self,conta):
        self.conta = conta;

def register():
    nome = "";  
    tipo = "";
    valor = "";
    while not nome:
        print("Digite seu nome da sua conta");
        nome = input();
    while not tipo:
        print("Digite o tipo da sua conta: ");
        tipo = input();
    while not valor and not type(valor) == int:
        print("Digite seu valor inicial da conta");
        try:
            valor = int(input());
        except:
            print("Numero Apenas");
    
    currentConta = Contas(nome, tipo, valor)
    contasArray.append(currentConta)

    main();

def depositar(conta):
    qnt = "";
    while not qnt and not type(qnt) == int:
        print("Qual e o valor que deseja depositar? ")
        try:
            qnt = int(input());
        except:
            print("Numeros apenas");
    if qnt < 0:
        print("Nao pode depositar");
    else:
        conta.setDepositar(qnt);
        currentExtrato = extrato("Deposito", qnt, conta);
        extratosArray.append(currentExtrato);
        logged(conta.getNome());


def sacar(conta):
    qnt = "";
    while not qnt and not type(qnt) == int:
        print("Qual e o valor que deseja sacar? ");
        try:
            qnt = int(input());
        except:
            print("Numeros apenas");
    if qnt <= conta.getValor() and conta.saquesDiarios > 0 and qnt <= 500:
        conta.saquesDiarios-=1;
        conta.setSacar(qnt);
        currentExtrato = extrato("Sacar", qnt, conta);
        print(conta.saquesDiarios);
        extratosArray.append(currentExtrato);
        logged(conta.getNome());
    elif conta.saquesDiarios <= 0:
        print("Voce chegou no seu limite de saques - 3");
        input();
        logged(conta.getNome());
    elif qnt > conta.getValor():
        print("Voce esta sem dindin!");
        input();
        logged(conta.getNome())
    elif qnt > 500:
        print("Valor maximo ultrapassado - Limite = 500");
        input();
        logged(conta.getNome());


def transfer(conta):
    qnt = "";
    print("Nome da conta que deseja transferir");
    accountToTransfer = input();
    
    while not qnt and not type(qnt) == int:
        print("Quantidade para transferir: ");
        try:
            qnt = int(input());
        except:
            print("Numeros apenas");
    
    for x in contasArray:
        if x.getNome() == accountToTransfer:
            conta.setSacar(qnt);
            if qnt <= conta.getValor():
                conta.setSacar(qnt);
                x.setDepositar(qnt);
                logged(conta.getNome());
                currentExtrato = extrato("Transferir", qnt, conta);
                extratosArray.append(currentExtrato);
            else:
                print("Voce esta sem dindin");
                logged(conta.getNome());
    
    print("Conta não encontrada!!");
    logged(conta.getNome());

def seeAccounts(conta):
    for x in contasArray:
        print("\nConta: "+x.getNome()+" Saldo: "+str(x.getValor()));
    input();
    logged(conta.getNome());

def seeExtratos(conta):
    contador = 1;
    if(not extratosArray):
        print("Sem Extratos!!");
        logged(conta.getNome());
    for extratos in extratosArray:
        if(extratos.getConta().getNome() == conta.getNome()):
            print(f"\nExtratos {contador}");
            
            print(f"Conta: {extratos.getConta().getNome()}");
            print(f"Tipo: {extratos.getTipo()}");
            print(f"Valor R$: {extratos.getValor()}");
            contador+=1;
    input();
    logged(conta.getNome());

def logged(nome):
    for x in contasArray:
        if x.getNome() == nome:
            print("\nOla " + x.getNome() + " Bem vindo a o banco bradesco");
            print("Tipo de conta: "+ x.getTipo() + "\n");
            print("Quantidade em R$: "+ str(x.getValor()) + "\n");
            print("O que deseja fazer? 1 - Depositar | 2 - Sacar | 3 - Transferir | 4 - Ver contas | 5 - Ver Extratos" );
            opt = input();
            match opt:
                case "2":
                    sacar(x);
                case "1":
                    depositar(x);
                case "3":
                    transfer(x);
                case "4":
                    seeAccounts(x);
                case "5":
                    seeExtratos(x);
                case _:
                    print("Valor invalido");
                    logged(nome);

def loginAccount():
    print("Qual conta deseja entrar?");
    nome = input();
    for x in contasArray:
        if(x.getNome() == nome):
            logged(nome)
    print("Conta não existe!!");
    main();



def main():
    print("O que deseja fazer? 1 - Entrar na Conta | 2 - Registrar");   
    opt = input();
    match opt:
        case "1":
            loginAccount();
        
        case "2":
            register();
        case _:
            print("Valor Invalido");
            main();

main();