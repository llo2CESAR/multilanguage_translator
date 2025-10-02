
from flask import request, jsonify
from bd import Dicionario_libras

app = Flask(__name__) 

@app.route('/traduzir-texto', methods=['POST'])
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

    return jsonify({"videos": urls_videos})