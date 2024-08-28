import itertools
from graphviz import Digraph
from automato_finito import AutomatoFinito
from afd import AFD

class AFN(AutomatoFinito):

    def desenhar(self, nome_arquivo):
        dot = Digraph()
        dot.attr(rankdir='LR')
        
        # Adicionar estados
        for estado in self.estados:
            if estado in self.estados_aceitacao:
                dot.node(str(estado), shape='doublecircle')
            else:
                dot.node(str(estado))
        
        # Adicionar transições
        for (estado, simbolo), proximos_estados in self.transicoes.items():
            for proximo_estado in proximos_estados:
                dot.edge(str(estado), str(proximo_estado), label=simbolo)
        
        # Indicar o estado inicial
        dot.attr('node', shape='point')
        dot.edge('', str(self.estado_inicial))
        
        dot.render(f'static/{nome_arquivo}', format='png', cleanup=True)
        return f'{nome_arquivo}.png'

    def converter_para_afd(self):
        novos_estados = []
        novas_transicoes = {}
        estados_iniciais = frozenset([self.estado_inicial])
        novos_estados.append(estados_iniciais)
        estados_aceitacao_afd = []

        estado_map = {estados_iniciais: 'S0'}  # Mapeia conjuntos de estados para nomes únicos
        prox_estado_id = 1

        while novos_estados:
            estado_atual = novos_estados.pop(0)
            nome_estado_atual = estado_map[estado_atual]
            for simbolo in self.alfabeto:
                proximos_estados = set()
                for estado in estado_atual:
                    proximos_estados.update(self.transicoes.get((estado, simbolo), []))
                proximos_estados = frozenset(proximos_estados)

                if proximos_estados:
                    if proximos_estados not in estado_map:
                        estado_map[proximos_estados] = f'S{prox_estado_id}'
                        prox_estado_id += 1
                        novos_estados.append(proximos_estados)
                    novas_transicoes[(nome_estado_atual, simbolo)] = estado_map[proximos_estados]
                else:
                    pass

            if estado_atual & self.estados_aceitacao:
                estados_aceitacao_afd.append(estado_map[estado_atual])

        estados_afd = set(estado_map.values())
        estado_inicial_afd = estado_map[estados_iniciais]
        estados_aceitacao_afd = set(estados_aceitacao_afd)

        return AFD(estados_afd, self.alfabeto, novas_transicoes, estado_inicial_afd, estados_aceitacao_afd)
    
    def gerar_palavras_iter(self, alfabeto, tamanho_max):
        palavras = []
        for tamanho in range(1, tamanho_max + 1):
            palavras.extend(''.join(p) for p in itertools.product(alfabeto, repeat=tamanho))
        return palavras
    
    def verificar_equivalencia(self, afd):
        palavras_teste = self.gerar_palavras_iter(list(self.alfabeto), 10)
        
        for palavra in palavras_teste:
            aceita_afn = self.aceitar_palavra(palavra)
            aceita_afd = afd.aceita_palavra(palavra)
            if aceita_afn != aceita_afd:
                return False
        return True

    def aceitar_palavra(self, palavra):
        return self._aceita_palavra_recursivo(self.estado_inicial, palavra)

    def _aceita_palavra_recursivo(self, estado_atual, palavra):
        if not palavra:
            return estado_atual in self.estados_aceitacao
        simbolo = palavra[0]
        proximos_estados = self.transicoes.get((estado_atual, simbolo), [])
        for proximo_estado in proximos_estados:
            if self._aceita_palavra_recursivo(proximo_estado, palavra[1:]):
                return True
        return False
