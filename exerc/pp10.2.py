''''Use o pensamento recursivo para implementar a função
 recursiva saúde() que, sobre a entrada inteira n, exibe n
 strings 'Hip ' seguidos por Hurrah.'''

def saude(n):
    if n<=0:
        print("Hurrah!!!")
    else:
        print("Hip",end=" ")
        saude(n-1)
