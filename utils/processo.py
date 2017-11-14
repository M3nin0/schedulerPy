import functools

'''
Classe que representa o processo
'''

class Processo():
    def __init__(self, id, tempo, prioridade):
        self.id = id
        # Tempo para executar o processo
        self.tempo = tempo
        self.prioridade = prioridade

    def __eq__(self, obj):
        return self.prioridade == obj

    def __lt__(self, other):
        return self.prioridade > other.prioridade

    def __repr__(self):
        return 'Obj(%r)' % self.value
