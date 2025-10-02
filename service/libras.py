from flask import jsonify

def processar_dados_libras(dados_entrada):
    if dados_entrada:
        texto_traduzido = "A tradução do sinal foi concluída com sucesso"
        return texto_traduzido
    else:
        return jsonify({"Dados inválidos"})

  