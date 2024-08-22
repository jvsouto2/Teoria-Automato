from flask import Flask, render_template, request
from afn import AFN
from afd import AFD
import os

app = Flask(__name__)

# Variáveis globais para armazenar os autômatos gerados
afn = None
afd = None

@app.route('/', methods=['GET', 'POST'])
def index():
    global afn, afd
    if request.method == 'POST':
        try:
            # Processar entrada do usuário para criar AFN
            estados = request.form.get('estados').split(',')
            alfabeto = request.form.get('alfabeto').split(',')
            transicoes = eval(request.form.get('transicoes'))  # Receber como dicionário: {('q0', 'a'): ['q1'], ...}
            estado_inicial = request.form.get('estado_inicial')
            estados_aceitacao = request.form.get('estados_aceitacao').split(',')

            afn = AFN(set(estados), set(alfabeto), transicoes, estado_inicial, set(estados_aceitacao))
            print("AFN criado com sucesso...")
            
            # Converter para AFD usando o método simplificado
            afd = afn.converter_para_afd()
            print("Conversão simplificada de AFN para AFD concluída.")

            # Desenhar os autômatos (se o método de desenho também estiver funcionando corretamente)
            nome_arquivo_afn = afn.desenhar('afn')
            nome_arquivo_afd = afd.desenhar('afd')

            print(f"Imagens geradas: {nome_arquivo_afn}, {nome_arquivo_afd}")

            return render_template('visualizar.html', afn_imagem=nome_arquivo_afn, afd_imagem=nome_arquivo_afd)
        except Exception as e:
            print(f"Erro durante o processamento: {e}")
            return "Erro ao processar os dados. Verifique se as entradas estão corretas."

    return render_template('index.html')

@app.route('/minimizar', methods=['POST'])
def minimizar():
    global afd
    try:
        afd_minimizado = afd.minimizar()
        nome_arquivo_afd_min = afd_minimizado.desenhar('afd_min')
        return render_template('visualizar.html', afn_imagem=None, afd_imagem=nome_arquivo_afd_min, afd_min_imagem=nome_arquivo_afd_min)
    except Exception as e:
        print(f"Erro durante a minimização: {e}")
        return "Erro ao minimizar o AFD."

@app.route('/simular', methods=['POST'])
def simular():
    global afd
    palavra = request.form['palavra']
    resultado = afd.aceita_palavra(palavra)
    if resultado:
        resultado_texto = "A palavra foi aceita pelo AFD."
    else:
        resultado_texto = "A palavra foi rejeitada pelo AFD."
    
    return render_template('simulacao.html', palavra=palavra, resultado=resultado_texto)

@app.route('/equivalencia', methods=['POST'])
def equivalencia():
    global afn, afd

    try:
        equivalente = afn.verificar_equivalencia(afd)
        resultado = "Os autômatos são equivalentes." if equivalente else "Os autômatos não são equivalentes."
        
        return render_template('equivalencia.html', equivalente=resultado)
    except Exception as e:
        print(f"Erro durante a verificação de equivalência: {e}")
        return "Erro ao verificar a equivalência entre AFN e AFD."

if __name__ == '__main__':
    app.run(debug=True, port=5001)
