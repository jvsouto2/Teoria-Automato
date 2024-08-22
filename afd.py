from automato_finito import AutomatoFinito

class AFD(AutomatoFinito):
    def aceita_palavra(self, palavra):
        estado_atual = self.estado_inicial
        for simbolo in palavra:
            if simbolo not in self.alfabeto:
                return False
            estado_atual = self.transicoes.get((estado_atual, simbolo))
            if estado_atual is None:
                return False
        return estado_atual in self.estados_aceitacao

    def minimizar(self):
        particao = [set(self.estados_aceitacao), set(self.estados) - set(self.estados_aceitacao)]
        novas_particoes = []

        while True:
            novas_particoes = []
            for grupo in particao:
                subdivisoes = {}
                for estado in grupo:
                    assinatura = tuple(self.transicoes.get((estado, simbolo)) for simbolo in self.alfabeto)
                    if assinatura not in subdivisoes:
                        subdivisoes[assinatura] = {estado}
                    else:
                        subdivisoes[assinatura].add(estado)
                
                novas_particoes.extend(subdivisoes.values())
            
            if novas_particoes == particao:
                break
            particao = novas_particoes

        novo_estado_map = {estado: i for i, grupo in enumerate(particao) for estado in grupo}
        novos_estados = set(novo_estado_map.values())
        novas_transicoes = {}
        for (estado, simbolo), proximo_estado in self.transicoes.items():
            novo_estado_atual = novo_estado_map[estado]
            novo_proximo_estado = novo_estado_map[proximo_estado]
            novas_transicoes[(novo_estado_atual, simbolo)] = novo_proximo_estado

        novo_estado_inicial = novo_estado_map[self.estado_inicial]
        novos_estados_aceitacao = {novo_estado_map[estado] for estado in self.estados_aceitacao}

        return AFD(novos_estados, self.alfabeto, novas_transicoes, novo_estado_inicial, novos_estados_aceitacao)
