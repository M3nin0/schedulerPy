class Processo():
    def __init__(self, id = -1, tempo_de_execucao = -1, prioridade = -1):
        self.id = id
        self.tempo_de_execucao = tempo_de_execucao
        self.prioridade = prioridade

    def __eq__(self, obj):
        return self.prioridade == obj

    def __lt__(self, obj):
        return self.prioridade > obj.prioridade

    def __repr__(self):
        return '%r' % self.prioridade
