class func:
    def __init__(self, name='', sala=0, data=''):
        self.name = name
        self.sala = sala
        self.data = data
    def __repr__(self):
        return "Nome: " + self.name + "\n" + "Salario: " + str(self.sala) + "\n" + "Data de admissão: " + self.data

    def nome(self, name):
        self.name = name

    def salario(self, sala):
        self.sala = sala

    def admiss(self, data):
        self.data = data


class geren(func):
    def __init__(self, name='', sala=0, data=''):
        self.name = name
        self.sala = sala*1.15
        self.data = data
    def salario(self, sala):
        self.sala = sala*1.15