class Roupa:
    def __init__(self, codigo, url, modelo, tem=True):
        self._codigo = codigo
        self.url = url
        self._modelo = modelo
        self._valor = 0
        if tem:
            self._disponivel = "Disponível"
        else:
            self._disponivel = "Não Disponível"

    @property
    def codigo(self):
        return self._codigo

    @property
    def modelo(self):
        return self._modelo

    @property
    def valor(self):
        return self._valor

    def update_valor(self, valor_atual):
        valor_atual = ((int(valor_atual.split('.')[0])*100) + int((valor_atual.split('.')[1])))
        self._valor += valor_atual

    @property
    def disponivel(self):
        return self._disponivel

    @disponivel.setter
    def disponivel(self, tem):
        if tem:
            self._disponivel = "Disponível"
        else:
            self._disponivel = "Não Disponível"

    def __str__(self):
        return f'Código: {self.codigo}\n{self.modelo}\nR${str(self.valor/100).replace(".",",")}\n{self.disponivel}\n\n{self.url}\n'




