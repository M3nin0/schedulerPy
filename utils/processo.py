'''
Classe que representa o processo
'''

class Processo():
    def __init__(self, id, tempo, prioridade):
        self.id = id
        # Tempo para executar o processo
        self.tempo = tempo
        self.prioridade = prioridade
