class Roupa:
    def __init__(self, url, modelo, tem=True):
        self.url = url
        self._modelo = modelo
        self._valor = 0
        if tem:
            self._disponivel = "Disponível"
        else:
            self._disponivel = "Não Disponível"

    @property
    def modelo(self):
        return self._modelo

    @property
    def valor(self):
        return self._valor

    def update_valor(self, valor_atual):
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
        return f'{self.modelo}\n{self.valor}\n{self.disponivel}\n{self.url}'




