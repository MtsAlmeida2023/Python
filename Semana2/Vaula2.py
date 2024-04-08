import random
class mylist(list):
    def choice(self):
        return random.choice(self)

'''estudando o conceito de herança onde 
a classe chamada mylist herda os metodos 
de uma lista normal e é adcionado o 
metodo "choice" no objeto
'''