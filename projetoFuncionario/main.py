
class func:
    def __init__(self, name='', sala=0, data=''):
        self.name = name
        self.sala = sala
        self.data = data
    def __repr__(self):
        return "Nome: " + self.name + "\n" + "Salario: " + str(self.sala) + "\n" + "Data de admissão: " + self.data

    def nome(self, name):
        self.name = input()

    def salario(self, sala):
        self.sala = float(input())

    def admiss(self, data):
        self.data = input()


funcionario = []
while True:
    print("=================[welcome}=====================")
    print("Escolha a funcão que desejar")
    print("1)Adicionar Funcionario\n2)Consultar Funcionario\n3)Editar")
    op = int(input())
    if op == 1:
        n = input("Digite o nome do funcionario: ")
        s = float(input("Digite o salario do Funcionario: "))
        d = input('Digite a data de admissão: ')
        colab=func(n,s,d)
        funcionario.append(colab)
    elif op == 2:
        i=0
        print("Digite o funcionario que deseja consultar:")
        for p in funcionario:
            i += 1
            print(i,")",p.name)
        o = int(input())
        print(funcionario[o-1])
    elif op==3:
        i = 0
        print("Digite o funcionario que deseja editar:")
        for p in funcionario:
            i += 1
            print(i, ")", p.name)
        switch=funcionario[o-1]
        switch.nome(input())
    else:
        print("Digite uma opção valida!!!")