from flask import Flask, request, jsonify, render_template
from bd import Dicionario_libras
from flask_cors import CORS
from service.texto import traduzir_texto_para_libras
from service.libras import processar_dados_libras
from service.voz import reconhecer_voz, traduzir_texto_para_libras
from service.translator import traduzir_texto_para_libras_service

app = Flask(__name__, template_folder='templates')
CORS(app) 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/traduzir', methods=['POST']) #API para receber dados em libras e retornar texto
def traduzir_libras_para_texto():
    try:
        dados_brutos = request.files.get('sinal_libras')
        if not dados_brutos:
            dados_brutos = request.data or request.json
        if not dados_brutos:
            return jsonify({"erro"})
        
        texto_resultado = processar_dados_libras(dados_brutos) #chamando o processamento importado de libras.py
        return jsonify({"texto": texto_resultado})

"""@app.route('/traduzir_texto', methods=['POST'])
def traduzir_texto_para_libras():
    data = request.get_json()
    if not data or 'texto' not in data:
        return jsonify({"error": "Nenhum texto fornecido"}), 400

    texto = data['texto'].lower().strip()
    if not texto:
        return jsonify({"videos": []})

    palavras = texto.split()

    # ordenar chaves por número de palavras (maior -> menor) para combinar frases antes de palavras únicas
    chaves_ordenadas = sorted(Dicionario_libras.keys(), key=lambda k: -len(k.split()))

    urls_videos = []
    i = 0
    while i < len(palavras):
        encontrado = False
        for chave in chaves_ordenadas:
            chave_palavras = chave.split()
            if i + len(chave_palavras) <= len(palavras) and palavras[i:i + len(chave_palavras)] == chave_palavras:
                url = Dicionario_libras.get(chave)
                if url:
                    urls_videos.append(url)
                i += len(chave_palavras)
                encontrado = True
                break
        if not encontrado:
            url = Dicionario_libras.get(palavras[i])
            if url:
                urls_videos.append(url)
            i += 1

    return jsonify({"videos": urls_videos})"""

@app.route('/dicionario_libras', methods=['GET'])
def obter_dicionario():
    return jsonify(Dicionario_libras)

"""@app.route('/traduzir_libras_para_texto', methods=['POST'])
def traduzir_libras_para_texto():

    return jsonify({"texto": ""})"""

@app.route('/voz-para-libras', methods=['POST']) #API paara receber audio, transcrever e gerar os videos
def traduzir_voz_para_libras():
    
    try:
        
        dados_audio = request.files.get('audio_file') #receber o arquivo
        
        if not dados_audio:
            return jsonify({"erro": "Nenhum arquivo de áudio foi enviado."}, 400)
        
       
        texto_transcrito = reconhecer_voz(dados_audio) #para reconhecer a voz
        
        if not texto_transcrito:
            return jsonify({"erro": "Não foi possível transcrever a voz."}, 400)
            
        
        videos_libras = traduzir_texto_para_libras(texto_transcrito)

        
        return jsonify({
            "texto_original": texto_transcrito,
            "videos": videos_libras
        }) #retornar em JSON e a lista de links para os videos

    except Exception as e: #tratamento de erros
        
        print(f"Erro durante a tradução de voz para LIBRAS: {e}")
        return jsonify({"erro": f"Erro do servidor: {str(e)}"}, 500)

"""@app.route('/traduzir_voz_para_libras', methods=['POST'])
def traduzir_voz_para_libras():
    return jsonify({"videos": []})"""

if __name__ == '__main__':
   
    app.run(debug=True)
