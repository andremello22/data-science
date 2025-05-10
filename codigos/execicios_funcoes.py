def soma(x, y):
    return x+y

def dobroDaSoma(soma):
    def g(*args, **kwargs):
        return soma(*args, **kwargs)*2
    return g

resutado = dobroDaSoma(soma)
print(resutado(10,10)) # 40

